from matplotlib import pyplot as plt
from skimage import io

img = io.imread("E:\Visual\Python\CD-Damage-Detection\img\image_50334977.JPG", as_gray = True)

plt.imshow (img)