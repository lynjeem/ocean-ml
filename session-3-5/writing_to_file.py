from netCDF4 import Dataset
import numpy as np 
import seawater as sw

dataset = Dataset(r"/Users/brownscholar/Documents/Dataset/dataset-armor-3d-rep-weekly_1574699840388.nc")
 
pressure = dataset['depth']
temperature = dataset['to']
salinty = dataset['so']

(temperature.shape)
(salinty.shape)
(pressure.shape)

#
#second step: maket the pressure data 3 dimensional

pressure_3D = np.zeros((31,80,27))

#layer1 = np.repeat(10,80*27).reshape(80,27)

#layer2 = np.repeat(20,80*27).reshape(80,27)


	
# for i in range(0,31):
# 	(np.repeat(pressure[i],80*27).reshape((80,27)))


for i in range(0,31):
	pressure_3D[i,:,:] = np.repeat(pressure[i],80*27).reshape(80,27)
	

density = sw.dens(salinty[:,:,:,:],temperature[:,:,:,:],pressure_3D)

print(density.shape)

#date1 = density[118,:,:,:]
date1 = density
#print(date1)


# density_file = open('density_file.txt',"w")
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(density[i,j,k])+'\n')
# 			print(density[i,j,k])
# density_file.close()
		
#denisty_file.write(str(denisty[i,j,k]))

# density_file_1 = open('density_file.txt',"w")
# for i in range (0,1356):
# 	for j in range(0,31):
# 		for k in range(0,80):
# 			for l in range(0,27):
# 				density_file_1.write(str(density[i,j,k,l])+'\n')
# density_file.close()



# file_titles = []

# file_content = []

for i in range (0,1356):
	timefile = open("file_"+str(i)+".txt","w")
	for j in range(0,31):
		for k in range(0,80):
			for l in range(0,27):
				timefile.write(str(density[i,j,k,l])+'\n')
	timefile.close()








