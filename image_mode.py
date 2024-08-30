from PIL import Image
from os.path import join

image1 = Image.open(join('resources', 'cat_bw.jpg')).convert('RGB')
image2 = Image.open(join('resources', 'raccoon.png')).convert('L')

print(image1.mode)
print(image2.mode)

image1.paste(image2, (100, 400))

image1.show()