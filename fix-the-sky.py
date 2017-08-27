from models import random_pix
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt

def array_fromim(path):
    with Image.open(path) as image:
        W, H = image.size
        return np.fromstring(image.tobytes(), dtype=np.uint8).reshape((H, W, 3))

def grayscaler(arr):
    # arr = arr.mean(axis=2).astype('uint8')  # grayscaler
    return arr[::2,::2]

def bad_pix(arr):
  threshold = 15						
  if np.any(arr == 0):					#get pixels that have a 0 somewhere
  	return False
  elif np.sum(arr)<threshold:			#or that fall below a threshold of their sum (e.g. 15)
  	return False
  else:
  	return True


def mask_bad(im):
  mask = np.apply_along_axis(bad_pix,2,im) 		#boolean
  return mask

def edge_mask(mask):
  h,w = mask.shape
  mask = mask.astype('uint8')
  em = np.zeros((h,w),dtype=bool)

  ### add edge exceptions later
  for i in range(1,(w-1)):
  	for j in range(1,(h-1)):
  	  if (mask[j,i]==0) and ((mask[j+1,i]+mask[j-1,i]+mask[j,i+1]+mask[j,i-1])>1):
  	  	em[j,i]=True
  return em

def iter_im(im,em,model):
  h,w,d = im.shape
  for i in range(1,(w-1)):
  	for j in range(1,(h-1)): 
  	  if em[j,i]==True:
  	  	im[j,i,:]=model()
  return im


def main():


  im = array_fromim('crops\\sky_bad.png')

  for _ in range(40):
    print('iter',_)
    mask = mask_bad(im)
    em = edge_mask(mask)
    im = iter_im(im,em,random_pix.random_pix)

    #plt on the fly
    #plt.imshow(im)
    #plt.draw()
    #plt.pause(0.05)

  ### Some outputs
  Image.fromarray(im).save('im_post.png')

  #mask = mask.astype('uint8')
  #mask[mask>0] = 255
  #Image.fromarray(mask).save('mask.png')
  
  #em = em.astype('uint8')
  #em[em>0] = 255
  #Image.fromarray(em).save('selected.png')

  print('-- DONE --')

if __name__ == "__main__":
  main()