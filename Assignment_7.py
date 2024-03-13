#import panoply
import netCDF4 as nc
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


#average the the three years
import netCDF4 as nc
import numpy as np

#ET
with xr.open_dataset('/Users/ranawail/geo_env/totalET_annualtot.nc', decode_times=False) as ds:
    # Calculate the average along the time dimension
    data_average = ds['totalET_annualtot'].mean(dim='time')

    # Save the averaged data to a new NetCDF file
    data_average.to_netcdf('averaged_ET.nc')

#Runoff
with xr.open_dataset('/Users/ranawail/geo_env/runoff_annualtot.nc', decode_times=False) as ds:
    # Calculate the average along the time dimension
    data_average = ds['runoff_annualtot'].mean(dim='time')

    # Save the averaged data to a new NetCDF file
    data_average.to_netcdf('averaged_runoff.nc')

# calculation the water balance
# Load the NetCDF files
precipitation = xr.open_dataset('/Users/ranawail/geo_env/Precipitation_annualtot.nc',decode_times=False )['Precipitation_annualtot']
evapotranspiration = xr.open_dataset('/Users/ranawail/geo_env/totalET_annualtot.nc', decode_times=False)['totalET_annualtot']
discharge = xr.open_dataset('/Users/ranawail/geo_env/discharge_annualtot.nc', decode_times=False)['discharge_annualtot']

# adjust the units
time_interval_seconds = 365 * 24 * 60 * 60
area_of_grid_cell = 55000*55000  #0.5 degree =55 km
# converting units from m to m^3
precipitation = precipitation * area_of_grid_cell
evapotranspiration = evapotranspiration * area_of_grid_cell
#convert from m^3/s to m^3
discharge = discharge * time_interval_seconds
# Calculate the water balance without storage change
water_balance = precipitation - evapotranspiration - discharge

# Optionally, you can calculate the mean water balance over time
mean_water_balance = water_balance.mean(dim='time')

# Save the result to a new NetCDF file
mean_water_balance.to_netcdf('water_balance_avg.nc')

grid_cell_precipitation = precipitation.isel(lat=5, lon=5)
grid_cell_evapotranspiration = evapotranspiration.isel(lat=5, lon=5)
grid_cell_discharge = discharge.isel(lat=5, lon=5)

# Calculate the water balance without storage change for the selected grid cell
grid_water_balance = grid_cell_precipitation - grid_cell_evapotranspiration - grid_cell_discharge

# Plot the water balance for the selected grid cell
grid_water_balance.plot.line()

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Water Balance')
plt.title('Water Balance for Grid Cell (lat=5, lon=5)')

# Show the plot
plt.show()

print(precipitation.values)

