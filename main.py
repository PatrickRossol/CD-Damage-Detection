import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images

from skimage.io import imread_collection

import itertools

#your path 
col_dir = 'E:\Visual\Python\CD-Damage-Detection\img_eve\dam\*.jpg'

#creating a collection with the available images
col = imread_collection(col_dir)

img_list = []

for img in col:
    img_list.append(filters.sobel(color.rgb2gray(img)))


#for i in range(0, len(img_list)):
# thresh = filters.threshold_isodata(img_list[i])
# img_list[0] = img_list[i] > thresh

for i in range(0, len(img_list)):
    img_list[i] = img_list[i] > 0.08

pixel_list = []

for img in img_list:
    whitePixel = 0
    for d1Pixel in img:
        for d2Pixel in d1Pixel:
            if d2Pixel == True:
                whitePixel += 1
    pixel_list.append(whitePixel)
        

print(pixel_list)



fig, axes = plt.subplots(nrows = 2, ncols = 2, sharex=True, sharey=True, figsize=(12, 12))


for i, k in zip(range(2), range(0, 4, 2)):
    for j in range(2):
        axes[i, j].imshow(img_list[k+j], cmap='gray')

# for i, k in zip(range(2), range(0, 9, 3)):
#     for j in range(2):
#         axes[i, j].imshow(img_list[k+j], cmap='gray')




plt.tight_layout()
plt.show()