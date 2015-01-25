#!/usr/bin/env python

import sys
from hyde_django.hyde_web import hyde_core


if len(sys.argv) != 2:
    ragequit('USAGE: jekyll.py <file>')

hyde_core.jekyll(sys.argv[1])
