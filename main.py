from os import listdir
from os.path import isfile, join
import shutil
import matplotlib.pyplot as plt
from skimage.io import imread_collection
from skimage import color
from skimage import filters



def white_pixel_counter(col):
    img_list = []

    for img in col:
        img_list.append(filters.sobel(color.rgb2gray(img)))

    ################### Display image
    fig, axes = plt.subplots(nrows = 2, ncols = 2, sharex=True, sharey=True, figsize=(12, 12))

    for i, k in zip(range(2), range(0, 4, 2)):
        for j in range(2):
            axes[i, j].imshow(img_list[k+j], cmap='gray')

    plt.tight_layout()
    plt.show()
    #####################

    for i in range(0, len(img_list)):
        img_list[i] = img_list[i] > 0.04

    
    pixel_list = []

    for img in img_list: 
        white_pixel = 0
        for d1_pixel in img:
            for d2_pixel in d1_pixel:
                if d2_pixel == True:
                    white_pixel += 1
        pixel_list.append(white_pixel)

    return pixel_list


#path for images
ref_dir = '.\\reference_good\*.jpg'
col_dir = '.\database\*.jpg'


#creating a collection with the available images
ref = imread_collection(ref_dir)
col = imread_collection(col_dir)


#counting the white pixels in the reference images
ref_pixel_cnt= white_pixel_counter(ref)


#getting the min and max value of the white picxels of the reference images
ref_min = min(ref_pixel_cnt)
ref_max = max(ref_pixel_cnt)


#counting the white pixels in the database images
col_pixel_cnt = white_pixel_counter(col)

bad_index_list = []
good_index_list = []


#sorting out the bad images and putting them in a list
for index, pixel_cnt in enumerate(col_pixel_cnt):
    if pixel_cnt > ref_min and pixel_cnt < ref_max:
        good_index_list.append(index)
    else:
        bad_index_list.append(index)


#moving the bad images to a new folder
only_files = [f for f in listdir('.\database') if isfile(join('.\database', f))]

for index in bad_index_list:
    shutil.move('.\database\\' + only_files[index], '.\sort_broken')