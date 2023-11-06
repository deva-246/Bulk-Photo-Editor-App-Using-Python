from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

def bwconvertor():

    for filename in os.listdir(path):

        # opening an image allowing edit
        img = Image.open(f"{path}/{filename}")

        #editing properties - sharpen, contrast, enhancement , Black and white

        edit = img.filter(ImageFilter.SHARPEN).convert('L')

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)


        clean_name = os.path.splitext(filename)[0]

        edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
        # print('Image converted to black and white successfully!')



# bwconvertor()
# print('Image converted to black and white successfully!')


