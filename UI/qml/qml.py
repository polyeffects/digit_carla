# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Wed Jan 9 17:46:39 2019
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x0e\x80\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: https:/\
/www.qt.io/licen\
sing/\x0d\x0a**\x0d\x0a** Th\
is file is part \
of the examples \
of the Qt Toolki\
t.\x0d\x0a**\x0d\x0a** $QT_B\
EGIN_LICENSE:BSD\
$\x0d\x0a** Commercial\
 License Usage\x0d\x0a\
** Licensees hol\
ding valid comme\
rcial Qt license\
s may use this f\
ile in\x0d\x0a** accor\
dance with the c\
ommercial licens\
e agreement prov\
ided with the\x0d\x0a*\
* Software or, a\
lternatively, in\
 accordance with\
 the terms conta\
ined in\x0d\x0a** a wr\
itten agreement \
between you and \
The Qt Company. \
For licensing te\
rms\x0d\x0a** and cond\
itions see https\
://www.qt.io/ter\
ms-conditions. F\
or further\x0d\x0a** i\
nformation use t\
he contact form \
at https://www.q\
t.io/contact-us.\
\x0d\x0a**\x0d\x0a** BSD Lic\
ense Usage\x0d\x0a** A\
lternatively, yo\
u may use this f\
ile under the te\
rms of the BSD l\
icense\x0d\x0a** as fo\
llows:\x0d\x0a**\x0d\x0a** \x22\
Redistribution a\
nd use in source\
 and binary form\
s, with or witho\
ut\x0d\x0a** modificat\
ion, are permitt\
ed provided that\
 the following c\
onditions are\x0d\x0a*\
* met:\x0d\x0a**   * R\
edistributions o\
f source code mu\
st retain the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er.\x0d\x0a**   * Redi\
stributions in b\
inary form must \
reproduce the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er in\x0d\x0a**     th\
e documentation \
and/or other mat\
erials provided \
with the\x0d\x0a**    \
 distribution.\x0d\x0a\
**   * Neither t\
he name of The Q\
t Company Ltd no\
r the names of i\
ts\x0d\x0a**     contr\
ibutors may be u\
sed to endorse o\
r promote produc\
ts derived\x0d\x0a**  \
   from this sof\
tware without sp\
ecific prior wri\
tten permission.\
\x0d\x0a**\x0d\x0a**\x0d\x0a** THI\
S SOFTWARE IS PR\
OVIDED BY THE CO\
PYRIGHT HOLDERS \
AND CONTRIBUTORS\
\x0d\x0a** \x22AS IS\x22 AND\
 ANY EXPRESS OR \
IMPLIED WARRANTI\
ES, INCLUDING, B\
UT NOT\x0d\x0a** LIMIT\
ED TO, THE IMPLI\
ED WARRANTIES OF\
 MERCHANTABILITY\
 AND FITNESS FOR\
\x0d\x0a** A PARTICULA\
R PURPOSE ARE DI\
SCLAIMED. IN NO \
EVENT SHALL THE \
COPYRIGHT\x0d\x0a** OW\
NER OR CONTRIBUT\
ORS BE LIABLE FO\
R ANY DIRECT, IN\
DIRECT, INCIDENT\
AL,\x0d\x0a** SPECIAL,\
 EXEMPLARY, OR C\
ONSEQUENTIAL DAM\
AGES (INCLUDING,\
 BUT NOT\x0d\x0a** LIM\
ITED TO, PROCURE\
MENT OF SUBSTITU\
TE GOODS OR SERV\
ICES; LOSS OF US\
E,\x0d\x0a** DATA, OR \
PROFITS; OR BUSI\
NESS INTERRUPTIO\
N) HOWEVER CAUSE\
D AND ON ANY\x0d\x0a**\
 THEORY OF LIABI\
LITY, WHETHER IN\
 CONTRACT, STRIC\
T LIABILITY, OR \
TORT\x0d\x0a** (INCLUD\
ING NEGLIGENCE O\
R OTHERWISE) ARI\
SING IN ANY WAY \
OUT OF THE USE\x0d\x0a\
** OF THIS SOFTW\
ARE, EVEN IF ADV\
ISED OF THE POSS\
IBILITY OF SUCH \
DAMAGE.\x22\x0d\x0a**\x0d\x0a**\
 $QT_END_LICENSE\
$\x0d\x0a**\x0d\x0a*********\
****************\
****************\
****************\
****************\
***/\x0d\x0a\x0d\x0a//import\
 QtQuick 2.12\x0d\x0a/\
/import QtQuick.\
Controls 2.12\x0d\x0ai\
mport QtQuick 2.\
9\x0d\x0aimport QtQuic\
k.Controls 2.3\x0d\x0a\
// This containe\
r and the transf\
orm on the Label\
 are\x0d\x0a// necessa\
ry to get precis\
e bounding rect \
of the text for \
layouting reason\
s,\x0d\x0a// since som\
e of the labels'\
 font sizes can \
get quite large.\
\x0d\x0aItem {\x0d\x0a    id\
: root\x0d\x0a    impl\
icitHeight: labe\
lTextMetrics.tig\
htBoundingRect.h\
eight\x0d\x0a    impli\
citWidth: label.\
implicitWidth\x0d\x0a\x0d\
\x0a    property al\
ias text: label.\
text\x0d\x0a    proper\
ty alias font: l\
abel.font\x0d\x0a    p\
roperty alias ho\
rizontalAlignmen\
t: label.horizon\
talAlignment\x0d\x0a  \
  property alias\
 verticalAlignme\
nt: label.vertic\
alAlignment\x0d\x0a   \
 property bool g\
lowEnabled: true\
\x0d\x0a    property c\
olor glowColor: \
colorGlow\x0d\x0a    p\
roperty color co\
lor: colorBright\
\x0d\x0a\x0d\x0a    Label {\x0d\
\x0a        id: lab\
el\x0d\x0a        anch\
ors.baseline: ro\
ot.baseline\x0d\x0a   \
     color: root\
.color\x0d\x0a\x0d\x0a      \
  layer.enabled:\
 root.glowEnable\
d\x0d\x0a        layer\
.effect: CustomG\
low {\x0d\x0a         \
   color: glowCo\
lor\x0d\x0a        }\x0d\x0a\
\x0d\x0a        TextMe\
trics {\x0d\x0a       \
     id: labelTe\
xtMetrics\x0d\x0a     \
       text: lab\
el.text\x0d\x0a       \
     font: label\
.font\x0d\x0a        }\
\x0d\x0a\x0d\x0a        tran\
sform: Translate\
 {\x0d\x0a            \
y: -labelTextMet\
rics.tightBoundi\
ngRect.y\x0d\x0a      \
  }\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x0b\xb7\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: https:/\
/www.qt.io/licen\
sing/\x0d\x0a**\x0d\x0a** Th\
is file is part \
of the examples \
of the Qt Toolki\
t.\x0d\x0a**\x0d\x0a** $QT_B\
EGIN_LICENSE:BSD\
$\x0d\x0a** Commercial\
 License Usage\x0d\x0a\
** Licensees hol\
ding valid comme\
rcial Qt license\
s may use this f\
ile in\x0d\x0a** accor\
dance with the c\
ommercial licens\
e agreement prov\
ided with the\x0d\x0a*\
* Software or, a\
lternatively, in\
 accordance with\
 the terms conta\
ined in\x0d\x0a** a wr\
itten agreement \
between you and \
The Qt Company. \
For licensing te\
rms\x0d\x0a** and cond\
itions see https\
://www.qt.io/ter\
ms-conditions. F\
or further\x0d\x0a** i\
nformation use t\
he contact form \
at https://www.q\
t.io/contact-us.\
\x0d\x0a**\x0d\x0a** BSD Lic\
ense Usage\x0d\x0a** A\
lternatively, yo\
u may use this f\
ile under the te\
rms of the BSD l\
icense\x0d\x0a** as fo\
llows:\x0d\x0a**\x0d\x0a** \x22\
Redistribution a\
nd use in source\
 and binary form\
s, with or witho\
ut\x0d\x0a** modificat\
ion, are permitt\
ed provided that\
 the following c\
onditions are\x0d\x0a*\
* met:\x0d\x0a**   * R\
edistributions o\
f source code mu\
st retain the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er.\x0d\x0a**   * Redi\
stributions in b\
inary form must \
reproduce the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er in\x0d\x0a**     th\
e documentation \
and/or other mat\
erials provided \
with the\x0d\x0a**    \
 distribution.\x0d\x0a\
**   * Neither t\
he name of The Q\
t Company Ltd no\
r the names of i\
ts\x0d\x0a**     contr\
ibutors may be u\
sed to endorse o\
r promote produc\
ts derived\x0d\x0a**  \
   from this sof\
tware without sp\
ecific prior wri\
tten permission.\
\x0d\x0a**\x0d\x0a**\x0d\x0a** THI\
S SOFTWARE IS PR\
OVIDED BY THE CO\
PYRIGHT HOLDERS \
AND CONTRIBUTORS\
\x0d\x0a** \x22AS IS\x22 AND\
 ANY EXPRESS OR \
IMPLIED WARRANTI\
ES, INCLUDING, B\
UT NOT\x0d\x0a** LIMIT\
ED TO, THE IMPLI\
ED WARRANTIES OF\
 MERCHANTABILITY\
 AND FITNESS FOR\
\x0d\x0a** A PARTICULA\
R PURPOSE ARE DI\
SCLAIMED. IN NO \
EVENT SHALL THE \
COPYRIGHT\x0d\x0a** OW\
NER OR CONTRIBUT\
ORS BE LIABLE FO\
R ANY DIRECT, IN\
DIRECT, INCIDENT\
AL,\x0d\x0a** SPECIAL,\
 EXEMPLARY, OR C\
ONSEQUENTIAL DAM\
AGES (INCLUDING,\
 BUT NOT\x0d\x0a** LIM\
ITED TO, PROCURE\
MENT OF SUBSTITU\
TE GOODS OR SERV\
ICES; LOSS OF US\
E,\x0d\x0a** DATA, OR \
PROFITS; OR BUSI\
NESS INTERRUPTIO\
N) HOWEVER CAUSE\
D AND ON ANY\x0d\x0a**\
 THEORY OF LIABI\
LITY, WHETHER IN\
 CONTRACT, STRIC\
T LIABILITY, OR \
TORT\x0d\x0a** (INCLUD\
ING NEGLIGENCE O\
R OTHERWISE) ARI\
SING IN ANY WAY \
OUT OF THE USE\x0d\x0a\
** OF THIS SOFTW\
ARE, EVEN IF ADV\
ISED OF THE POSS\
IBILITY OF SUCH \
DAMAGE.\x22\x0d\x0a**\x0d\x0a**\
 $QT_END_LICENSE\
$\x0d\x0a**\x0d\x0a*********\
****************\
****************\
****************\
****************\
***/\x0d\x0a\x0d\x0a//import\
 QtQuick 2.12\x0d\x0a/\
/import QtQuick.\
Layouts 1.12\x0d\x0a//\
import QtQuick.C\
ontrols 2.12\x0d\x0aim\
port QtQuick 2.9\
\x0d\x0aimport QtQuick\
.Layouts 1.3\x0d\x0aim\
port QtQuick.Con\
trols 2.3\x0d\x0a\x0d\x0aBut\
ton {\x0d\x0a    id: b\
utton\x0d\x0a    check\
able: true\x0d\x0a    \
font.pixelSize: \
fontSizeExtraSma\
ll\x0d\x0a    leftPadd\
ing: 4\x0d\x0a    righ\
tPadding: 4\x0d\x0a   \
 topPadding: 12\x0d\
\x0a    bottomPaddi\
ng: 12\x0d\x0a    impl\
icitWidth: 60\x0d\x0a \
   implicitHeigh\
t: 90\x0d\x0a\x0d\x0a    ico\
n.name: \x22placeho\
lder\x22\x0d\x0a    icon.\
width: 44\x0d\x0a    i\
con.height: 44\x0d\x0a\
    display: But\
ton.TextUnderIco\
n\x0d\x0a}\x0d\x0a\
\x00\x00\x0aM\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: https:/\
/www.qt.io/licen\
sing/\x0d\x0a**\x0d\x0a** Th\
is file is part \
of the examples \
of the Qt Toolki\
t.\x0d\x0a**\x0d\x0a** $QT_B\
EGIN_LICENSE:BSD\
$\x0d\x0a** Commercial\
 License Usage\x0d\x0a\
** Licensees hol\
ding valid comme\
rcial Qt license\
s may use this f\
ile in\x0d\x0a** accor\
dance with the c\
ommercial licens\
e agreement prov\
ided with the\x0d\x0a*\
* Software or, a\
lternatively, in\
 accordance with\
 the terms conta\
ined in\x0d\x0a** a wr\
itten agreement \
between you and \
The Qt Company. \
For licensing te\
rms\x0d\x0a** and cond\
itions see https\
://www.qt.io/ter\
ms-conditions. F\
or further\x0d\x0a** i\
nformation use t\
he contact form \
at https://www.q\
t.io/contact-us.\
\x0d\x0a**\x0d\x0a** BSD Lic\
ense Usage\x0d\x0a** A\
lternatively, yo\
u may use this f\
ile under the te\
rms of the BSD l\
icense\x0d\x0a** as fo\
llows:\x0d\x0a**\x0d\x0a** \x22\
Redistribution a\
nd use in source\
 and binary form\
s, with or witho\
ut\x0d\x0a** modificat\
ion, are permitt\
ed provided that\
 the following c\
onditions are\x0d\x0a*\
* met:\x0d\x0a**   * R\
edistributions o\
f source code mu\
st retain the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er.\x0d\x0a**   * Redi\
stributions in b\
inary form must \
reproduce the ab\
ove copyright\x0d\x0a*\
*     notice, th\
is list of condi\
tions and the fo\
llowing disclaim\
er in\x0d\x0a**     th\
e documentation \
and/or other mat\
erials provided \
with the\x0d\x0a**    \
 distribution.\x0d\x0a\
**   * Neither t\
he name of The Q\
t Company Ltd no\
r the names of i\
ts\x0d\x0a**     contr\
ibutors may be u\
sed to endorse o\
r promote produc\
ts derived\x0d\x0a**  \
   from this sof\
tware without sp\
ecific prior wri\
tten permission.\
\x0d\x0a**\x0d\x0a**\x0d\x0a** THI\
S SOFTWARE IS PR\
OVIDED BY THE CO\
PYRIGHT HOLDERS \
AND CONTRIBUTORS\
\x0d\x0a** \x22AS IS\x22 AND\
 ANY EXPRESS OR \
IMPLIED WARRANTI\
ES, INCLUDING, B\
UT NOT\x0d\x0a** LIMIT\
ED TO, THE IMPLI\
ED WARRANTIES OF\
 MERCHANTABILITY\
 AND FITNESS FOR\
\x0d\x0a** A PARTICULA\
R PURPOSE ARE DI\
SCLAIMED. IN NO \
EVENT SHALL THE \
COPYRIGHT\x0d\x0a** OW\
NER OR CONTRIBUT\
ORS BE LIABLE FO\
R ANY DIRECT, IN\
DIRECT, INCIDENT\
AL,\x0d\x0a** SPECIAL,\
 EXEMPLARY, OR C\
ONSEQUENTIAL DAM\
AGES (INCLUDING,\
 BUT NOT\x0d\x0a** LIM\
ITED TO, PROCURE\
MENT OF SUBSTITU\
TE GOODS OR SERV\
ICES; LOSS OF US\
E,\x0d\x0a** DATA, OR \
PROFITS; OR BUSI\
NESS INTERRUPTIO\
N) HOWEVER CAUSE\
D AND ON ANY\x0d\x0a**\
 THEORY OF LIABI\
LITY, WHETHER IN\
 CONTRACT, STRIC\
T LIABILITY, OR \
TORT\x0d\x0a** (INCLUD\
ING NEGLIGENCE O\
R OTHERWISE) ARI\
SING IN ANY WAY \
OUT OF THE USE\x0d\x0a\
** OF THIS SOFTW\
ARE, EVEN IF ADV\
ISED OF THE POSS\
IBILITY OF SUCH \
DAMAGE.\x22\x0d\x0a**\x0d\x0a**\
 $QT_END_LICENSE\
$\x0d\x0a**\x0d\x0a*********\
****************\
****************\
****************\
****************\
***/\x0d\x0aimport QtG\
raphicalEffects \
1.0\x0d\x0a//import Qt\
GraphicalEffects\
 1.12\x0d\x0a\x0d\x0aGlow {\x0d\
\x0a    color: glow\
Color\x0d\x0a    sampl\
es: 20\x0d\x0a    spre\
ad: 0.3\x0d\x0a}\x0d\x0a\
\x00\x00\x86\x06\
/\
* DIGIT UI *****\
****************\
****************\
****************\
****************\
*******/\x0d\x0a\x0d\x0a//im\
port QtQuick 2.1\
2\x0d\x0a//import QtQu\
ick.Layouts 1.12\
\x0d\x0a//import QtQui\
ck.Controls 2.12\
\x0d\x0a//import QtQui\
ck.Controls.Imag\
ine 2.12\x0d\x0a//impo\
rt QtQuick.Windo\
w 2.0\x0d\x0aimport Qt\
Quick 2.9\x0d\x0aimpor\
t QtQuick.Layout\
s 1.3\x0d\x0aimport Qt\
Quick.Controls 2\
.3\x0d\x0aimport QtQui\
ck.Controls.Imag\
ine 2.3\x0d\x0aimport \
QtQuick.Window 2\
.0\x0d\x0a\x0d\x0aApplicatio\
nWindow {\x0d\x0a    i\
d: window\x0d\x0a    w\
idth: 800\x0d\x0a    h\
eight: 480\x0d\x0a    \
minimumWidth: 80\
0\x0d\x0a    minimumHe\
ight: 480\x0d\x0a    m\
aximumWidth: 800\
\x0d\x0a    maximumHei\
ght: 480\x0d\x0a    vi\
sible: true\x0d\x0a   \
 title: \x22Digit\x22\x0d\
\x0a\x0d\x0a    readonly \
property color c\
olorGlow: \x22#1d6d\
64\x22\x0d\x0a    readonl\
y property color\
 colorWarning: \x22\
#d5232f\x22\x0d\x0a    re\
adonly property \
color colorMain:\
 \x22#6affcd\x22\x0d\x0a    \
readonly propert\
y color colorBri\
ght: \x22#ffffff\x22\x0d\x0a\
    readonly pro\
perty color colo\
rLightGrey: \x22#88\
8\x22\x0d\x0a    readonly\
 property color \
colorDarkGrey: \x22\
#333\x22\x0d\x0a\x0d\x0a    rea\
donly property i\
nt fontSizeExtra\
Small: Qt.applic\
ation.font.pixel\
Size * 0.8\x0d\x0a    \
readonly propert\
y int fontSizeMe\
dium: Qt.applica\
tion.font.pixelS\
ize * 1.5\x0d\x0a    r\
eadonly property\
 int fontSizeLar\
ge: Qt.applicati\
on.font.pixelSiz\
e * 2\x0d\x0a    reado\
nly property int\
 fontSizeExtraLa\
rge: Qt.applicat\
ion.font.pixelSi\
ze * 5\x0d\x0a\x0d\x0a    //\
    Component.on\
Completed: {\x0d\x0a  \
  //        x = \
Screen.width / 2\
 - width / 2\x0d\x0a  \
  //        y = \
Screen.height / \
2 - height / 2\x0d\x0a\
    //    }\x0d\x0a\x0d\x0a \
   //    Shortcu\
t {\x0d\x0a    //     \
   sequence: \x22Ct\
rl+Q\x22\x0d\x0a    //   \
     onActivated\
: Qt.quit()\x0d\x0a   \
 //    }\x0d\x0a\x0d\x0a    \
StackLayout {\x0d\x0a \
       id: stack\
Layout\x0d\x0a        \
anchors.fill: pa\
rent\x0d\x0a        cu\
rrentIndex: bar.\
currentIndex\x0d\x0a\x0d\x0a\
        Frame {\x0d\
\x0a            id:\
 delayFrame\x0d\x0a   \
         Layout.\
fillWidth: true\x0d\
\x0a            z: \
-1\x0d\x0a            \
StackLayout {\x0d\x0a \
               i\
d: reverbStack1\x0d\
\x0a               \
 anchors.fill: p\
arent\x0d\x0a         \
       Frame {\x0d\x0a\
                \
    id: reverbFr\
ame3\x0d\x0a          \
          width:\
 800\x0d\x0a          \
          height\
: 480\x0d\x0a         \
           z: -1\
\x0d\x0a              \
      Column {\x0d\x0a\
                \
        id: colu\
mn2\x0d\x0a           \
             x: \
0\x0d\x0a             \
           y: 42\
\x0d\x0a              \
          width:\
 120\x0d\x0a          \
              he\
ight: 258\x0d\x0a     \
               }\
\x0d\x0a\x0d\x0a            \
        Column {\
\x0d\x0a              \
          id: co\
lumn3\x0d\x0a         \
               x\
: 650\x0d\x0a         \
               y\
: 58\x0d\x0a          \
              wi\
dth: 102\x0d\x0a      \
                \
  height: 271\x0d\x0a \
                \
       spacing: \
10\x0d\x0a            \
            Glow\
ingLabel {\x0d\x0a    \
                \
        color: \x22\
#ffffff\x22\x0d\x0a      \
                \
      text: qsTr\
(\x22TIME\x22)\x0d\x0a      \
                \
      font.pixel\
Size: fontSizeMe\
dium\x0d\x0a          \
              }\x0d\
\x0a\x0d\x0a             \
           Dial \
{\x0d\x0a             \
               i\
d: mixDial1\x0d\x0a   \
                \
         width: \
100\x0d\x0a           \
                \
 height: 100\x0d\x0a  \
                \
          Layout\
.preferredHeight\
: 128\x0d\x0a         \
                \
   Layout.alignm\
ent: Qt.AlignHCe\
nter\x0d\x0a          \
                \
  Label {\x0d\x0a     \
                \
           color\
: \x22#ffffff\x22\x0d\x0a   \
                \
             tex\
t: mixDial1.valu\
e.toFixed(0)\x0d\x0a  \
                \
              fo\
nt.pixelSize: Qt\
.application.fon\
t.pixelSize * 3\x0d\
\x0a               \
                \
 anchors.centerI\
n: parent\x0d\x0a     \
                \
       }\x0d\x0a      \
                \
      Layout.max\
imumHeight: 128\x0d\
\x0a               \
             val\
ue: 42\x0d\x0a        \
                \
    stepSize: 1\x0d\
\x0a               \
             to:\
 100\x0d\x0a          \
                \
  Layout.preferr\
edWidth: 128\x0d\x0a  \
                \
          from: \
0\x0d\x0a             \
               L\
ayout.maximumWid\
th: 128\x0d\x0a       \
                \
     Layout.mini\
mumHeight: 64\x0d\x0a \
                \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
                \
Layout.minimumWi\
dth: 64\x0d\x0a       \
                \
 }\x0d\x0a\x0d\x0a          \
              Gl\
owingLabel {\x0d\x0a  \
                \
          color:\
 \x22#ffffff\x22\x0d\x0a    \
                \
        text: \x22F\
EEDBACK\x22\x0d\x0a      \
                \
      font.pixel\
Size: fontSizeMe\
dium\x0d\x0a          \
              }\x0d\
\x0a\x0d\x0a             \
           Dial \
{\x0d\x0a             \
               i\
d: sizeDial1\x0d\x0a  \
                \
          width:\
 100\x0d\x0a          \
                \
  height: 100\x0d\x0a \
                \
           Layou\
t.preferredHeigh\
t: 128\x0d\x0a        \
                \
    Layout.align\
ment: Qt.AlignHC\
enter\x0d\x0a         \
                \
   onMoved: {\x0d\x0a \
                \
               k\
nobs.ui_knob_cha\
nge(\x22feedback\x22, \
sizeDial1.value)\
\x0d\x0a              \
              }\x0d\
\x0a               \
             val\
ue: 42\x0d\x0a        \
                \
    Layout.maxim\
umHeight: 128\x0d\x0a \
                \
           Layou\
t.preferredWidth\
: 128\x0d\x0a         \
                \
   stepSize: 1\x0d\x0a\
                \
            to: \
100\x0d\x0a           \
                \
 from: 0\x0d\x0a      \
                \
      Layout.max\
imumWidth: 128\x0d\x0a\
                \
            Layo\
ut.minimumHeight\
: 64\x0d\x0a          \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
                \
       Layout.mi\
nimumWidth: 64\x0d\x0a\
\x0d\x0a              \
              La\
bel {\x0d\x0a         \
                \
       x: 33\x0d\x0a  \
                \
              y:\
 8\x0d\x0a            \
                \
    color: \x22#fff\
fff\x22\x0d\x0a          \
                \
      text: size\
Dial1.value.toFi\
xed(0)\x0d\x0a\x0d\x0a      \
                \
          font.p\
ixelSize: Qt.app\
lication.font.pi\
xelSize * 3\x0d\x0a   \
                \
             anc\
hors.centerIn: p\
arent\x0d\x0a         \
                \
   }\x0d\x0a          \
              }\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a         \
           }\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
\x0d\x0a            Ta\
bBar {\x0d\x0a        \
        id: reve\
rbTabs1\x0d\x0a       \
         width: \
376\x0d\x0a           \
     height: 38\x0d\
\x0a               \
 anchors.bottom:\
 parent.bottom\x0d\x0a\
                \
TabButton {\x0d\x0a   \
                \
 id: tabButton7\x0d\
\x0a               \
     text: qsTr(\
\x22Main\x22)\x0d\x0a       \
         }\x0d\x0a\x0d\x0a  \
              Ta\
bButton {\x0d\x0a     \
               i\
d: tabButton8\x0d\x0a \
                \
   text: qsTr(\x22E\
ffects\x22)\x0d\x0a      \
          }\x0d\x0a\x0d\x0a \
               T\
abButton {\x0d\x0a    \
                \
id: tabButton9\x0d\x0a\
                \
    text: qsTr(\x22\
Bus\x22)\x0d\x0a         \
       }\x0d\x0a      \
          anchor\
s.bottomMargin: \
0\x0d\x0a            }\
\x0d\x0a\x0d\x0a            \
ProgressBar {\x0d\x0a \
               i\
d: leftEncoderVa\
l1\x0d\x0a            \
    x: -12\x0d\x0a    \
            y: -\
12\x0d\x0a            \
    width: 93\x0d\x0a \
               h\
eight: 41\x0d\x0a     \
           Glowi\
ngLabel {\x0d\x0a     \
               w\
idth: 93\x0d\x0a      \
              he\
ight: 41\x0d\x0a      \
              co\
lor: \x22#ffffff\x22\x0d\x0a\
                \
    text: qsTr(\x22\
SIZE\x22)\x0d\x0a        \
            font\
.pixelSize: font\
SizeMedium\x0d\x0a    \
            }\x0d\x0a \
               v\
alue: 0.5\x0d\x0a     \
       }\x0d\x0a      \
      Layout.fil\
lHeight: true\x0d\x0a \
       }\x0d\x0a\x0d\x0a    \
    Frame {\x0d\x0a   \
         id: rev\
erbFrame1\x0d\x0a     \
       Layout.fi\
llWidth: true\x0d\x0a \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
z: -1\x0d\x0a\x0d\x0a       \
     StackLayout\
 {\x0d\x0a            \
    id: reverbSt\
ack\x0d\x0a           \
     anchors.fil\
l: parent\x0d\x0a\x0d\x0a\x0d\x0a \
               F\
rame {\x0d\x0a        \
            id: \
reverbFrame\x0d\x0a   \
                \
 width: 800\x0d\x0a   \
                \
 height: 480\x0d\x0a  \
                \
  z: -1\x0d\x0a\x0d\x0a     \
               C\
olumn {\x0d\x0a       \
                \
 id: column\x0d\x0a   \
                \
     x: -12\x0d\x0a   \
                \
     y: 168\x0d\x0a   \
                \
     width: 120\x0d\
\x0a               \
         height:\
 258\x0d\x0a\x0d\x0a        \
                \
GlowingLabel {\x0d\x0a\
                \
            colo\
r: \x22#ffffff\x22\x0d\x0a  \
                \
          text: \
qsTr(\x22SIZE\x22)\x0d\x0a  \
                \
          font.p\
ixelSize: fontSi\
zeMedium\x0d\x0a      \
                \
  }\x0d\x0a\x0d\x0a         \
               D\
ial {\x0d\x0a         \
                \
   id: sizeDial\x0d\
\x0a               \
             wid\
th: 100\x0d\x0a       \
                \
     height: 100\
\x0d\x0a              \
              fr\
om: 0\x0d\x0a         \
                \
   value: 42\x0d\x0a  \
                \
          Layout\
.minimumHeight: \
64\x0d\x0a            \
                \
Layout.preferred\
Width: 128\x0d\x0a    \
                \
        Layout.m\
inimumWidth: 64\x0d\
\x0a               \
             ste\
pSize: 1\x0d\x0a      \
                \
      Layout.pre\
ferredHeight: 12\
8\x0d\x0a             \
               L\
ayout.fillHeight\
: true\x0d\x0a        \
                \
    Layout.align\
ment: Qt.AlignHC\
enter\x0d\x0a         \
                \
   to: 100\x0d\x0a    \
                \
        Layout.m\
aximumWidth: 128\
\x0d\x0a              \
              La\
yout.maximumHeig\
ht: 128\x0d\x0a       \
                \
     Label {\x0d\x0a  \
                \
              co\
lor: \x22#ffffff\x22\x0d\x0a\
                \
                \
text: sizeDial.v\
alue.toFixed(0)\x0d\
\x0a               \
                \
 font.pixelSize:\
 Qt.application.\
font.pixelSize *\
 3\x0d\x0a            \
                \
    anchors.cent\
erIn: parent\x0d\x0a  \
                \
          }\x0d\x0a   \
                \
     }\x0d\x0a        \
            }\x0d\x0a\x0d\
\x0a\x0d\x0a             \
       ColumnLay\
out {\x0d\x0a         \
               x\
: 191\x0d\x0a         \
               y\
: 66\x0d\x0a          \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
               L\
ayout.fillWidth:\
 true\x0d\x0a\x0d\x0a       \
                \
 Image {\x0d\x0a      \
                \
      x: 0\x0d\x0a    \
                \
        Layout.f\
illHeight: false\
\x0d\x0a              \
              so\
urce: \x22qrc:/icon\
s/reverb_cube.pn\
g\x22\x0d\x0a            \
                \
fillMode: Image.\
PreserveAspectFi\
t\x0d\x0a             \
           }\x0d\x0a  \
                \
      Layout.pre\
ferredWidth: 350\
\x0d\x0a              \
      }\x0d\x0a\x0d\x0a\x0d\x0a   \
                \
 Column {\x0d\x0a     \
                \
   id: column1\x0d\x0a\
                \
        x: 662\x0d\x0a\
                \
        y: 168\x0d\x0a\
                \
        width: 1\
02\x0d\x0a            \
            heig\
ht: 271\x0d\x0a       \
                \
 GlowingLabel {\x0d\
\x0a               \
             col\
or: \x22#ffffff\x22\x0d\x0a \
                \
           text:\
 qsTr(\x22MIX\x22)\x0d\x0a  \
                \
          font.p\
ixelSize: fontSi\
zeMedium\x0d\x0a      \
                \
  }\x0d\x0a\x0d\x0a         \
               D\
ial {\x0d\x0a         \
                \
   id: mixDial\x0d\x0a\
                \
            widt\
h: 100\x0d\x0a        \
                \
    height: 100\x0d\
\x0a               \
             ste\
pSize: 1\x0d\x0a      \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
           from:\
 0\x0d\x0a            \
                \
Layout.maximumHe\
ight: 128\x0d\x0a     \
                \
       Layout.pr\
eferredHeight: 1\
28\x0d\x0a            \
                \
to: 100\x0d\x0a       \
                \
     Label {\x0d\x0a  \
                \
              co\
lor: \x22#ffffff\x22\x0d\x0a\
                \
                \
text: mixDial.va\
lue.toFixed(0)\x0d\x0a\
                \
                \
font.pixelSize: \
Qt.application.f\
ont.pixelSize * \
3\x0d\x0a             \
                \
   anchors.cente\
rIn: parent\x0d\x0a   \
                \
         }\x0d\x0a    \
                \
        Layout.m\
inimumWidth: 64\x0d\
\x0a               \
             Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
                \
            valu\
e: 42\x0d\x0a         \
                \
   Layout.minimu\
mHeight: 64\x0d\x0a   \
                \
         Layout.\
maximumWidth: 12\
8\x0d\x0a             \
               L\
ayout.preferredW\
idth: 128\x0d\x0a     \
                \
   }\x0d\x0a          \
          }\x0d\x0a   \
             }\x0d\x0a\
            }\x0d\x0a\x0d\
\x0a            Tab\
Bar {\x0d\x0a         \
       id: rever\
bTabs\x0d\x0a         \
       width: 37\
6\x0d\x0a             \
   height: 38\x0d\x0a \
               a\
nchors.bottom: p\
arent.bottom\x0d\x0a  \
              an\
chors.bottomMarg\
in: 0\x0d\x0a         \
       TabButton\
 {\x0d\x0a            \
        id: tabB\
utton4\x0d\x0a        \
            text\
: qsTr(\x22Main\x22)\x0d\x0a\
                \
}\x0d\x0a\x0d\x0a           \
     TabButton {\
\x0d\x0a              \
      id: tabBut\
ton5\x0d\x0a          \
          text: \
qsTr(\x22Effects\x22)\x0d\
\x0a               \
 }\x0d\x0a\x0d\x0a          \
      TabButton \
{\x0d\x0a             \
       id: tabBu\
tton6\x0d\x0a         \
           text:\
 qsTr(\x22Bus\x22)\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
\x0d\x0a            Pr\
ogressBar {\x0d\x0a   \
             id:\
 leftEncoderVal\x0d\
\x0a               \
 x: -12\x0d\x0a       \
         y: -12\x0d\
\x0a               \
 width: 93\x0d\x0a    \
            heig\
ht: 41\x0d\x0a        \
        value: 0\
.5\x0d\x0a\x0d\x0a          \
      GlowingLab\
el {\x0d\x0a          \
          width:\
 93\x0d\x0a           \
         height:\
 41\x0d\x0a           \
         color: \
\x22#ffffff\x22\x0d\x0a     \
               t\
ext: qsTr(\x22SIZE\x22\
)\x0d\x0a             \
       font.pixe\
lSize: fontSizeM\
edium\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a\x0d\x0a        Fr\
ame {\x0d\x0a         \
   id: frame\x0d\x0a  \
          width:\
 800\x0d\x0a          \
  height: 480\x0d\x0a \
           ancho\
rs.rightMargin: \
0\x0d\x0a            a\
nchors.bottomMar\
gin: 0\x0d\x0a        \
    anchors.left\
Margin: 0\x0d\x0a     \
       anchors.t\
opMargin: 0\x0d\x0a   \
         content\
Height: 480\x0d\x0a   \
         content\
Width: 800\x0d\x0a\x0d\x0a\x0d\x0a\
            RowL\
ayout {\x0d\x0a       \
         id: mai\
nRowLayout\x0d\x0a    \
            widt\
h: 800\x0d\x0a        \
        height: \
480\x0d\x0a           \
     anchors.fil\
l: parent\x0d\x0a     \
           ancho\
rs.margins: 24\x0d\x0a\
                \
spacing: 36\x0d\x0a\x0d\x0a \
               C\
ontainer {\x0d\x0a    \
                \
id: leftTabBar\x0d\x0a\
\x0d\x0a              \
      currentInd\
ex: 1\x0d\x0a\x0d\x0a       \
             Lay\
out.fillWidth: f\
alse\x0d\x0a          \
          Layout\
.fillHeight: tru\
e\x0d\x0a\x0d\x0a           \
         ButtonG\
roup {\x0d\x0a        \
                \
buttons: columnL\
ayout.children\x0d\x0a\
                \
    }\x0d\x0a\x0d\x0a       \
             con\
tentItem: Column\
Layout {\x0d\x0a      \
                \
  id: columnLayo\
ut\x0d\x0a            \
            spac\
ing: 3\x0d\x0a\x0d\x0a      \
                \
  Repeater {\x0d\x0a  \
                \
          model:\
 leftTabBar.cont\
entModel\x0d\x0a      \
                \
  }\x0d\x0a           \
         }\x0d\x0a\x0d\x0a  \
                \
  FeatureButton \
{\x0d\x0a             \
           id: n\
avigationFeature\
Button\x0d\x0a        \
                \
text: qsTr(\x22Navi\
gation\x22)\x0d\x0a      \
                \
  icon.name: \x22na\
vigation\x22\x0d\x0a     \
                \
   Layout.fillHe\
ight: true\x0d\x0a    \
                \
}\x0d\x0a\x0d\x0a           \
         Feature\
Button {\x0d\x0a      \
                \
  text: qsTr(\x22Mu\
sic\x22)\x0d\x0a         \
               i\
con.name: \x22music\
\x22\x0d\x0a             \
           check\
ed: true\x0d\x0a      \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
               }\
\x0d\x0a\x0d\x0a            \
        FeatureB\
utton {\x0d\x0a       \
                \
 text: qsTr(\x22Mes\
sage\x22)\x0d\x0a        \
                \
icon.name: \x22mess\
age\x22\x0d\x0a          \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
           }\x0d\x0a\x0d\x0a\
                \
    FeatureButto\
n {\x0d\x0a           \
             tex\
t: qsTr(\x22Command\
\x22)\x0d\x0a            \
            icon\
.name: \x22command\x22\
\x0d\x0a              \
          Layout\
.fillHeight: tru\
e\x0d\x0a             \
       }\x0d\x0a\x0d\x0a    \
                \
FeatureButton {\x0d\
\x0a               \
         text: q\
sTr(\x22Settings\x22)\x0d\
\x0a               \
         font.fa\
mily: \x22Times New\
 Roman\x22\x0d\x0a       \
                \
 icon.name: \x22set\
tings\x22\x0d\x0a        \
                \
Layout.fillHeigh\
t: true\x0d\x0a       \
             }\x0d\x0a\
                \
}\x0d\x0a\x0d\x0a           \
     StackLayout\
 {\x0d\x0a            \
        currentI\
ndex: leftTabBar\
.currentIndex\x0d\x0a\x0d\
\x0a               \
     Layout.pref\
erredWidth: 150\x0d\
\x0a               \
     Layout.maxi\
mumWidth: 150\x0d\x0a \
                \
   Layout.fillWi\
dth: false\x0d\x0a\x0d\x0a  \
                \
  Item {}\x0d\x0a\x0d\x0a   \
                \
 ColumnLayout {\x0d\
\x0a               \
         spacing\
: 16\x0d\x0a\x0d\x0a        \
                \
ButtonGroup {\x0d\x0a \
                \
           id: v\
iewButtonGroup\x0d\x0a\
                \
            butt\
ons: viewTypeRow\
Layout.children\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
      RowLayout \
{\x0d\x0a             \
               i\
d: viewTypeRowLa\
yout\x0d\x0a          \
                \
  spacing: 3\x0d\x0a\x0d\x0a\
                \
            Layo\
ut.bottomMargin:\
 12\x0d\x0a\x0d\x0a         \
                \
   Button {\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Compact\
\x22)\x0d\x0a            \
                \
    font.pixelSi\
ze: fontSizeExtr\
aSmall\x0d\x0a        \
                \
        checked:\
 true\x0d\x0a\x0d\x0a       \
                \
         Layout.\
fillWidth: true\x0d\
\x0a               \
             }\x0d\x0a\
                \
            Butt\
on {\x0d\x0a          \
                \
      text: qsTr\
(\x22Full\x22)\x0d\x0a      \
                \
          font.p\
ixelSize: fontSi\
zeExtraSmall\x0d\x0a  \
                \
              ch\
eckable: true\x0d\x0a\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
     }\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a           \
             Glo\
wingLabel {\x0d\x0a   \
                \
         text: q\
sTr(\x22VOLUME\x22)\x0d\x0a \
                \
           color\
: \x22white\x22\x0d\x0a     \
                \
       font.pixe\
lSize: fontSizeM\
edium\x0d\x0a         \
               }\
\x0d\x0a\x0d\x0a            \
            Dial\
 {\x0d\x0a            \
                \
id: volumeDial\x0d\x0a\
                \
            from\
: 0\x0d\x0a           \
                \
 value: 42\x0d\x0a    \
                \
        to: 100\x0d\
\x0a               \
             ste\
pSize: 1\x0d\x0a\x0d\x0a    \
                \
        Layout.a\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
                \
       Layout.mi\
nimumWidth: 64\x0d\x0a\
                \
            Layo\
ut.minimumHeight\
: 64\x0d\x0a          \
                \
  Layout.preferr\
edWidth: 128\x0d\x0a  \
                \
          Layout\
.preferredHeight\
: 128\x0d\x0a         \
                \
   Layout.maximu\
mWidth: 128\x0d\x0a   \
                \
         Layout.\
maximumHeight: 1\
28\x0d\x0a            \
                \
Layout.fillHeigh\
t: true\x0d\x0a\x0d\x0a     \
                \
       Label {\x0d\x0a\
                \
                \
text: volumeDial\
.value.toFixed(0\
)\x0d\x0a             \
                \
   color: \x22white\
\x22\x0d\x0a             \
                \
   font.pixelSiz\
e: Qt.applicatio\
n.font.pixelSize\
 * 3\x0d\x0a          \
                \
      anchors.ce\
nterIn: parent\x0d\x0a\
                \
            }\x0d\x0a \
                \
       }\x0d\x0a\x0d\x0a    \
                \
    ButtonGroup \
{\x0d\x0a             \
               i\
d: audioSourceBu\
ttonGroup\x0d\x0a     \
                \
   }\x0d\x0a\x0d\x0a        \
                \
RowLayout {\x0d\x0a   \
                \
         Layout.\
topMargin: 16\x0d\x0a\x0d\
\x0a               \
             Glo\
wingLabel {\x0d\x0a   \
                \
             id:\
 radioOption\x0d\x0a  \
                \
              te\
xt: qsTr(\x22RADIO\x22\
)\x0d\x0a             \
                \
   color: \x22white\
\x22\x0d\x0a             \
                \
   font.pixelSiz\
e: fontSizeMediu\
m\x0d\x0a             \
                \
   horizontalAli\
gnment: Label.Al\
ignLeft\x0d\x0a\x0d\x0a     \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
               }\
\x0d\x0a              \
              Gl\
owingLabel {\x0d\x0a  \
                \
              te\
xt: qsTr(\x22AUX\x22)\x0d\
\x0a               \
                \
 color: colorLig\
htGrey\x0d\x0a        \
                \
        font.pix\
elSize: fontSize\
Medium * 0.8\x0d\x0a  \
                \
              ho\
rizontalAlignmen\
t: Label.AlignHC\
enter\x0d\x0a         \
                \
       glowEnabl\
ed: false\x0d\x0a\x0d\x0a   \
                \
             Lay\
out.alignment: Q\
t.AlignBottom\x0d\x0a \
                \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
                \
   }\x0d\x0a          \
                \
  GlowingLabel {\
\x0d\x0a              \
                \
  text: qsTr(\x22MP\
3\x22)\x0d\x0a           \
                \
     color: colo\
rDarkGrey\x0d\x0a     \
                \
           font.\
pixelSize: fontS\
izeMedium * 0.6\x0d\
\x0a               \
                \
 horizontalAlign\
ment: Label.Alig\
nRight\x0d\x0a        \
                \
        glowEnab\
led: false\x0d\x0a\x0d\x0a  \
                \
              La\
yout.alignment: \
Qt.AlignBottom\x0d\x0a\
                \
                \
Layout.fillWidth\
: true\x0d\x0a        \
                \
    }\x0d\x0a         \
               }\
\x0d\x0a\x0d\x0a            \
            Fram\
e {\x0d\x0a           \
                \
 id: stationFram\
e\x0d\x0a             \
               l\
eftPadding: 1\x0d\x0a \
                \
           right\
Padding: 1\x0d\x0a    \
                \
        topPaddi\
ng: 1\x0d\x0a         \
                \
   bottomPadding\
: 1\x0d\x0a\x0d\x0a         \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
            Layo\
ut.preferredHeig\
ht: 128\x0d\x0a\x0d\x0a     \
                \
       ListView \
{\x0d\x0a             \
                \
   clip: true\x0d\x0a \
                \
               a\
nchors.fill: par\
ent\x0d\x0a\x0d\x0a         \
                \
       ScrollInd\
icator.vertical:\
 ScrollIndicator\
 {\x0d\x0a            \
                \
        parent: \
stationFrame\x0d\x0a  \
                \
                \
  anchors.top: p\
arent.top\x0d\x0a     \
                \
               a\
nchors.right: pa\
rent.right\x0d\x0a    \
                \
                \
anchors.rightMar\
gin: 1\x0d\x0a        \
                \
            anch\
ors.bottom: pare\
nt.bottom\x0d\x0a     \
                \
           }\x0d\x0a\x0d\x0a\
                \
                \
model: ListModel\
 {\x0d\x0a            \
                \
        ListElem\
ent { name: \x22V-R\
adio\x22; frequency\
: \x22105.5 MHz\x22 }\x0d\
\x0a               \
                \
     ListElement\
 { name: \x22World \
News\x22; frequency\
: \x2293.4 MHz\x22 }\x0d\x0a\
                \
                \
    ListElement \
{ name: \x22TekStep\
 FM\x22; frequency:\
 \x2295.0 MHz\x22 }\x0d\x0a \
                \
                \
   ListElement {\
 name: \x22Classic \
Radio\x22; frequenc\
y: \x2289.9 MHz\x22 }\x0d\
\x0a               \
                \
     ListElement\
 { name: \x22Buena \
Vista FM\x22; frequ\
ency: \x22100.8 MHz\
\x22 }\x0d\x0a           \
                \
         ListEle\
ment { name: \x22Dr\
ive-by Radio\x22; f\
requency: \x2299.1 \
MHz\x22 }\x0d\x0a        \
                \
            List\
Element { name: \
\x22Unknown #1\x22; fr\
equency: \x22104.5 \
MHz\x22 }\x0d\x0a        \
                \
            List\
Element { name: \
\x22Unknown #2\x22; fr\
equency: \x2291.2 M\
Hz\x22 }\x0d\x0a         \
                \
           ListE\
lement { name: \x22\
Unknown #3\x22; fre\
quency: \x2293.8 MH\
z\x22 }\x0d\x0a          \
                \
          ListEl\
ement { name: \x22U\
nknown #4\x22; freq\
uency: \x2280.4 MHz\
\x22 }\x0d\x0a           \
                \
         ListEle\
ment { name: \x22Un\
known #5\x22; frequ\
ency: \x22101.1 MHz\
\x22 }\x0d\x0a           \
                \
         ListEle\
ment { name: \x22Un\
known #6\x22; frequ\
ency: \x2292.2 MHz\x22\
 }\x0d\x0a            \
                \
    }\x0d\x0a         \
                \
       delegate:\
 ItemDelegate {\x0d\
\x0a               \
                \
     id: station\
Delegate\x0d\x0a      \
                \
              wi\
dth: parent.widt\
h\x0d\x0a             \
                \
       height: 2\
2\x0d\x0a             \
                \
       text: mod\
el.name\x0d\x0a       \
                \
             fon\
t.pixelSize: fon\
tSizeExtraSmall\x0d\
\x0a               \
                \
     topPadding:\
 0\x0d\x0a            \
                \
        bottomPa\
dding: 0\x0d\x0a\x0d\x0a    \
                \
                \
contentItem: Row\
Layout {\x0d\x0a      \
                \
                \
  Label {\x0d\x0a     \
                \
                \
       text: mod\
el.name\x0d\x0a       \
                \
                \
     font: stati\
onDelegate.font\x0d\
\x0a               \
                \
             hor\
izontalAlignment\
: Text.AlignLeft\
\x0d\x0a              \
                \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
              }\x0d\
\x0a               \
                \
         Label {\
\x0d\x0a              \
                \
              te\
xt: model.freque\
ncy\x0d\x0a           \
                \
                \
 font: stationDe\
legate.font\x0d\x0a   \
                \
                \
         horizon\
talAlignment: Te\
xt.AlignRight\x0d\x0a \
                \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
                \
           }\x0d\x0a  \
                \
                \
  }\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
    }\x0d\x0a         \
               }\
\x0d\x0a\x0d\x0a            \
            Fram\
e {\x0d\x0a           \
                \
 Layout.fillWidt\
h: true\x0d\x0a\x0d\x0a     \
                \
       RowLayout\
 {\x0d\x0a            \
                \
    anchors.fill\
: parent\x0d\x0a\x0d\x0a    \
                \
            Labe\
l {\x0d\x0a           \
                \
         text: q\
sTr(\x22Sort by\x22)\x0d\x0a\
                \
                \
    font.pixelSi\
ze: fontSizeExtr\
aSmall\x0d\x0a\x0d\x0a      \
                \
              La\
yout.alignment: \
Qt.AlignTop\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
                \
  ColumnLayout {\
\x0d\x0a              \
                \
      RadioButto\
n {\x0d\x0a           \
                \
             tex\
t: qsTr(\x22Name\x22)\x0d\
\x0a               \
                \
         font.pi\
xelSize: fontSiz\
eExtraSmall\x0d\x0a   \
                \
                \
 }\x0d\x0a            \
                \
        RadioBut\
ton {\x0d\x0a         \
                \
               t\
ext: qsTr(\x22Frequ\
ency\x22)\x0d\x0a        \
                \
                \
font.pixelSize: \
fontSizeExtraSma\
ll\x0d\x0a            \
                \
        }\x0d\x0a     \
                \
               R\
adioButton {\x0d\x0a  \
                \
                \
      text: qsTr\
(\x22Favourites\x22)\x0d\x0a\
                \
                \
        font.pix\
elSize: fontSize\
ExtraSmall\x0d\x0a    \
                \
                \
    checked: tru\
e\x0d\x0a             \
                \
       }\x0d\x0a      \
                \
          }\x0d\x0a   \
                \
         }\x0d\x0a    \
                \
    }\x0d\x0a         \
           }\x0d\x0a  \
              }\x0d\
\x0a\x0d\x0a             \
   Rectangle {\x0d\x0a\
                \
    color: color\
Main\x0d\x0a          \
          implic\
itWidth: 1\x0d\x0a    \
                \
Layout.fillHeigh\
t: true\x0d\x0a       \
         }\x0d\x0a\x0d\x0a  \
              Co\
lumnLayout {\x0d\x0a  \
                \
  Layout.preferr\
edWidth: 350\x0d\x0a  \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
              La\
yout.fillHeight:\
 true\x0d\x0a\x0d\x0a       \
             Glo\
wingLabel {\x0d\x0a   \
                \
     id: timeLab\
el\x0d\x0a            \
            text\
: qsTr(\x2211:02\x22)\x0d\
\x0a               \
         font.pi\
xelSize: fontSiz\
eExtraLarge\x0d\x0a\x0d\x0a \
                \
       Layout.al\
ignment: Qt.Alig\
nHCenter\x0d\x0a\x0d\x0a    \
                \
    GlowingLabel\
 {\x0d\x0a            \
                \
text: qsTr(\x22AM\x22)\
\x0d\x0a              \
              fo\
nt.pixelSize: fo\
ntSizeLarge\x0d\x0a   \
                \
         anchors\
.left: parent.ri\
ght\x0d\x0a           \
                \
 anchors.leftMar\
gin: 8\x0d\x0a        \
                \
}\x0d\x0a             \
       }\x0d\x0a\x0d\x0a    \
                \
Label {\x0d\x0a       \
                \
 text: qsTr(\x2201/\
01/2018\x22)\x0d\x0a     \
                \
   color: colorL\
ightGrey\x0d\x0a      \
                \
  font.pixelSize\
: fontSizeMedium\
\x0d\x0a\x0d\x0a            \
            Layo\
ut.alignment: Qt\
.AlignHCenter\x0d\x0a \
                \
       Layout.to\
pMargin: 2\x0d\x0a    \
                \
    Layout.botto\
mMargin: 10\x0d\x0a   \
                \
 }\x0d\x0a\x0d\x0a          \
          Image \
{\x0d\x0a             \
           sourc\
e: \x22qrc:/icons/c\
ar.png\x22\x0d\x0a       \
                \
 fillMode: Image\
.PreserveAspectF\
it\x0d\x0a\x0d\x0a          \
              La\
yout.fillHeight:\
 true\x0d\x0a\x0d\x0a       \
                \
 Column {\x0d\x0a     \
                \
       x: parent\
.width * 0.88\x0d\x0a \
                \
           y: pa\
rent.height * 0.\
56\x0d\x0a            \
                \
spacing: 3\x0d\x0a\x0d\x0a  \
                \
          Image \
{\x0d\x0a             \
                \
   source: \x22qrc:\
/icons/warning.p\
ng\x22\x0d\x0a           \
                \
     anchors.hor\
izontalCenter: p\
arent.horizontal\
Center\x0d\x0a\x0d\x0a      \
                \
          layer.\
enabled: true\x0d\x0a \
                \
               l\
ayer.effect: Cus\
tomGlow {\x0d\x0a     \
                \
               s\
pread: 0.2\x0d\x0a    \
                \
                \
samples: 40\x0d\x0a   \
                \
                \
 color: colorWar\
ning\x0d\x0a          \
                \
      }\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      GlowingLab\
el {\x0d\x0a          \
                \
      text: qsTr\
(\x22Door open\x22)\x0d\x0a \
                \
               c\
olor: colorWarni\
ng\x0d\x0a            \
                \
    glowColor: Q\
t.rgba(colorWarn\
ing.r, colorWarn\
ing.g, colorWarn\
ing.b, 0.4)\x0d\x0a   \
                \
         }\x0d\x0a    \
                \
    }\x0d\x0a         \
           }\x0d\x0a  \
              }\x0d\
\x0a\x0d\x0a             \
   Rectangle {\x0d\x0a\
                \
    color: color\
Main\x0d\x0a          \
          implic\
itWidth: 1\x0d\x0a    \
                \
Layout.fillHeigh\
t: true\x0d\x0a       \
         }\x0d\x0a\x0d\x0a  \
              Co\
lumnLayout {\x0d\x0a  \
                \
  Row {\x0d\x0a       \
                \
 spacing: 8\x0d\x0a\x0d\x0a \
                \
       Image {\x0d\x0a\
                \
            sour\
ce: \x22qrc:/icons/\
weather.png\x22\x0d\x0a  \
                \
      }\x0d\x0a\x0d\x0a     \
                \
   Column {\x0d\x0a   \
                \
         spacing\
: 8\x0d\x0a\x0d\x0a         \
                \
   Row {\x0d\x0a      \
                \
          anchor\
s.horizontalCent\
er: parent.horiz\
ontalCenter\x0d\x0a\x0d\x0a \
                \
               G\
lowingLabel {\x0d\x0a \
                \
                \
   id: outsideTe\
mpValueLabel\x0d\x0a  \
                \
                \
  text: qsTr(\x2231\
\x22)\x0d\x0a            \
                \
        font.pix\
elSize: fontSize\
ExtraLarge\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 GlowingLabel {\x0d\
\x0a               \
                \
     text: qsTr(\
\x22\xc2\xb0C\x22)\x0d\x0a        \
                \
            font\
.pixelSize: Qt.a\
pplication.font.\
pixelSize * 2.5\x0d\
\x0a               \
                \
     anchors.bas\
eline: outsideTe\
mpValueLabel.bas\
eline\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Label {\x0d\x0a\
                \
                \
text: qsTr(\x22Osak\
a, Japan\x22)\x0d\x0a    \
                \
            colo\
r: colorLightGre\
y\x0d\x0a             \
                \
   font.pixelSiz\
e: fontSizeMediu\
m\x0d\x0a             \
               }\
\x0d\x0a              \
          }\x0d\x0a   \
                \
 }\x0d\x0a\x0d\x0a          \
          Column\
Layout {\x0d\x0a      \
                \
  id: airConRowL\
ayout\x0d\x0a         \
               s\
pacing: 8\x0d\x0a\x0d\x0a   \
                \
     Layout.pref\
erredWidth: 128\x0d\
\x0a               \
         Layout.\
preferredHeight:\
 380\x0d\x0a          \
              La\
yout.fillHeight:\
 true\x0d\x0a\x0d\x0a       \
                \
 Item {\x0d\x0a       \
                \
     Layout.fill\
Height: true\x0d\x0a  \
                \
      }\x0d\x0a\x0d\x0a     \
                \
   SwitchDelegat\
e {\x0d\x0a           \
                \
 text: qsTr(\x22AC\x22\
)\x0d\x0a             \
               l\
eftPadding: 0\x0d\x0a \
                \
           right\
Padding: 0\x0d\x0a    \
                \
        topPaddi\
ng: 0\x0d\x0a         \
                \
   bottomPadding\
: 0\x0d\x0a\x0d\x0a         \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
   }\x0d\x0a\x0d\x0a        \
                \
// QTBUG-63269\x0d\x0a\
                \
        Item {\x0d\x0a\
                \
            impl\
icitHeight: temp\
eratureValueLabe\
l.implicitHeight\
\x0d\x0a              \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
  Layout.topMarg\
in: 16\x0d\x0a\x0d\x0a      \
                \
      Label {\x0d\x0a \
                \
               t\
ext: qsTr(\x22Tempe\
rature\x22)\x0d\x0a      \
                \
          anchor\
s.baseline: temp\
eratureValueLabe\
l.bottom\x0d\x0a      \
                \
          anchor\
s.left: parent.l\
eft\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  GlowingLabel {\
\x0d\x0a              \
                \
  id: temperatur\
eValueLabel\x0d\x0a   \
                \
             tex\
t: qsTr(\x2224\xc2\xb0C\x22)\
\x0d\x0a              \
                \
  font.pixelSize\
: fontSizeLarge\x0d\
\x0a               \
                \
 anchors.right: \
parent.right\x0d\x0a  \
                \
          }\x0d\x0a   \
                \
     }\x0d\x0a\x0d\x0a      \
                \
  Slider {\x0d\x0a    \
                \
        value: 0\
.35\x0d\x0a           \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
 }\x0d\x0a\x0d\x0a          \
              //\
 QTBUG-63269\x0d\x0a  \
                \
      Item {\x0d\x0a  \
                \
          implic\
itHeight: powerV\
alueLabel.implic\
itHeight\x0d\x0a      \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
          Layout\
.topMargin: 16\x0d\x0a\
\x0d\x0a              \
              La\
bel {\x0d\x0a         \
                \
       text: qsT\
r(\x22Power\x22)\x0d\x0a    \
                \
            anch\
ors.baseline: po\
werValueLabel.bo\
ttom\x0d\x0a          \
                \
      anchors.le\
ft: parent.left\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Gl\
owingLabel {\x0d\x0a  \
                \
              id\
: powerValueLabe\
l\x0d\x0a             \
                \
   text: qsTr(\x221\
0%\x22)\x0d\x0a          \
                \
      font.pixel\
Size: fontSizeLa\
rge\x0d\x0a           \
                \
     anchors.rig\
ht: parent.right\
\x0d\x0a              \
              }\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
      Slider {\x0d\x0a\
                \
            valu\
e: 0.25\x0d\x0a       \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
     }\x0d\x0a\x0d\x0a      \
                \
  SwitchDelegate\
 {\x0d\x0a            \
                \
text: qsTr(\x22Low\x22\
)\x0d\x0a             \
               l\
eftPadding: 0\x0d\x0a \
                \
           right\
Padding: 0\x0d\x0a    \
                \
        topPaddi\
ng: 0\x0d\x0a         \
                \
   bottomPadding\
: 0\x0d\x0a\x0d\x0a         \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
       Layout.to\
pMargin: 16\x0d\x0a   \
                \
     }\x0d\x0a\x0d\x0a      \
                \
  SwitchDelegate\
 {\x0d\x0a            \
                \
text: qsTr(\x22High\
\x22)\x0d\x0a            \
                \
checked: true\x0d\x0a \
                \
           leftP\
adding: 0\x0d\x0a     \
                \
       rightPadd\
ing: 0\x0d\x0a        \
                \
    topPadding: \
0\x0d\x0a             \
               b\
ottomPadding: 0\x0d\
\x0a\x0d\x0a             \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
               }\
\x0d\x0a\x0d\x0a            \
            Swit\
chDelegate {\x0d\x0a  \
                \
          text: \
qsTr(\x22Defog\x22)\x0d\x0a \
                \
           leftP\
adding: 0\x0d\x0a     \
                \
       rightPadd\
ing: 0\x0d\x0a        \
                \
    topPadding: \
0\x0d\x0a             \
               b\
ottomPadding: 0\x0d\
\x0a\x0d\x0a             \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
               }\
\x0d\x0a\x0d\x0a            \
            Swit\
chDelegate {\x0d\x0a  \
                \
          text: \
qsTr(\x22Recirculat\
e\x22)\x0d\x0a           \
                \
 leftPadding: 0\x0d\
\x0a               \
             rig\
htPadding: 0\x0d\x0a  \
                \
          topPad\
ding: 0\x0d\x0a       \
                \
     bottomPaddi\
ng: 0\x0d\x0a\x0d\x0a       \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
     }\x0d\x0a\x0d\x0a      \
                \
  Item {\x0d\x0a      \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
       }\x0d\x0a      \
              }\x0d\
\x0a               \
 }\x0d\x0a\x0d\x0a          \
      Container \
{\x0d\x0a             \
       id: right\
TabBar\x0d\x0a\x0d\x0a      \
              cu\
rrentIndex: 1\x0d\x0a\x0d\
\x0a               \
     Layout.fill\
Height: true\x0d\x0a\x0d\x0a\
                \
    ButtonGroup \
{\x0d\x0a             \
           butto\
ns: rightTabBarC\
ontentLayout.chi\
ldren\x0d\x0a         \
           }\x0d\x0a\x0d\x0a\
                \
    contentItem:\
 ColumnLayout {\x0d\
\x0a               \
         id: rig\
htTabBarContentL\
ayout\x0d\x0a         \
               s\
pacing: 3\x0d\x0a\x0d\x0a   \
                \
     Repeater {\x0d\
\x0a               \
             mod\
el: rightTabBar.\
contentModel\x0d\x0a  \
                \
      }\x0d\x0a       \
             }\x0d\x0a\
\x0d\x0a              \
      Item {\x0d\x0a  \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
   }\x0d\x0a\x0d\x0a        \
            Feat\
ureButton {\x0d\x0a   \
                \
     text: qsTr(\
\x22Windows\x22)\x0d\x0a    \
                \
    icon.name: \x22\
windows\x22\x0d\x0a\x0d\x0a    \
                \
    Layout.maxim\
umHeight: naviga\
tionFeatureButto\
n.height\x0d\x0a      \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
               }\
\x0d\x0a              \
      FeatureBut\
ton {\x0d\x0a         \
               t\
ext: qsTr(\x22Air C\
on.\x22)\x0d\x0a         \
               i\
con.name: \x22air-c\
on\x22\x0d\x0a           \
             che\
cked: true\x0d\x0a\x0d\x0a  \
                \
      Layout.max\
imumHeight: navi\
gationFeatureBut\
ton.height\x0d\x0a    \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
 }\x0d\x0a            \
        FeatureB\
utton {\x0d\x0a       \
                \
 text: qsTr(\x22Sea\
ts\x22)\x0d\x0a          \
              ic\
on.name: \x22seats\x22\
\x0d\x0a\x0d\x0a            \
            Layo\
ut.maximumHeight\
: navigationFeat\
ureButton.height\
\x0d\x0a              \
          Layout\
.fillHeight: tru\
e\x0d\x0a             \
       }\x0d\x0a      \
              Fe\
atureButton {\x0d\x0a \
                \
       text: qsT\
r(\x22Statistics\x22)\x0d\
\x0a               \
         icon.na\
me: \x22statistics\x22\
\x0d\x0a\x0d\x0a            \
            Layo\
ut.maximumHeight\
: navigationFeat\
ureButton.height\
\x0d\x0a              \
          Layout\
.fillHeight: tru\
e\x0d\x0a             \
       }\x0d\x0a      \
          }\x0d\x0a   \
         }\x0d\x0a    \
    }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a \
   }\x0d\x0a\x0d\x0a    Roun\
dButton {\x0d\x0a     \
   id: roundButt\
on\x0d\x0a        x: 7\
41\x0d\x0a        y: 4\
22\x0d\x0a        widt\
h: 74\x0d\x0a        h\
eight: 77\x0d\x0a     \
   text: \x22M\x22\x0d\x0a  \
  }\x0d\x0a\x0d\x0a    TabBa\
r {\x0d\x0a        id:\
 bar\x0d\x0a        x:\
 94\x0d\x0a        y: \
0\x0d\x0a        width\
: 613\x0d\x0a        h\
eight: 41\x0d\x0a\x0d\x0a   \
     TabButton {\
\x0d\x0a            id\
: tabButton\x0d\x0a   \
         text: q\
sTr(\x22Delay\x22)\x0d\x0a  \
      }\x0d\x0a\x0d\x0a     \
   TabButton {\x0d\x0a\
            id: \
tabButton1\x0d\x0a    \
        text: qs\
Tr(\x22Reverb\x22)\x0d\x0a  \
      }\x0d\x0a\x0d\x0a     \
   TabButton {\x0d\x0a\
            id: \
tabButton2\x0d\x0a    \
        text: qs\
Tr(\x22Mixer\x22)\x0d\x0a   \
     }\x0d\x0a\x0d\x0a      \
  TabButton {\x0d\x0a \
           id: t\
abButton3\x0d\x0a     \
       text: qsT\
r(\x22Cab\x22)\x0d\x0a      \
  }\x0d\x0a    }\x0d\x0a\x0d\x0a\x0d\x0a\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a}\x0d\x0a\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a/*##^## D\
esigner {\x0d\x0a    D\
{i:125;invisible\
:true}\x0d\x0a}\x0d\x0a ##^#\
#*/\x0d\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x10\
\x04\xa4a|\
\x00G\
\x00l\x00o\x00w\x00i\x00n\x00g\x00L\x00a\x00b\x00e\x00l\x00.\x00q\x00m\x00l\
\x00\x11\
\x03\x80\x8f\xbc\
\x00F\
\x00e\x00a\x00t\x00u\x00r\x00e\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\
\x00\x0e\
\x0a@\x89\x5c\
\x00C\
\x00u\x00s\x00t\x00o\x00m\x00G\x00l\x00o\x00w\x00.\x00q\x00m\x00l\
\x00\x09\
\x0e\x07\x85\xdc\
\x00d\
\x00i\x00g\x00i\x00t\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x02\
\x00\x00\x002\x00\x00\x00\x00\x00\x01\x00\x00\x0e\x84\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00Z\x00\x00\x00\x00\x00\x01\x00\x00\x1a?\
\x00\x00\x00|\x00\x00\x00\x00\x00\x01\x00\x00$\x90\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
