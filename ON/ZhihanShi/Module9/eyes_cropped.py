from PIL import Image

img = Image.open('bullgog2.png')

cropped = img.crop((0,150,590,235))
cropped.save('eyes_cropped.png')
copy_img = img.copy()
copy_img.paste(cropped,(0,0))

copy_img.save('four_eyes_bulldog.png')
