#to do
from netCDF4 import Dataset
import numpy as np 
import seawater as sw 

dataset = Dataset(r"/Users/brownscholar/Documents/Dataset/dataset-armor-3d-rep-weekly_1574699840388.nc")

g_height = dataset['zo'][:]

print(g_height)