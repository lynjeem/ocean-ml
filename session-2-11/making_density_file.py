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

<<<<<<< HEAD
#inputs: salinty, temperature, pressure in form of netcdf file
#first step import data and get the inputs 

from netCDF4 import Dataset
import numpy as np 

dataset = Dataset(r"/Users/brownscholar/Documents/Dataset/dataset-armor-3d-rep-weekly_1574699840388.nc")
 
pressure = dataset['depth']
temperature = dataset['to']
salinty = dataset['so']

print(temperature.shape)
print(salinty.shape)
print(pressure.shape)

#
#second step: maket the pressure data 3 dimensional

pressure_3D = np.zeros((31,80,27))

layer1 = np.repeat(10,80*27).reshape(80,27)

#layer2 = np.repeat(20,80*27).reshape(80,27)





for i in pressure[:]:
	print(np.repeat(i,80*27).reshape(80,27))

	
for i in range(0,31):
	print(np.repeat(pressure[i],80*27).reshape((80,27)))
	print(pressure_3D[i,:,:])
	print(np.repeat)

for i in range(0,31):
	pressure_3D[i,:,:] = np.repeat(pressure[i],80*27).reshape(80,27)
	
print(pressure_3D)






	#print(pressure_3D[i,:,:])
=======
# inputs: salinity, temperature, pressure in form of netcdf file

>>>>>>> 3ea6b141428d75ef84a8447b9d02e3430e6e9b3c
