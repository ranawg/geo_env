import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
from mpl_toolkits.axes_grid1 import make_axes_locatable



#Download the data set
dset = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')

pdb.set_trace()

dset_hist = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')

# Calculate the mean tempreture for 1850-1900
mean_temp_1850_1900 = np.mean(dset_hist['tas'].sel(time=slice('18500101', '19001231')), axis=0)
plt.imshow(mean_temp_1850_1900)
cbar = plt.colorbar()
cbar.set_label('Temperature (K)')
plt.title('Historical Temperatures: 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig('asst2fig_mt1850.png', dpi=300)
#mean temp for each scenario
#ssp119
dset_ssp119 = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
mean_temp_ssp119 = np.mean(dset_ssp119['tas'].sel(time=slice('20710116', '21001216')), axis=0)

#ssp245
dset_ssp245 = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
mean_temp_ssp245 = np.mean(dset_ssp245['tas'].sel(time=slice('20710116', '21001216')), axis=0)

#ssp585
dset_ssp585 = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')
mean_temp_ssp585 = np.mean(dset_ssp585['tas'].sel(time=slice('20710116', '21001216')), axis=0)

#plot them on one plot
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
cmap = 'coolwarm'
vmin, vmax = 200, 300
#adding each map to the axis
mean_temp_ssp119.plot(ax=axs[0], cmap=cmap, vmin=vmin, vmax=vmax)
axs[0].set_title('SSP119')

mean_temp_ssp245.plot(ax=axs[1], cmap=cmap, vmin=vmin, vmax=vmax)
axs[1].set_title('SSP245')

mean_temp_ssp585.plot(ax=axs[2], cmap=cmap, vmin=vmin, vmax=vmax)
axs[2].set_title('SSP585')
#title
fig.suptitle('Temperature Projections for 2071-2100')
# labels
for ax in axs:
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

plt.savefig('asst2fig_ssp.png', dpi=300)

# tempreture differnce
#SSP119
temp_diff_ssp119 = mean_temp_ssp119 - mean_temp_1850_1900
#SSP245
temp_diff_ssp245 = mean_temp_ssp245 - mean_temp_1850_1900
#SSP585
temp_diff_ssp585 = mean_temp_ssp585 - mean_temp_1850_1900

# plot them in one plot; specifications:
fig, axs = plt.subplots(1, 3, figsize=(20, 5), sharex=True, sharey=True)
cmap = 'coolwarm'
vmin, vmax = -2, 2
#adding each map to the axis
im1 = temp_diff_ssp119.plot(ax=axs[0], cmap=cmap, vmin=vmin, vmax=vmax)
axs[0].set_title('SSP119')

im2 = temp_diff_ssp245.plot(ax=axs[1], cmap=cmap, vmin=vmin, vmax=vmax)
axs[1].set_title('SSP245')

im3 = temp_diff_ssp585.plot(ax=axs[2], cmap=cmap, vmin=vmin, vmax=vmax)
axs[2].set_title('SSP585')
#title
fig.suptitle('Temperature Differences: SSP Projection vs. Historical ')
# labels
for ax in axs:
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

plt.savefig('asst2fig_diff_temp.png', dpi=300)
