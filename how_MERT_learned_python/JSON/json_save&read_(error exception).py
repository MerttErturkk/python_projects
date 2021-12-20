# -*- coding: utf-8 -*-
"""   Thu Jun 25 23:48:20 2020   @author: ERTURK
"""


import json

# Load the username, if it has been stored previously. 
#  Otherwise, prompt for the username and store it. 

filename = 'username.json' 
try:
    with open(filename) as f_obj:
        username =json.load(f_obj)
except FileNotFoundError:
    #if it is not given already ask for it instead of showing ERROR.
    username =input("What is your name? ")
    with open(filename,"w") as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username+" !")
else:
    print("Welcome back, "+username +" !")