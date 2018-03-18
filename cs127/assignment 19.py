#Terry Huang
#feb 18, 2018
#assignment 19

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):

    for col in range(mapShape[1]):
        #color scheme [x,y,z], z=(0,1,2) ; (red, green, blue)

        if elevations[row, col] <= 0:

            floodMap[row, col, 2] = 1

        elif elevations[row, col] <= 6:

            floodMap[row, col, 0] = 1

        elif elevations[row, col] <= 20:
            floodMap[row, col, 0] = .5
            floodMap[row, col, 1] = .5
            floodMap[row, col, 2] = .5

        else:

            floodMap[row, col, 1] = 1

plt.imshow(floodMap)

plt.show()

plt.imsave('floodMap.png', floodMap)