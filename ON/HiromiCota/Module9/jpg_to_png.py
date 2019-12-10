from PIL import Image


img = Image.open('pug.jpg')
# That's a pug, not a bulldog
width, height = img.size
print("Width:", width, "Height:", height)
# check to confirm that it's a jpg because file extensions are not always correct
if img.format == 'JPEG':
    img.save('pug.png')
