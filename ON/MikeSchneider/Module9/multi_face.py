from PIL import Image


def multi_face():

img = Image.open(‘bulldog2.png)
width, height = img.size
resize = img.resize((int(width//4), int(height//4)))

flip = resize.transpose(Image.FLIP_LEFT_RIGHT)
fwidth, fheight = flip.size


pattern = Image.new(‘RGBA’, (590, 428), ‘green’)

w, h = pattern.size
for left in range(0, w, fwidth):
for top in range(0, h, fheight):
pattern.paste(flip, (let, top))
pattern.save(‘multi_face.png)


if __name__ == “__main__”:
multi_face()
