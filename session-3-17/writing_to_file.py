from netCDF4 import Dataset
import numpy as np 
import seawater as sw
import datetime as td
import tricubic
#import interpolate

dataset = Dataset(r"/Users/brownscholar/Documents/Dataset/dataset-armor-3d-rep-weekly_1574699840388.nc")
 
pressure = dataset['depth']
temperature = dataset['to']
salinty = dataset['so']
latitude = dataset['latitude']
longitude = dataset['longitude']
time = dataset['time']
geo = dataset['zo']

(temperature.shape)
(salinty.shape)
(pressure.shape)
(time.shape)

def interp(startgrid):
	num_depths = 30 
	z_step = 10 
	depth_list = [10, 20, 30, 50, 75, 100, 125, 150, 200, 250, 300, 400]

	new_depth = np.arange(z_step,(num_depths+1)*z_step,z_step) 
	new_depth_index = []
	left = 0
	right = 1
	for i in range(0,len(new_depth)):
		target_value = new_depth[i]
		if target_value > depth_list[right]:
			right += 1
			left +=1
		left_value = depth_list[left]
		right_value = depth_list[right]
		a = target_value-left_value
		b = right_value-left_value
		new_index = a/b+left
		new_depth_index.append(new_index)
		#start grid is shape lat,lon,depth
		lat = startgrid.shape[1]
		lon = startgrid.shape[2]
		depth = startgrid.shape[0]

	interp_grid = np.zeros((len(new_depth_index),lat,lon))
	ip = tricubic.tricubic(list(startgrid),[depth,lat,lon])

	for i in range(0,lat):
		for j in range(0,lon):
			for k in range(0,len(new_depth_index)):
				res = ip.ip([new_depth_index[k],i,j])
				interp_grid[k,i,j] = res

	return interp_grid


pressure_3D = np.zeros((31,80,27))

#layer1 = np.repeat(10,80*27).reshape(80,27)

#layer2 = np.repeat(20,80*27).reshape(80,27)


	
# for i in range(0,31):
# 	(np.repeat(pressure[i],80*27).reshape((80,27)))


for i in range(0,31):
	pressure_3D[i,:,:] = np.repeat(pressure[i],80*27).reshape(80,27)
	

density = sw.dens(salinty[:,:,:,:],temperature[:,:,:,:],pressure_3D)
density = density -1000
print(density.shape)

#date1 = density[118,:,:,:]
date1 = density
#print(date1)

geo = geo[:] * 100


# density_file = open('density_file.txt',"w")
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(density[i,j,k])+'\n')
# 			print(density[i,j,k])
# density_file.close()
		
#denisty_file.write(str(denisty[i,j,k]))

# density_file_1 = open('density_file.txt',"w")
# for i in range (0,30:
# 	for j in range(0,31):
# 		for k in range(0,80):
# 			for l in range(0,27):
# 				density_file_1.write(str(density_at_time[j,k,l])+'\n')
# density_file.close()



# file_titles = []

# file_content = []

#for i in range (0,1356):


start_date = td.date(1950,1,1)
#for i in time[:]:
    #hours = td.timedelta(hours = int[i])

for i in range(0,1356):
	hours = td.timedelta(hours = int(time[i]))
	after = start_date + hours
	date = after.strftime("%y") + after.strftime("%m") + after.strftime("%d")
	density_time = open('/Users/brownscholar/documents/Densityfiles' + 'density' + str(date) + '.gr ', "w")
	density_time.write("\t30\n\t80\t27")
	density_at_time = interp(density[i,: 12,:]) 
	geo_time = open('/Users/brownscholar/documents/Geofiles' + 'geo' + str(date) + '.gr', "w")
	geo_time.write("\t30\n\t80\t27")
	geo_at_time = interp(geo[i,: 12 ,:])
	for j in range(0,30):
		for k in range(0,80):
			for l in range(0,27):
				density_at_time.write(str(density_at_time[j,k,l])+'\n')
				geo_at_time.write(str(ge0_at_time[j,k,l])+ '\n')
	density_file.close()
 










