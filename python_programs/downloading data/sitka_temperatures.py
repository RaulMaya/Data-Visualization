import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_2 = 'data/sitka_weather_2018_simple.csv'
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    dates, highs, lows = [], [], []
    
    for x in reader:
        high = round(((int(x[5]) - 32) * (5/9)),0)
        date = datetime.strptime(x[2], '%Y-%m-%d')
        low = round(((int(x[6]) - 32) * (5/9)),0)
        highs.append(high)
        lows.append(low)
        dates.append(date)


plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.plot(dates, highs, c='crimson', alpha=0.6)
ax.plot(dates, lows, c='turquoise', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='royalblue', alpha=0.2)

ax.set_title('Daily high and low temperatures of 2018', fontsize = 20)
ax.set_xlabel('Date', fontsize = 14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°C)', fontsize = 14)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()
fig.savefig('../../outputs/downloading data/sitka_temp.png', bbox_inches = 'tight')