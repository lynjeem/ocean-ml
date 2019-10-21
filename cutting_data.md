# Today we’re going to put a few things we’ve learned together and cut our data

Check out this beautiful beach in Bermuda: 
![bermuda :')](https://www.gotobermuda.com/sites/default/files/styles/hero/public/head-south-shore-horseshoe-bay-beach.jpg?itok=OBBhtfew)

#First a bit about our data: 
Review: We have been looking at sea_velocity_19930101.nc, which is one of many netcdf files downloaded from [here](http://marine.copernicus.eu.)This file contains the global horizontal and vertical velocities of the ocean, called ugos and vgos respectively.

We want to match that data to the data about carbon in the ocean
* This data comes from BIOS, which is the Bermuda Institute of Ocean Sciences.  
* The data we are interested in is called BATS, which stands for Bermuda Atlantic Time-series Study. 
* BATS has collected data on the physical, biological, and chemical properties of the ocean every month since before 1988. 
* BATS is **not** global, it covers  roughly this: 

<img src="https://raw.githubusercontent.com/madesai22/ocean-ml/master/images/BATS_data.png" width="400" height="450" />

