#!/usr/bin/env python

import sys
import png
import png_image

def ragequit(message):
    print(message)
    sys.exit(0)

#header format: !?! <filename length> filename <file length> !?!
def build_header(filename, file_data):
    if(len(filename) > 255):
        ragequit('Filename too long!')
    file_len = len(file_data)
    filesize_info = ''
    while file_len > 0:
        byte = file_len & 255
        filesize_info += chr(byte)
        file_len = (file_len - byte) / 256
    header_body = chr(len(filename)) + filename + filesize_info
    return '!?!' + header_body + '!?!'

if len(sys.argv) != 3:
    ragequit('USAGE: hyde.py <imagetohidein> <filetohide>')

if sys.argv[1][-4:] != '.png':
    ragequit('For now, I can only hide things in .png files.')

hide_image = png_image.read_from_file(sys.argv[1])
data_size = hide_image.width * hide_image.height


hidden_file = open(sys.argv[2])
file_data = hidden_file.read()
header_data = build_header(sys.argv[2], file_data)

store_bytes = list(header_data) + list(file_data)

if len(store_bytes) > hide_image.width * hide_image.height:
    ragequit("Image not large enough!")

for char in store_bytes:
    hide_image.store_next_byte(ord(char))

writer = png.Writer(width=hide_image.width, height=hide_image.height)

outfile = open(sys.argv[1][0:-4] + '-secret.png', 'wb')
writer.write(outfile, hide_image.pixels)
