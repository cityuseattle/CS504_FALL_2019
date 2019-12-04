from PIL import Image

img = Image.open('bulldog.jpg')
width,height = img.size
print("Width:",width,"Height:",height)
if img.format == 'JPEG':
    img.save('bullgog2.png')
    