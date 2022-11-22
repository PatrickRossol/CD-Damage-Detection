import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images

from skimage.io import imread_collection

import itertools

#your path 
col_dir = 'E:\Visual\Python\CD-Damage-Detection\img\*.jpg'

#creating a collection with the available images
col = imread_collection(col_dir)

img_list = []

for img in col:
    img_list.append(filters.sobel(color.rgb2gray(img)))

half_list = int(len(img_list) /2)
list_len = len(img_list)

fig, axes = plt.subplots(nrows = 3, ncols = 3, sharex=True, sharey=True, figsize=(10, 10))


for i, k in zip(range(3), range(0, 9, 3)):
    for j in range(3):
        axes[i, j].imshow(img_list[k+j], cmap='gray')






plt.tight_layout()
plt.show()