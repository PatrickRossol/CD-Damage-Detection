from skimage import io, color
import matplotlib.pyplot as plt
from skimage import filters

img1 = io.imread("E:\Visual\Python\CD-Damage-Detection\img\image_50387457.JPG", as_gray=True)
img2 = io.imread("E:\Visual\Python\CD-Damage-Detection\img\image_50372865.JPG", as_gray=True)

mylist = [img1, img2]

for img in mylist:
   # plt.imshow(img, cmap='gray')
    thresh = filters.threshold_yen(img)
    binary = img <= thresh
   # fig, ax = filters.try_all_threshold(img, figsize=(10, 8), verbose=False)
    #plt.show()
    plt.imshow(binary, cmap='gray')

plt.show()