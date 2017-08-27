from PIL import Image
import numpy as np 
np.random.seed(100)

def random_pix():
  return np.random.randint(256, size=3)
  