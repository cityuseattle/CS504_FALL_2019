from PIL import Image

img = Image.open('bulldog.jpg')
width, height = img.size
print("Width:", width, "Height:", height)

# if .jpg file, change to .png
if img.format == "JPEG":
    img.save('bulldog2.png')