__author__ = 'will'
from PIL import Image, ImageDraw
import binascii

import sys


def create_base_image(w, h):
    real_size = (w+6, h+6)
    bottom_right_corner = (w+5, h+5)
    im = Image.new('RGB', real_size, color=(255, 255, 255))

    ## drawing outer rectangle
    draw = ImageDraw.Draw(im)
    draw.rectangle([(0, 0), bottom_right_corner], outline=0)

    ##  drawing 3 corners

    draw.point([2, 2], fill=0)
    draw.point([2, h+3], fill=0)
    draw.point([h+3, 2], fill=0)
    del draw

    return im


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print """usage: token_encoder.py [data] [width, height] [output file]"""
        exit(0)

    data = None
    w, h = 10, 10
    outputfile = "output.png"

    if len(sys.argv) >= 2:
        data = sys.argv[1]
    if len(sys.argv) >= 3:
        w, h = int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) >= 5:
        outputfile = sys.argv[4]

    print "image:", (w, h), "data", data, "saving to ", outputfile


    data_size_available = w*h - 3

    im = create_base_image(w, h)
    draw = ImageDraw.Draw(im)

    databits = ''.join(format(ord(x), 'b') for x in data)

    print databits, len(databits)

    for i, char in enumerate(databits):
        xpos = i % w + 3
        ypos = i / w + 3
        if char == '1':
            draw.point([xpos, ypos], fill=0)

    im = im.resize((512, 512))
    im.save(outputfile, 'PNG')











