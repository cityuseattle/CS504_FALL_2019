from PIL import Image


img = Image.open('pug.png')
# crop the eyes
cropped = img.crop((0, 150, 590, 235))
cropped.save('eyes_cropped.png')

copy_img = img.copy()
copy_img.paste(cropped, (0,0))
# is there a builtin for 0,0? Seems like it'd be a normal default value
copy_img.save('four_eyes_pug.png')
# That's still a pug, not a bulldog