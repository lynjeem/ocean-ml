from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w = dataset['w']
print(w.shape)


w_lat = w[:,0,:,0]
w_lat = np.swapaxes(w_lat,0,1)
lat = dataset['latitude']
title = "hovmoller diagram at latitude " + str(lat[0])
print(w_lat.shape)

plt.title(title)
top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
newcmp = ListedColormap(newcolors, name='RedBlue')
plt.pcolormesh(w_lat,cmap = newcmp)

plt.show()