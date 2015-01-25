#!/usr/bin/env python

import sys
import png_image

def ragequit(message):
    print(message)
    sys.exit(0)

def read_bytes(image, n_bytes):
    return_value = ''
    for i in range(0, n_bytes):
        val = image.extract_next_byte()
        return_value += chr(val)
    return return_value


if len(sys.argv) != 2:
    ragequit('USAGE: jekyll.py <file>')

if sys.argv[1][-4:] != '.png':
    ragequit('For now, I can only unhide things from .png files.')

hiding_file = png_image.read_from_file(sys.argv[1])

if read_bytes(hiding_file, 3) != '!?!':
    ragequit('This file has nothing hiding in it (that I know about...)')

filename_length = ord(read_bytes(hiding_file, 1))
filename = read_bytes(hiding_file, filename_length)

size_to_end = ''
while size_to_end[-3:] != '!?!':
    size_to_end += read_bytes(hiding_file, 1)
filesize = 0
for char in size_to_end[0:-3]:
    filesize = (filesize << 8) + ord(char)
file_contents = read_bytes(hiding_file, filesize)

outfile = open(filename, 'wb')
outfile.write(bytes(file_contents, 'UTF-8'))
outfile.close()
