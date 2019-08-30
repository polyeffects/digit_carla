/* polylfo.lv2
 *
 * Copyright (C) 2019 Poly Effects <info@polyeffects.com>
 * 
 * based on midifilter by 
 *
 * Copyright (C) 2013 Robin Gareus <robin@gareus.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#ifdef _WIN32
#define random() rand()
#define srandom(X) srand(X)
#endif

#include "polylfo.h"


// ports needed midi out, trigger in, which CC to send on
// later CV out

/******************************************************************************
 * common 'helper' functions
 */
static int midi_limit_val(const int d) {
    if (d < 0) return 0;
    if (d > 127) return 127;
    return d;
}

static int midi_limit_chn(const int c) {
    if (c < 0) return 0;
    if (c > 15) return 15;
    return c;
}

static int midi_valid(const int d) {
    if (d >=0 && d < 128) return 1;
    return 0;
}

static int midi_14bit(const uint8_t * const b) {
    return ((b[1]) | (b[2]<<7));
}

static int midi_is_panic(const uint8_t * const b, const int s) {
    if (s == 3
            && (b[0] & 0xf0) == MIDI_CONTROLCHANGE
            && ( (b[1]&0x7f) == 123 || (b[1]&0x7f) == 120 )
            && (b[2]&0x7f) == 0)
        return 1;
    return 0;
}

static float normrand(const float dev) {
    static char initialized = 0;
    static float randmem;

    if (!initialized) {
        randmem =  2.0 * random() / (float)RAND_MAX - 1;
        initialized = 1;
    }

    float U = 2.0 * random() / (float)RAND_MAX - 1; //rand E(-1,1)
    float S = SQUARE(U) + SQUARE(randmem); //map 2 random vars to unit circle

    if(S >= 1.0f) {
        //repull RV if outside unit circle
        U = 2.0* random() / (float)RAND_MAX - 1;
        S = SQUARE(U) + SQUARE(randmem);
        if(S >= 1.0f) {
            U = 2.0* random() / (float)RAND_MAX - 1;
            S = SQUARE(U) + SQUARE(randmem);
            if(S >= 1.0f) {
                U=0;
            }
        }
    }
    randmem = U; //store RV for next round
    return U ? (dev * U * sqrt(-2.0 * log(S) / S)) : 0;
}

/**
 * add a midi message to the output port
 */
    void
forge_midimessage(PolyLFO* self,
        uint32_t tme,
        const uint8_t* const buffer,
        uint32_t size)
{
    LV2_Atom midiatom;
    midiatom.type = self->uris.midi_MidiEvent;
    midiatom.size = size;

    if (0 == lv2_atom_forge_frame_time(&self->forge, tme)) return;
    if (0 == lv2_atom_forge_raw(&self->forge, &midiatom, sizeof(LV2_Atom))) return;
    if (0 == lv2_atom_forge_raw(&self->forge, buffer, size)) return;
    lv2_atom_forge_pad(&self->forge, sizeof(LV2_Atom) + size);
}

/**
 * Update the current position based on a host message.  This is called by
 * run() when a time:Position is received.
 */
static void
update_position(PolyLFO* self, const LV2_Atom_Object* obj)
{
    const PolyLFOURIs* uris = &self->uris;

    // Received new transport position/speed
    LV2_Atom *beat = NULL, *bpm = NULL, *speed = NULL;
    LV2_Atom *fps = NULL, *frame = NULL;
    lv2_atom_object_get(obj,
            uris->time_barBeat, &beat,
            uris->time_beatsPerMinute, &bpm,
            uris->time_speed, &speed,
            uris->time_frame, &frame,
            uris->time_fps, &fps,
            NULL);
    if (bpm && bpm->type == uris->atom_Float) {
        // Tempo changed, update BPM
        self->bpm = ((LV2_Atom_Float*)bpm)->body;
        self->available_info |= NFO_BPM;
    }
    if (speed && speed->type == uris->atom_Float) {
        // Speed changed, e.g. 0 (stop) to 1 (play)
        self->speed = ((LV2_Atom_Float*)speed)->body;
        self->available_info |= NFO_SPEED;
    }
    if (beat && beat->type == uris->atom_Float) {
        const double samples_per_beat = 60.0 / self->bpm * self->samplerate;
        self->bar_beats    = ((LV2_Atom_Float*)beat)->body;
        self->beat_beats   = self->bar_beats - floor(self->bar_beats);
        self->pos_bbt      = self->beat_beats * samples_per_beat;
        self->available_info |= NFO_BEAT;
    }
    if (fps && fps->type == uris->atom_Float) {
        self->frames_per_second = ((LV2_Atom_Float*)fps)->body;
        self->available_info |= NFO_FPS;
    }
    if (frame && frame->type == uris->atom_Long) {
        self->pos_frame = ((LV2_Atom_Long*)frame)->body;
        self->available_info |= NFO_FRAME;
    }
}
/******************************************************************************
 * LV2
 */

float smoothstep(float x) {
    // Scale, bias and saturate x to 0..1 range
    // x = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0); 
    // Evaluate polynomialv
    //
    return x * x * (3 - 2 * x);
}

float accell(float x){
    return x * x;
}

float decell(float v){
    return 1 - (1 - v) * (1 - v); 
}

/* float random(v){ */
/*     return Math.random() * v; */
/* } */

/* float linear_interpolate(float y1, float y2, float mu){ */
/*     return (y1*(1-mu)+y2*mu); */
/* } */

/* float cosine_interpolate(y1, y2, mu) { */
/*     float mu2; */
/*     mu2 = (1-Math.cos(mu*Math.PI))/2; */
/*     return (y1*(1-mu2)+y2*mu2); */
/* } */
static float
generate_lfo(LV2_Handle instance, const float cur_time)
{
    // TODO cope with looping vs not
    // time in our parameters is in bars. 
    // which segment are we in?
    PolyLFO* self = (PolyLFO*)instance;
    int start_seg = 0;
    int end_seg = 1;
	const float num_points = *(self->num_points);
    for (int i = 0; i < num_points; i++) {
        // if point time > current_time prev point is the start of this segement 
        if (*(self->time[i]) > cur_time) {
            break;
        }
        start_seg = i;
    }
    if (start_seg+1 > MAX_POINTS){
        end_seg = 0;
    }
    else {
        end_seg = start_seg + 1;
    }
    // generate according to segment type
    // send MIDI on specified CC and channel


    // linear
    // var m = (seg_y2 - seg_y1) / (seg_x2 - seg_x1);
    float mu; // diff x
    /* float bend_factor; */
    const float start_time = *(self->time[start_seg]);
    const float end_time = *(self->time[end_seg]);
	const float style = *(self->style[start_seg]);
    const float start_value = *(self->value[start_seg]);
    const float end_value = *(self->value[end_seg]);

    /* for (int j = seg_x1; j < seg_x2; j++) { */
    mu = (cur_time - start_time) / (end_time - start_time); // 0-1 how far through seg
    // v = v; // linear
    if (style <= 0.5) {
        //if linear do nothing
    } else if (style <= 1) {
        mu = smoothstep(mu);
    } else if (style <= 2) {
        mu = accell(mu);
    } else if (style <= 3) {
        mu = decell(mu);
    } else if (style <= 4) {
        mu = 0;
    } else if (style <= 5) {
        /* float r = (float) ((double)rand()/(double)(RAND_MAX)) * 2.0 - 1.0; */
        /* mu = RAIL(mu * r, -1.0, 1.0); */
        mu = decell(mu);
    }
    return (start_value * (1-mu)+end_value*mu);
}

    static void
run(LV2_Handle instance, uint32_t n_samples)
{
    PolyLFO* self = (PolyLFO*)instance;
    self->n_samples = n_samples;

	/* const float        trigger   = *(self->trigger); */
	/* const float        num_points   = *(self->num_points); */
	/* const float* const input  = amp->input; */
	/* const float* const input  = amp->input; */
	/* float* const       output = self->output; */
    const uint8_t channel = (uint8_t) *(self->channel); //channel 0 is 1
    const uint8_t cc_num = (uint8_t) *(self->cc_num); 


    if (!self->midiout || !self->midiin) {
        /* eg. ARDOUR::LV2Plugin::latency_compute_run()
         * -> midi ports are not yet connected
         */
        goto out;
    }

    /* prepare midiout port */
    const uint32_t capacity = self->midiout->atom.size;
    lv2_atom_forge_set_buffer(&self->forge, (uint8_t*)self->midiout, capacity);
    lv2_atom_forge_sequence_head(&self->forge, &self->frame, 0);

    /* process events on the midiin port */
    LV2_Atom_Event* ev = lv2_atom_sequence_begin(&(self->midiin)->body);
    while(!lv2_atom_sequence_is_end(&(self->midiin)->body, (self->midiin)->atom.size, ev)) {
        /* if (ev->body.type == self->uris.midi_MidiEvent) { */

			/* const uint8_t* const msg = (const uint8_t*)(ev + 1); */
			/* if (lv2_midi_message_type(msg) == LV2_MIDI_MSG_PGM_CHANGE && ((msg[0] & 0x0F) == (channel - 1))) { */	

				/* fprintf(stderr, "got program change\n"); */
				/* // channel msg[0] */ 
				/* // new program msg[1] */
			/* } */
        /*     /1* self->filter_fn(self, ev->time.frames, (uint8_t*)(ev+1), ev->body.size); *1/ */
        /* } */
        if (ev->body.type == self->uris.atom_Blank || ev->body.type == self->uris.atom_Object) {
            const LV2_Atom_Object* obj = (LV2_Atom_Object*)&ev->body;
            if (obj->body.otype == self->uris.time_Position) {
                update_position(self, obj);
            }
        }
        ev = lv2_atom_sequence_next(ev);
    }

    /* increment position for next cycle */
    if (self->available_info & NFO_BEAT) {
        float bpm = self->bpm;
        if (self->available_info & NFO_SPEED) {
            bpm *= self->speed;
        }
        if (bpm != 0) {
            const double samples_per_beat = 60.0 * self->samplerate / bpm;
            self->bar_beats    += (double) n_samples / samples_per_beat;
            self->beat_beats   = self->bar_beats - floor(self->bar_beats);
            self->pos_bbt      = self->beat_beats * samples_per_beat;
        }
    }
    if (self->available_info & NFO_FRAME) {
        self->pos_frame += n_samples;
    }

out:
    // send MIDI
    if (self->bpm != 0){
        float out;
        uint8_t buf[3];
        uint8_t cur_lfo;
        out = generate_lfo(instance, fmod(self->bar_beats, 4) / 4); // TODO get beats per bar 
        cur_lfo = (uint8_t) (out * 127);      // map float to MIDI range 0,1 to 0-127
        if (cur_lfo == self->prev_sent){
            return; // lfo value is same as last sent
        }
        self->prev_sent = cur_lfo;
        // if cc is different to previous sent value
        // send control change on the correct CC and channel
        buf[0] = MIDI_CONTROLCHANGE | (channel - 1);      
        buf[1] = cc_num;  // CC 102-119 for LFOs
        buf[2] = midi_limit_val(cur_lfo);

        forge_midimessage(self, 0 /*frame time*/, buf, 3);
    }
}


    static inline void
map_mf_uris(LV2_URID_Map* map, PolyLFOURIs* uris)
{
    uris->atom_Blank         = map->map(map->handle, LV2_ATOM__Blank);
    uris->atom_Object        = map->map(map->handle, LV2_ATOM__Object);
    uris->midi_MidiEvent     = map->map(map->handle, LV2_MIDI__MidiEvent);
    uris->atom_Sequence      = map->map(map->handle, LV2_ATOM__Sequence);

    uris->atom_Long           = map->map(map->handle, LV2_ATOM__Long);
    uris->atom_Float          = map->map(map->handle, LV2_ATOM__Float);
    uris->time_Position       = map->map(map->handle, LV2_TIME__Position);
    uris->time_barBeat        = map->map(map->handle, LV2_TIME__barBeat);
    uris->time_beatsPerMinute = map->map(map->handle, LV2_TIME__beatsPerMinute);
    uris->time_speed          = map->map(map->handle, LV2_TIME__speed);
    uris->time_frame          = map->map(map->handle, LV2_TIME__frame);
    uris->time_fps            = map->map(map->handle, LV2_TIME__framesPerSecond);
}

    static LV2_Handle
instantiate(const LV2_Descriptor*         descriptor,
        double                    rate,
        const char*               bundle_path,
        const LV2_Feature* const* features)
{
    int i;
    PolyLFO* self = (PolyLFO*)calloc(1, sizeof(PolyLFO));
    if (!self) return NULL;

    for (i=0; features[i]; ++i) {
        if (!strcmp(features[i]->URI, LV2_URID__map)) {
            self->map = (LV2_URID_Map*)features[i]->data;
        }
    }

    if (!self->map) {
        fprintf(stderr, "midifilter.lv2 error: Host does not support urid:map\n");
        free(self);
        return NULL;
    }

    map_mf_uris(self->map, &self->uris);
    lv2_atom_forge_init(&self->forge, self->map);
    self->samplerate = rate;
    self->bpm = 120;
    /* self->num_points = 1.0f; */
    /* self->trigger = 0.0f; */
    self->prev_sent = 0;


    for (i=0; i < MAX_POINTS; ++i) {
        self->time[i] = 0;
        self->value[i] = 0;
        self->style[i] = 0;
    }

    return (LV2_Handle)self;
}

#define TIME_PORT(n) \
    case (n+4): \
self->time[n] = (const float*)data; \
break;

#define VALUE_PORT(n) \
    case (n+4+MAX_POINTS): \
self->value[n] = (const float*)data; \
break;

#define STYLE_PORT(n) \
    case (n+4+MAX_POINTS+MAX_POINTS): \
self->style[n] = (const float*)data; \
break;

    static void
connect_port(LV2_Handle    instance,
        uint32_t   port,
        void*      data)
{
    PolyLFO* self = (PolyLFO*)instance;

    switch (port) {
        case 0:
            self->midiin = (const LV2_Atom_Sequence*)data;
            break;
        case 1:
            self->midiout = (LV2_Atom_Sequence*)data;
            break;
        case 2:
            self->trigger = (float*)data;
            break;
        case 3:
            self->num_points = (const float*)data;
            break;
            LOOP_CFG(TIME_PORT)
            LOOP_CFG(VALUE_PORT)
            LOOP_CFG(STYLE_PORT)
        case 52:
            self->channel = (const float*)data;
        case 53:
            self->cc_num = (const float*)data;
        default:
                break;
    }
}

    static void
cleanup(LV2_Handle instance)
{
    PolyLFO* self = (PolyLFO*)instance;
    if (self->cleanup_fn) {
        self->cleanup_fn(self);
    }

    free(instance);
}

    const void*
extension_data(const char* uri)
{
    return NULL;
}

static const LV2_Descriptor descriptor = {
	LFO_URI,
	instantiate,
	connect_port,
	NULL,
	run,
	NULL,
	cleanup,
	extension_data
};

#undef LV2_SYMBOL_EXPORT
#ifdef _WIN32
#    define LV2_SYMBOL_EXPORT __declspec(dllexport)
#else
#    define LV2_SYMBOL_EXPORT  __attribute__ ((visibility ("default")))
#endif
LV2_SYMBOL_EXPORT
const LV2_Descriptor*
lv2_descriptor(uint32_t index)
{
	switch (index) {
	case 0:  return &descriptor;
	default: return NULL;
	}
}
/* vi:set ts=4 sts=4 sw=4: */
