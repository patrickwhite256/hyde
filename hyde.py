#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core

if len(sys.argv) != 3:
    hyde_core.ragequit('USAGE: hyde.py <imagetohidein> <filetohide>')

hide_file = open(sys.argv[1], 'rb')
hide_filedata = hide_file.read()
hide_file.close()
hidden_file = open(sys.argv[2], 'rb')
hidden_filedata = hidden_file.read()
hidden_file.close()

out_bytes = hyde_core.hyde((sys.argv[1], hide_filedata),
                           (sys.argv[2], hidden_filedata))

outfile = open(sys.argv[1][0:-4] + '-secret.png', 'wb')
outfile.write(out_bytes)
outfile.close()
