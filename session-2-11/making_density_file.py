from netCDF4 import Dataset
import numpy as np
import seawater as sw

dataset = Dataset(r'/Users/helenfellow/Documents/cnn_paper/data/dataset-armor-3d-rep-weekly_1574699840388.nc')
# first step: import the data and get temp, salinity pressure
temperature = dataset['to']
salinity = dataset['so']
pressure = dataset['depth']

print(temperature.shape)
print(salinity.shape)
print(pressure.shape)

print(pressure[:])
#second step: make the pressure data 3 dimenional


pressure_3d = np.zeros((31,80,27))

# first_layer = np.repeat(10,80*27).reshape(80,27)

# second_layer = np.repeat(20,80*27).reshape(80,27)

 # for depth_level in pressure[:]:
 # 	print(np.repeat(depth_level,80*27).reshape((80,27)))
#print(pressure[:])
for i in range(0,31):
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))

#salinity = float(salinity)
#temperature = float(temperature)

density = sw.dens(salinity[:],temperature[:],pressure_3d)

print(density)
# to do: 

# inputs: salinity, temperature, pressure in form of netcdf file

