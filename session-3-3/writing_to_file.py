

for i in range(0,10):
	for j in range (0,10):
		for k in range(0,10):
			print(i,j,k)

from netCDF4 import Dataset
import numpy as np 
import seawater as sw

dataset = Dataset(r"/Users/brownscholar/Documents/Dataset/dataset-armor-3d-rep-weekly_1574699840388.nc")
 
pressure = dataset['depth']
temperature = dataset['to']
salinty = dataset['so']

 # print(temperature.shape)
 # print(salinty.shape)
 # print(pressure.shape)

#
#second step: maket the pressure data 3 dimensional

pressure_3D = np.zeros((31,80,27))

layer1 = np.repeat(10,80*27).reshape(80,27)

#layer2 = np.repeat(20,80*27).reshape(80,27)


density_file = open('density_file.txt',"w")




salinty

#time1 = density_file[0,:,:,:]

for i in range(0,31):
	for j in range(0,80):
		for k in range(0,27):
			time1[i,j,k]

density_file = open('density_file.txt',"w")
for i in range(0,31):
	for j in range(0,80):
		for k in range(0,27):
			denisty_file.write(str(time1[i,j,k]))
denisty_file.close()


#for i in pressure[:]:
	#print(np.repeat(i,80*27).reshape(80,27))

	
#for i in range(0,31):
	# print(np.repeat(pressure[i],80*27).reshape((80,27)))
	# print(pressure_3D[i,:,:])
	# print(np.repeat)

for i in range(0,31):
	pressure_3D[i,:,:] = np.repeat(pressure[i],80*27).reshape(80,27)
	
#print(pressure_3D)

density = sw.dens(salinty[:],temperature[:],pressure_3D)
=======
from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1581373134952.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

print(pressure.shape)
print(temperture.shape)
print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

# for depth_level in pressure:
# 	print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
>>>>>>> 3ea6b141428d75ef84a8447b9d02e3430e6e9b3c
density = density-1000

print(density.shape)

<<<<<<< HEAD



	#print(pressure_3D[i,:,:])
=======
for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			print(i,j,k)
>>>>>>> 3ea6b141428d75ef84a8447b9d02e3430e6e9b3c
