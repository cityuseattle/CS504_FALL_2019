from PIL import Image

# image info and changing format

# this returns value of img object data type
img = Image.open('bulldog.jpg')
width, height = img.size
print("Width:", width, "Height:", height)
# if .jpg file, change to .png
if img.format == 'JPEG':
    img.save('bulldog2.png')