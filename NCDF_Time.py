# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import os
import netCDF4
import numpy as np
import pandas as pd

os.chdir("C:/Calluna/Projekt/CementaSlite/Copernicus_BaltFys")
os.listdir()

file_in=netCDF4.Dataset('dataset-bal-analysis-forecast-phy-dailymeans_1657797649987.nc', "r", format="NETCDF4")

tname = "time"

nctime = file_in.variables[tname][:]

t_unit = file_in.variables[tname].units

try :

    t_cal = file_in.variables[tname].calendar

except AttributeError : # Attribute doesn't exist

    t_cal = u"gregorian" # or standard

datevar = []

#netCDF4.num2date(times, units)

datevar.append(netCDF4.num2date(nctime,units = t_unit,calendar = t_cal))

df = pd.DataFrame.from_records(datevar)
df.to_csv("phyDaily_dates.csv", sep = ',', encoding = "UTF-8")