from PIL import Image

def multi_face():
    
    #resize
    img = Image.open('bulldog.jpg')
    width, height = img.size
    resize = img.resize((int(width//4), int(height//4)))
    # flip image from left to right like mirror
    flip = resize.transpose(Image.FLIP_LEFT_RIGHT)
    fwidth, fheight = flip.size

    # add small flipped images into pattern
    pattern = Image.new('RGBA', (590, 428), 'green')
    # image grid 4x4
    w, h = pattern.size
    for left in range(0, w, fwidth):
        for top in range(0, h, fheight):
            pattern.paste(flip, (left, top))
    pattern.save('multi_face.png')

if __name__ == "__main__":
    multi_face()

