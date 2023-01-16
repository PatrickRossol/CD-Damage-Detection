import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

from skimage import filters

from skimage.io import imread_collection

import itertools
import shutil

from os import listdir
from os.path import isfile, join



def white_pixel_counter(col):
    img_list = []

    for img in col:
        img_list.append(filters.sobel(color.rgb2gray(img)))


    #for i in range(0, len(img_list)):
    # thresh = filters.threshold_isodata(img_list[i])
    # img_list[0] = img_list[i] > thresh

    for i in range(0, len(img_list)):
        img_list[i] = img_list[i] > 0.05

    pixel_list = []

    for img in img_list: 
        whitePixel = 0
        for d1Pixel in img:
            for d2Pixel in d1Pixel:
                if d2Pixel == True:
                    whitePixel += 1
        pixel_list.append(whitePixel)

    return pixel_list

#your path
ref_dir = '.\\reference_good\*.jpg'
col_dir = '.\database\*.jpg'

#creating a collection with the available images
ref = imread_collection(ref_dir)
col = imread_collection(col_dir)



ref_pixel_cnt = white_pixel_counter(ref)
ref_min = min(ref_pixel_cnt)
ref_max = max(ref_pixel_cnt)

col_pixel_cnt = white_pixel_counter(col)

bad_index_list = []
good_index_list = []

for index, pixel_cnt in enumerate(col_pixel_cnt):
    if pixel_cnt > ref_min and pixel_cnt < ref_max:
        good_index_list.append(index)
    else:
        bad_index_list.append(index)



onlyfiles = [f for f in listdir('.\database') if isfile(join('.\database', f))]

for index in bad_index_list:
    shutil.move('.\database\\' + onlyfiles[index], '.\sort_broken') 






# fig, axes = plt.subplots(nrows = 2, ncols = 2, sharex=True, sharey=True, figsize=(12, 12))


# for i, k in zip(range(2), range(0, 4, 2)):
#     for j in range(2):
#         axes[i, j].imshow(img_list[k+j], cmap='gray')

# for i, k in zip(range(2), range(0, 9, 3)):
#     for j in range(2):
#         axes[i, j].imshow(img_list[k+j], cmap='gray')




# plt.tight_layout()
# plt.show()