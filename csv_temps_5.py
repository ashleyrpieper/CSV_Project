import matplotlib.pyplot as plt
import csv
from datetime import datetime

file_1 = open("death_valley_2018_simple.csv", "r")
file_2 = open("sitka_weather_07-2018_simple.csv", "r")

csv_file1 = csv.reader(file_1, delimiter = ",")
csv_file2 = csv.reader(file_2, delimiter = ",")

location_name = ''

header_row = next(csv_file1)

highs1 = []
lows1 = []
dates1 = []
highs2 = []
lows2 = []
dates2 = []

name_index = header_row.index('NAME')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
date_index = header_row.index('DATE')


for row in csv_file1:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(current_date)

for row in csv_file2:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)
    
fig, axs = plt.subplots(2,1)


plt.title("Daily Temps in Death Valley 2018", fontsize=16)
plt.plot(dates1, highs1, color = 'red', alpha=0.5)
plt.plot(dates1, lows1, color = 'blue', alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.2)
plt.title("Daily Temps in Sitka 2018", fontsize=16)
plt.plot(dates2, highs2, color = 'red', alpha=0.5)
plt.plot(dates2, lows2, color = 'blue', alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.2)
plt.xlabel("",fontsize=8)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis='both',which="major",labelsize=12)
fig.autofmt_xdate()


plt.show()