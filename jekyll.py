#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core


if len(sys.argv) != 2:
    print('USAGE: jekyll.py <file>')
    exit(1)

hiding_file = open(sys.argv[1], 'rb')
hiding_filedata = hiding_file.read()
hiding_file.close()

try:
    out_bytes, filename = hyde_core.jekyll((sys.argv[1], hiding_filedata))
except hyde_core.HydeException as e:
    print(e.msg)
    exit(1)

outfile = open(filename, 'wb')
outfile.write(out_bytes)
outfile.close()
