import random
random.seed(100)
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt

def array_fromim(path):
    with Image.open(path) as image:
        W, H = image.size
        return np.fromstring(image.tobytes(), dtype=np.uint8).reshape((H, W, 3))


def threebythree(N):
  
  print ('Generating 3x3')
  im = array_fromim('crops\\sky_good.png')
  h,w,d = im.shape

  samples = [ (random.randint(1,(h-2)),random.randint(1,(w-2))) for _ in range(N)]

  samples=  np.array(samples)

  for j in range(-1,2):
  	for i in range(-1,2):
  	  print(i,j)
  	  inter = np.array([samples[:,0]+j,samples[:,1]+i]).T
  	  samples = np.concatenate((samples,inter), axis=1)

  samples = np.delete(samples, np.s_[10:12], axis=1)

  #samples = np.array(samples)
  #print (samples)

  #print(samples[:,0].shape)
  a = [ 2*k for k in range(9)]
  b = [(2*k+1) for k in range(9)]

  R = np.array([im[samples[:,i],samples[:,j],0] for i,j in zip(a,b)]).T
  G = np.array([im[samples[:,i],samples[:,j],1] for i,j in zip(a,b)]).T
  B = np.array([im[samples[:,i],samples[:,j],2] for i,j in zip(a,b)]).T

  y_R = R[:,0]
  y_G = G[:,0]
  y_B = B[:,0]
  cube = np.array([R[:,1:],G[:,1:],B[:,1:]])
  cube = np.swapaxes(cube,0,2)
  cube = np.swapaxes(cube,0,1)
  print(cube)
  np.savez('data\\3x3.npz',X=cube, y_R = y_R, y_G = y_G, y_B = y_B)

  #Nx8x3

  #    j,i
  #    1  2  3
  #    4  0  5
  #    6  7  8


if __name__ == "__main__":
  threebythree(5000)