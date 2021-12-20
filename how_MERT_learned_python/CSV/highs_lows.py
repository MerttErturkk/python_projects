# -*- coding: utf-8 -*-
import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Get dates, high and low temperatures from file.
filename ="sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row= next(reader)
    
    dates, highs,lows= [],[],[]
    for row in reader:
        current_date =datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)
        
        high =int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
    print(highs)
    
    # Prints headers.
    for index,column_header in enumerate(header_row):
        print(index,column_header)
        
#Plot data.
fig =plt.figure(dpi=128,figsize=(15,9))
plt.plot(dates,highs, c="red" ,alpha= 0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

#Format plot.
plt.title("Daily high and low temperatures, July 2018",fontsize =24)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.show()




