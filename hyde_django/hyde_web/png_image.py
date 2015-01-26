import png

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
        r_index = x * (4 if self.metadata['alpha'] else 3)
        self.pixels[y][r_index] = (self.pixels[y][r_index] & 0b11111000) | (
                byte >> 5)
        self.pixels[y][r_index + 1] = (self.pixels[y][r_index + 1] & 0b11111000) | (
                byte >> 2 & 0b111)
        self.pixels[y][r_index + 2] = (self.pixels[y][r_index + 2] & 0b11111100) | (
                byte & 0b11)
    
    def extract_next_byte(self):
        return_value = self.extract_byte_from_pixel(self.next_x, self.next_y)
        self.next_x += 1
        if self.next_x == self.width:
            self.next_x = 0
            self.next_y += 1
        return return_value

    def extract_byte_from_pixel(self, x, y):
        r_index = x * (4 if self.metadata['alpha'] else 3)
        return (((self.pixels[y][r_index] & 0b111) << 5) +
                ((self.pixels[y][r_index + 1] & 0b111) << 2) +
                ((self.pixels[y][r_index + 2] & 0b11)))


def read_from_filedata(filebytes):
    reader = png.Reader(bytes=filebytes)
    return PngImage(*reader.read())
