import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import tools

dset = xr.open_dataset('/Users/ranawail/Desktop/Course_Data/ERA5_Data/download.nc')

t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])
#converting the temp col from k to C and prep from m/h to mm/h
t2m = t2m - 273.15
tp = tp * 1000

#if the the data set has 4 dims, compute the mean across the second dim to simplify the data set
if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)
#create ts for temp and precp near resouvoire
df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:,3,2]
df_era5['tp'] = tp[:,3,2]
# plot ts

legend_labels = ["Temp [°C]", "Precp [mm]"]  # Labels for different data series if applicable

# Plotting the DataFrame
ax = df_era5.plot()

# Adding labels and title
ax.set_xlabel("Time")
ax.set_ylabel('Value')
ax.set_title("Wadi Murwani Climatology Time Series")

# Adding legend with labels if there are multiple data series
if len(legend_labels) > 1:
    ax.legend(legend_labels)

plt.savefig('asst6_rea_ts2.png', dpi=300)
#plt.show()


'''
# another way
#wadi Murwani location 22.174997, 39.583705
specific_latitude = 22.174997
specific_longitude = 39.583705
selected_location = dset.sel(latitude=specific_latitude, longitude=specific_longitude, method='nearest')

#time sereis plot
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(selected_location['time'], selected_location['t2m'], 'g-')
ax2.plot(selected_location['time'], selected_location['tp'], 'b-')

ax1.set_xlabel('Time')
ax1.set_ylabel('T [°C]', color='g')
ax2.set_ylabel('P [mm]', color='b')

fig.legend(["Temp", "Prec"])

#plt.show()

fig.savefig('asst6_rea_ts.png', dpi=300)
'''
#the annual preciptation
#first change to annual time step
annual_precip = df_era5['tp'].resample('YE').mean()*365.25
mean_annual_precip = np.nanmean(annual_precip)
print(mean_annual_precip)

#Potential evaporation
#the inputs
tmin = df_era5['t2m'].resample("D").min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values
lat = 21.25
doy = df_era5['t2m'].resample('D').mean().index.dayofyear
#compute PE
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)
#plot PE time series
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label='Potential Evaporation')
plt.xlabel('Time')
plt.ylabel('Potential evaporation (mm d−1)')
plt.savefig('asst6_EP_ts.png', dpi=300)
#plt.show()

#annual mean pe
print(pe)
pe_df = pd.DataFrame({'data': pe})
pe_df.index = pd.to_datetime(ts_index)
annual_pe = pe_df.resample('YE').mean()*24*365.25
mean_annual_pe = np.nanmean(annual_pe)
print(mean_annual_pe)

#lost water from resv
area_m = 1.6 * 1e6  #m^2
annual_pe_m = mean_annual_pe /1000 #m/y
lost_water = area_m * annual_pe_m
print(lost_water)
