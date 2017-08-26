import random

import numpy as np
from PIL import Image


def array_fromim(path):
    with Image.open(path) as image:
        W, H = image.size
        return np.fromstring(image.tobytes(), dtype=np.uint8).reshape((H, W, 3))

def generate_random():
    while True:
        x, y = random.randint(0,W-4000), random.randint(0, H//3-1000)
        yield im[y:y+1000:10, x:x+2000:10]

def postprocess(arr):
    # arr = arr.mean(axis=2).astype('uint8')  # grayscaler
    return arr[::2,::2]


x,y,w,h = 800,0,16382-1620,3628//3
im = array_fromim('raw/IMG_4275.JPG')

sky_good = postprocess(im[y:h,x:w])
Image.fromarray(sky_good).save('crops/sky_good.png')

sky_bad = postprocess(im[y:h,x+w-1000:])
Image.fromarray(sky_bad).save('crops/sky_bad.png')
