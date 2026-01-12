import matplotlib.pyplot as mpl
import numpy as np


x = np.array[90, 50, 40, 70, 69]
y = np.array[2, 4, 6, 8, 10]
mpl.scatter(x,y)

x = np.array[45, 23, 56, 78, 21, 89]
y = np.array[34, 56 ,89 ,23 ,21]
mpl.scatter(x, y)

mpl.xlabel("area of car lot")
mpl.ylabel("number of cars")

mpl.show()