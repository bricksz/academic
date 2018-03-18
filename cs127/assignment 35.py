#terry huang
#3/15/2018
#assignment 35

import matplotlib.pyplot as plt
import numpy as np

x = input('Enter file name: ')
img = plt.imread(x)

#imgage shape in (Y, X, Z)
height = img.shape[0]
width = img.shape[1]

img2 = img[height//2:, :width//2]

plt.imshow(img2)
plt.show()

y = input('Enter output name: ')

plt.imsave(y, img2)