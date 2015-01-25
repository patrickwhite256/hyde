#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core

if len(sys.argv) != 3:
    hyde_core.ragequit('USAGE: hyde.py <imagetohidein> <filetohide>')

if sys.argv[1][-4:] != '.png':
    hyde_core.ragequit('For now, I can only hide things in .png files.')

outfile = open(sys.argv[1][0:-4] + '-secret.png', 'wb')
hidden_file = open(sys.argv[2])
hyde_core.hyde(sys.argv[1], sys.argv[2], hidden_file, outfile)
outfile.close()
