from PIL import Image

import random

def divide_img(image, n):
    '''
    @param n: size of rows x columns of created grid. For example, n := 4
    creates a 4x4 grid with a total of 16 sub-images.
    '''
    subs = []
    sub_w = image.size[0] / n # Width of sub-image
    sub_h = image.size[1] / n # Height of sub-image
    
    for i in range(n):
        for j in range(n):
            left = sub_w * i
            upper = sub_h * i
            right = sub_w * i + sub_w
            lower = sub_h * i + sub_h

            sub_img = image.crop((left, upper, right, lower))
            subs.append(sub_img)

    return subs

#TODO
# Create list of sub-images
# img_subs = divide_img(img, n)

# Save sub-images in random order
indices_used = []
filename_prefix = 'angel_of_death'
for sub in im_subs:
    i = random.randrange(1, len(im_subs)+1)
    while i in indices_used:
        i = random.randrange(1, len(im_subs)+1)
    indices_used.append(i)
    sub.save(f'subimages/{filename_prefix}_pt{i}.png') # Assumes "subimages" directory exists
