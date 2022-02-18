from dice import Side

# Creating a D6
die = Side(6)

# Make some rolls, and store the results
results = []
for ind_roll in range(200):
    result = die.roll()
    results.append(result)
print(results)