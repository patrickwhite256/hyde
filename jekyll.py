#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core


if len(sys.argv) != 2:
    hyde_core.ragequit('USAGE: jekyll.py <file>')

hiding_file = open(sys.argv[1], 'rb')
hiding_filedata = hiding_file.read()
hiding_file.close()

out_bytes, filename = hyde_core.jekyll((sys.argv[1], hiding_filedata))

outfile = open(filename, 'wb')
outfile.write(out_bytes)
outfile.close()
