# to do: 

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