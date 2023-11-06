from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/Noisyedits'

def noisyedits():
    for filename in os.listdir(path):
        # opening an image allowing edit
        img = Image.open(f"{path}/{filename}")

        #noisy
        edit2 = img.convert('1')

        clean_name = os.path.splitext(filename)[0]

        edit2.save(f'.{pathOut}/{clean_name}_noisyedit.jpg')
        # print('Image Noised Successfully! ')




noisyedits()
# print('Image Noised Successfully! ')
