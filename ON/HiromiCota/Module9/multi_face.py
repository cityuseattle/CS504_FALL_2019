from PIL import Image


def multi_face():
    #resize
    img = Image.open('pug.png')
    width, height = img.size
    resize = img.resize((int(width//4), int(height//4)))
    # What's double slash do that single slash doesn't?
    flip = resize.transpose(Image.FLIP_LEFT_RIGHT)
    fwidth, fheight = flip.size

    #make a pattern
    pattern = Image.new('RGBA', (590,428), 'green')
    # why'd we grab the dimensions if we're gonna hard code them?
    # make a 4x4 image grid
    w, h = pattern.size
    for left in range(0, w, fwidth):
        for top in range(0, h, fheight):
            pattern.paste(flip, (left, top))
    pattern.save('multi_face.png')

if __name__ == "__main__":
    multi_face()