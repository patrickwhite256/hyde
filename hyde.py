#!/usr/bin/env python

import sys
import png

def read_image(infile):
    reader = png.Reader(filename=infile)
    return PngImage(*reader.read())

class PngImage:
    "a simple wrapper around the data returned by the PyPng library"

    def __init__(self, width, height, pixels, metadata):
        self.width = width
        self.height = height
        self.pixels = pixels
        self.metadata = metadata


if len(sys.argv) != 3:
    print('USAGE: hyde.py <imagetohidein> <filetohide>')
    sys.exit(0)

if sys.argv[1][-4:] != '.png':
    print('For now, I can only hide things in .png files.')
    sys.exit(0)

read_image(sys.argv[1])
