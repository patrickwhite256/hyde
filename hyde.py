#!/usr/bin/env python

import sys
import png

def ragequit(message):
    print(message)
    sys.exit(0)

def read_image(infile):
    reader = png.Reader(filename=infile)
    return PngImage(*reader.read())

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

class PngImage:
    "a simple wrapper around the data returned by the PyPng library"

    def __init__(self, width, height, pixels, metadata):
        self.width = width
        self.height = height
        self.pixels = list(pixels)
        self.metadata = metadata
        self.next_x = 0
        self.next_y = 0

    def store_next_byte(self, byte):
        self.store_byte_in_pixel(byte, self.next_x, self.next_y)
        self.next_x += 1
        if self.next_x == self.width:
            self.next_x = 0
            self.next_y += 1

    def store_byte_in_pixel(self, byte, x, y):
        r_index = x * (3 if self.metadata['alpha'] else 3)
        self.pixels[y][r_index] = (self.pixels[y][r_index] & 0b11111000) | (
                byte >> 5)
        self.pixels[y][r_index + 1] = (self.pixels[y][r_index + 1] & 0b11111000) | (
                byte >> 2 & 0b111)
        self.pixels[y][r_index + 2] = (self.pixels[y][r_index + 2] & 0b11111100) | (
                byte & 0b11)
        

if len(sys.argv) != 3:
    ragequit('USAGE: hyde.py <imagetohidein> <filetohide>')

if sys.argv[1][-4:] != '.png':
    ragequit('For now, I can only hide things in .png files.')

hide_image = read_image(sys.argv[1])
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
