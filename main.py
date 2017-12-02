# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw

def drawing(img,imgae_array):
    x,y = img.size
    draw = ImageDraw.Draw(img)
    for i in range(0,x):
        for j in range(0,y):
            if imgae_array[j][i]==1:
                draw.point((i,j),(0x00))
    img = img.resize((300,300))
    return img

def make_image(screen, bgcolor, filename,imgae_array):
    img = Image.new('L', screen, bgcolor)
    img = drawing(img,imgae_array)
    img.save(filename)

if __name__ == '__main__':
    f = open('source.py')
    lines = f.readlines()
    f.close()
    width = 0
    for line in lines:
        if len(line) > width:
            width = len(line)

    height = len(lines)

    screen = (width,height) #横 縦

    bgcolor=0xff
    imgae_array = [[0 for i in range(width)] for j in range(height)]
    for i,s in enumerate(lines):
        for j,w in enumerate(s):
            if(w!=' ' and w != '¥t'):
                imgae_array[i][j] = 1
    filename = "source.png"
    make_image(screen, bgcolor, filename,imgae_array)
