import sys
import png
from io import BytesIO

from . import png_image

def ragequit(message):
    print(message)
    sys.exit(0)

#header format: !?! <filename length> filename <file length> !?!
def build_header(filename, file_data):
    if(len(filename) > 255):
        ragequit('Filename too long!')
    file_len = len(file_data)
    filesize_info = b''
    while file_len > 0:
        byte = file_len & 255
        filesize_info += bytes([byte])
        file_len = file_len >> 8
    header_body = bytes([len(filename)]) + bytes(filename, 'UTF-8') + filesize_info
    return b'!?!' + header_body + b'!?!'

#hidefiledata: tuple (filename, binary file data)
#hiddenfiledata: tuple of same format
#return: binary png data
def hyde(hidefiledata, hiddenfiledata):

    if hidefiledata[0][-4:] != '.png':
        hyde_core.ragequit('For now, I can only hide things in .png files.')

    hide_image = png_image.read_from_filedata(hidefiledata[1])
    data_size = hide_image.width * hide_image.height

    file_data = hiddenfiledata[1]
    header_data = build_header(hiddenfiledata[0], file_data)

    store_bytes = header_data + file_data

    if len(store_bytes) > hide_image.width * hide_image.height:
        ragequit('Image not large enough!')

    for byte in store_bytes:
        hide_image.store_next_byte(byte)

    writer = png.Writer(width=hide_image.width, height=hide_image.height,
            alpha=hide_image.metadata['alpha'])

    out = BytesIO()
    writer.write(out, hide_image.pixels)
    return out.getvalue()

def read_bytes(image, n_bytes):
    return_value = b''
    for i in range(0, n_bytes):
        val = image.extract_next_byte()
        return_value += bytes([val])
    return return_value


#hidingfiledata: same as above
#return: binary file data, filename
def jekyll(hidingfiledata):

    if hidingfiledata[0][-4:] != '.png':
        ragequit('For now, I can only unhide things from .png files.')

    hiding_file = png_image.read_from_filedata(hidingfiledata[1])

    if read_bytes(hiding_file, 3) != b'!?!':
        ragequit('This file has nothing hiding in it (that I know about...)')

    filename_length = read_bytes(hiding_file, 1)[0]
    filename = read_bytes(hiding_file, filename_length).decode('UTF-8')

    size_to_end = b''
    while size_to_end[-3:] != b'!?!':
        size_to_end += read_bytes(hiding_file, 1)
    filesize = 0
    for byte in size_to_end[0:-3]:
        filesize = (filesize << 8) + byte
    file_contents = read_bytes(hiding_file, filesize)

    return file_contents, filename
