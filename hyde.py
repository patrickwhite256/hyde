#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core

if len(sys.argv) != 3:
    print('USAGE: hyde.py <imagetohidein> <filetohide>')
    exit(1)

hide_file = open(sys.argv[1], 'rb')
hide_filedata = hide_file.read()
hide_file.close()
hidden_file = open(sys.argv[2], 'rb')
hidden_filedata = hidden_file.read()
hidden_file.close()

try:
    out_bytes = hyde_core.hyde((sys.argv[1], hide_filedata),
                               (sys.argv[2], hidden_filedata))
except hyde_core.HydeException as e:
    print(e.msg)
    exit(1)

outfile = open(sys.argv[1][0:-4] + '-secret.png', 'wb')
outfile.write(out_bytes)
outfile.close()
