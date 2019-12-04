from PIL import Image, ImageFilter

# blur image
img = Image.open('bulldog2.png')
im_blurred = img.filter(filter=ImageFilter.BLUR)
im_blurred.save('blur.jpg')

# grayscale
img_gray = img.convert('L')
img_gray.save('grayscale.png')
