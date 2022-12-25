from PIL import Image,ImageEnhance,ImageFilter
import os

img  = Image.open('F:/hey/extra/dog.jpg')

# img.save('dog1.png')
# img.show

# max_siz = (250,250)
# img.thumbnail(max_siz)
# img.save('F:/hey/extra/dogsmall.jpg')

# if ('F:/hey/extra/dog.jpg').endswith('.jpg'):
#     print("yes")

# name,extention = os.path.splitext('F:/hey/extra/dog.jpg')
# print(extention)

# en = ImageEnhance.Sharpness(img)
# en.enhance(0).save('F:/hey/extra/dogblurr.jpg')

# en = ImageEnhance.Color(img)
# en.enhance(6).save('F:/hey/extra/dogcr.jpg')

# en = ImageEnhance.Brightness(img)
# en.enhance(1.3).save('F:/hey/extra/dogbr.jpg')

# en = ImageEnhance.Contrast(img)
# en.enhance(1.3).save('F:/hey/extra/dogcon.jpg')

# img.filter(ImageFilter.GaussianBlur(radius=6)).save('F:/hey/extra/dogblr.jpg')