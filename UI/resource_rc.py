# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Wed Jan 16 15:42:01 2019
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x01#\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0a\x0d\x0a[Im\
agine]\x0d\x0aPath=:/i\
magine-assets\x0d\x0aP\
alette\x5cText=#6af\
fcd\x0d\x0aPalette\x5cBut\
tonText=#6affcd\x0d\
\x0aPalette\x5cWindowT\
ext=#6affcd\x0d\x0a\x0d\x0a[\
Material]\x0d\x0aFont\x5c\
Family=Open Sans\
 Light\x0d\x0aFont\x5c\x5c%2\
A%20PixelSize=20\
 */\x0d\x0aFont\x5cWeight\
=12\x0d\x0a\x0d\x0a[Default]\
\x0d\x0aFont\x5cFamily=Op\
en Sans Light\x0d\x0aF\
ont\x5cPixelSize=20\
\x0d\x0a\
"

qt_resource_name = b"\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
