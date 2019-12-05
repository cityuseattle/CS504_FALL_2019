from PIL import Image, ImageFilter

img = Image.open('bulldog2.png')
im_blurred = img.filter(filter=ImageFilter.BLUR)
im_blurred.save('blur.jpg')

img_gray = img.convert('L')
img_gray.save('grayscale.png')