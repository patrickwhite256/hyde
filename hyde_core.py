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

def hyde(hidefilename, hiddenfilename, outfile):
    hide_image = png_image.read_from_file(hidefilename)
    data_size = hide_image.width * hide_image.height

    hidden_file = open(hiddenfilename)
    file_data = hidden_file.read()
    header_data = build_header(hiddenfilename, file_data)

    store_bytes = list(header_data) + list(file_data)

    if len(store_bytes) > hide_image.width * hide_image.height:
        ragequit("Image not large enough!")

    for char in store_bytes:
        hide_image.store_next_byte(ord(char))

    writer = png.Writer(width=hide_image.width, height=hide_image.height)

    writer.write(outfile, hide_image.pixels)

def read_bytes(image, n_bytes):
    return_value = ''
    for i in range(0, n_bytes):
        val = image.extract_next_byte()
        return_value += chr(val)
    return return_value


def jekyll(filename, outfile=None):

    if filename[-4:] != '.png':
        ragequit('For now, I can only unhide things from .png files.')
    hiding_file = png_image.read_from_file(filename)

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

    if outfile is None:
        outfile = open(filename, 'wb')
    outfile.write(bytes(file_contents, 'UTF-8'))
