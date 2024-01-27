import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

#Download the data set
dset = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/SRTMGL1_NC.003_Data/N21E039.SRTMGL1_NC.nc')

#use a breaking point to stop and explore vars in file
pdb.set_trace()

#get the elevation model var
DEM = np.array(dset.variables['SRTMGL1_DEM'])

pdb.set_trace()

dset.close()

#make a figure 
plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label('Elevation (m asl)')
#plt.show()
plt.savefig('assignment_1.png', dpi=300)
