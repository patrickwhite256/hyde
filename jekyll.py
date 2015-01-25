#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core


if len(sys.argv) != 2:
    hyde_core.ragequit('USAGE: jekyll.py <file>')

if sys.argv[1][-4:] != '.png':
    hyde_core.ragequit('For now, I can only unhide things from .png files.')

hyde_core.jekyll(sys.argv[1])
