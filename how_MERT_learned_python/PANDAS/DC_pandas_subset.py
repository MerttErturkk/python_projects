# -*- coding: utf-8 -*-
"""   Wed Jun 16 19:17:39 2021   @author: ERTURK
"""



names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


import pandas as pd
import numpy as np

my_dict={"country":names,"drives_right":dr,"cars_per_cap":cpc}

cars = pd.DataFrame(my_dict)

# =============================================================================
# 
# =============================================================================

# =============================================================================
#We subset cars by using "drives right" bool
sel = cars[cars['drives_right']]

print(sel)


print("\n\n##################\nCarmaniac countries\n#####################")
#FOR COUNTRIES THAT HAVE MORE THAN 500 CAR PER 1000
#BOOL
car_maniac = cars[cars["cars_per_cap"]>500]

print(car_maniac)





print("\n100<cars<500\n")
medium = cars[np.logical_and(cars["cars_per_cap"]>100 , cars["cars_per_cap"]<500)]
print(medium)



# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = str(cars.loc[lab,"country"]).upper()


# Print cars
print(cars)