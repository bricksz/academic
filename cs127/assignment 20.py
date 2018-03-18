#Terry Huang
#feb 18, 2018
#assignment 20

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):

    for col in range(mapShape[1]):
        #color scheme [x,y,z], z=(0,1,2) ; (red, green, blue)

        if elevations[row, col] <= 0:

            floodMap[row, col, 2] = .5

        elif elevations[row, col] == 1:
            floodMap[row, col, 0] = .75
            floodMap[row, col, 1] = .75
            floodMap[row, col, 2] = .75

        else:

            floodMap[row, col, 0] = .5
            floodMap[row, col, 1] = .5
            floodMap[row, col, 2] = .5

plt.imshow(floodMap)

plt.show()

plt.imsave('coast.png', floodMap)