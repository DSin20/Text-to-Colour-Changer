##Colour Converter project
import math
from PIL import Image, ImageDraw, ImageFont

def text_to_colour(data):
    r = [ord(i) for i in data] + [0 for i in range(4 - (len(data)%4))]
    return [(r[c],r[c+1],r[c+2],r[c+3]) for c in range(0,len(r),4)]

def colour_to_text(data):
    return ("".join([chr(i) for j in data for i in j]))


def encoder(txt_file):
    f = open(txt_file, 'r')
    text = f.read()
    RGB_list = text_to_colour(text)
    s = math.ceil(math.sqrt(len(RGB_list)))
    blank = Image.new('RGBA',(s,s), (0, 0, 0, 0))
    pixels = blank.load()

    width, height = blank.size
    i = 0
    for y in range(width):
        for x in range(height):
            if i < len(RGB_list):
                pixels[x, y] = RGB_list[i]
                i += 1
    return blank

def decoder(image):
    Im = Image.open(image)
    pixels = Im.load()
    RGB_list = []
    width, height = Im.size
    for y in range(width):
        for x in range(height):
            RGB_list += [pixels[x, y]]

    return colour_to_text(RGB_list)


encoder('Taming_Of_The_Shrew.txt').save("image3.png")
#print(decoder("image3.png"))