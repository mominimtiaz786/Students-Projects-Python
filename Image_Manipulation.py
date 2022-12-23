# !!! pip install pillow

from PIL import Image

image = Image.open('path/to/image.jpg')

new_size = (200, 200)

image = image.resize(new_size)
image = image.rotate(45)

from PIL import ImageFilter

image = image.filter(ImageFilter.BLUR)

image.save('path/to/modified_image.jpg')
