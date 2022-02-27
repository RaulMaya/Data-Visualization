import json

path  = 'data/eq_data_1_day_m1.json'
with open(path) as j:
    earthquakes = json.load(j)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as j:
    json.dump(earthquakes, j, indent=4)

print(len(earthquakes['features']))