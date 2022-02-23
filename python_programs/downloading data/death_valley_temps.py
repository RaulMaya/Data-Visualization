import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_2 = 'data/death_valley_2018_simple.csv'
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    dates, highs, lows = [], [], []
    
    for x in reader:
        date = datetime.strptime(x[2], '%Y-%m-%d')
        try:
            high = round(((int(x[4]) - 32) * (5/9)),0)
            low = round(((int(x[5]) - 32) * (5/9)),0)
        except ValueError:
            print(f"Missing data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)


plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.plot(dates, highs, c='orange', alpha=0.6)
ax.plot(dates, lows, c='skyblue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.2)

ax.set_title('Daily high and low temperatures of 2018\nin Death Valley, CA', fontsize = 20)
ax.set_xlabel('Date', fontsize = 14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°C)', fontsize = 14)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()
fig.savefig('../../outputs/downloading data/death_valley.png', bbox_inches = 'tight')