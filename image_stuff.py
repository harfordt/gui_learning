from __future__ import print_function

import sys
sys.path.append("N:\python-modules")

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

imagepath = input("What is the name of the image file? ")
try:
    im = Image.open(imagepath)
except IOError:
    print("Cannot read file")

value = float(input("Give me a value from 0 to 1(e.g. 0.5)"))
im = ImageEnhance.Contrast(im).enhance(float(value))
im.save("enhanced.jpg")
