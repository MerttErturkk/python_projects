
# Print cars
print(cars)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']


# Specify row labels of cars
cars.index= row_labels

# Print cars again
print(cars)
print(cars.loc[["RU","MOR"],["country","drives_right"]])


print("\n\n\n\n")
# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:,["cars_per_cap","drives_right"]])