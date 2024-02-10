import tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
from mpl_toolkits.axes_grid1 import make_axes_locatable

#ISD Data
df_isd =  tools.read_isd_csv('/Users/ranawail/geo_env/41024099999.csv')
#plot the data
df_isd.plot(title = "ISD data for Jeddah")
plt.savefig('asst3_isd.png', dpi=300)
plt.close()

#Heat index (HI) Calculation
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,  df_isd['TMP'].values)

df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)

max_hi = df_isd['HI'].max()
max_hi_date = df_isd['HI'].idxmax()

df_isd.loc[[max_hi_date]]

#HI using hourly data

daily_isd = df_isd.resample('D').mean()
#print(daily_isd.head(),daily_isd.tail() )
daily_isd['RH'] = tools.dewpoint_to_rh(daily_isd['DEW'].values,  daily_isd['TMP'].values)
daily_isd['HI'] = tools.gen_heat_index(daily_isd['TMP'].values, daily_isd['RH'].values)

#plot the hourly
fig1, ax1 = plt.subplots()
ax1.plot(daily_isd.index, daily_isd['HI'])
ax1.set_title('HI For Jeddah Using Daily Data')
ax1.set_xlabel('Time')
ax1.set_ylabel('Heat Index (HI)')
plt.savefig('asst3_daily.png', dpi=300)

# plot hourly HI time series
fig2, ax2 = plt.subplots()
ax2.plot(df_isd.index, df_isd['HI'])
ax2.set_title('HI For Jeddah Using Hourly Data')
ax2.set_xlabel('Time')
ax2.set_ylabel('Heat Index (HI)')
plt.savefig('asst3_hourly.png', dpi=300)

#SSP projection adjustment
# Adding 3 C to temp col
projected_isd = df_isd
projected_isd['TMP'] = projected_isd['TMP'] + 3
#recalculate HI
projected_isd['RH'] = tools.dewpoint_to_rh(projected_isd['DEW'].values,  projected_isd['TMP'].values)
projected_isd['HI'] = tools.gen_heat_index(projected_isd['TMP'].values, projected_isd['RH'].values)

max_hi_pro = projected_isd['HI'].max()
max_hi_date_pro = projected_isd['HI'].idxmax()

print(max_hi_pro, max_hi_date_pro)
print(df_isd.loc[[max_hi_date]])