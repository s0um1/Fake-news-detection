#!/usr/bin/env python

from PIL import Image, ImageChops


#ORIG = './books-edited.jpg'
ORIG = 'img.jpeg'
TEMP = 'temp.jpg'
SAVE = 'tosend.jpg'
SCALE = 15


def ELA():
    original = Image.open(ORIG)
    original.save(TEMP, quality=50)
    temporary = Image.open(TEMP)

    diff = ImageChops.difference(original, temporary)
    d = diff.load()
    WIDTH, HEIGHT = diff.size
    print("width = ", WIDTH)
    print("height = ", HEIGHT)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            d[x, y] = tuple(k * SCALE for k in d[x, y])

    print(diff)
    print(d)
    diff.save(SAVE)


if __name__ == '__main__':
    ELA()
