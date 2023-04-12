#put python script here
import xarray as xr
import glob
import numpy as np


### i put 0s to nans in replace0s.ipynb
def make_yearlist(yrst, yrend):
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    baseDir = '/gpfs/home/mep22dku/scratch/NanooseObs/SS1500-extract-nans/'
    for i in range(0,len(yrs)):
        ty = yrs[i]
        for m in range(1,13):
            if m < 10:
                tm = f'0{m}'
            else:
                tm = m
            tstr = f'y{ty}m{tm}'
            tfi= f'{baseDir}/*{tstr}*.nc'
            t2 = glob.glob(tfi)
            # print(t2)
            ylist.append(t2[0])
    return ylist

st = 1980; en = 1989
tylist = make_yearlist(st, en)
tdat = xr.open_mfdataset(tylist)
tdat_daily = tdat.resample(time_counter = 'D').mean().mean(dim = ['y','x']) ### this needs to change to be weighted
tdat_daily.to_netcdf(f'SS1500_ts_timeseries_{st}-{en}.nc')

st = 1990; en = 1999
tylist = make_yearlist(st, en)
tdat = xr.open_mfdataset(tylist)
tdat_daily = tdat.resample(time_counter = 'D').mean().mean(dim = ['y','x']) ### this needs to change to be weighted
tdat_daily.to_netcdf(f'SS1500_ts_timeseries_{st}-{en}.nc')

st = 2000; en = 2009
tylist = make_yearlist(st, en)
tdat = xr.open_mfdataset(tylist)
tdat_daily = tdat.resample(time_counter = 'D').mean().mean(dim = ['y','x']) ### this needs to change to be weighted
tdat_daily.to_netcdf(f'SS1500_ts_timeseries_{st}-{en}.nc')

st = 2010; en = 2018
tylist = make_yearlist(st, en)
tdat = xr.open_mfdataset(tylist)
tdat_daily = tdat.resample(time_counter = 'D').mean().mean(dim = ['y','x']) ### this needs to change to be weighted
tdat_daily.to_netcdf(f'SS1500_ts_timeseries_{st}-{en}.nc')