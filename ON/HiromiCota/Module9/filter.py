from PIL import Image, ImageFilter


#blur the image
img = Image.open('pug.png')
im_blurred = img.filter(filter=ImageFilter.BLUR)
im_blurred.save('blur.jpg')

#greyscale
img_grey = img.convert('L')
img_grey.save('grayscale.png')