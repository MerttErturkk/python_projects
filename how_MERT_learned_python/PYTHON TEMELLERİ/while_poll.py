# -*- coding: utf-8 -*-
"""   Tue Jun 23 17:03:42 2020   @author: ERTURK
"""


responses = {}

# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response =input("which mountain would you like to climb someday?")
    #then we add  name and response to the list
    responses[name] = response
    repeat = input("Would you like to let another person respond? (Y or N)")
    if repeat=="N":
        polling_active=False

#polling is now complete
print("\n------Poll Results-------")
for name,response in responses.items():
    print(name +" would like to climb " +response + ".")