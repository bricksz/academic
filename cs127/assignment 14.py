#terry huang
#feb 13, 2018
#assignment 14

import matplotlib.pyplot as plt
import numpy as np

x=input('Enter name of the input file: ')
y=input('Enter name of the output file: ')

img = plt.imread(x)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2 [:,:,0] = 0
img2 [:,:,2] = 0

plt.imshow(img2)
plt.show()

plt.imsave(y, img2)