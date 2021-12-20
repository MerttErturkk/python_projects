# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:13:13 2020

@author: ERTURK
"""
lights=["red","yellow","green"]
currentLight= lights[0] # initially "red
if currentLight == "red":
    print("STOP")
if currentLight=="yellow":
    print("READY!")
if currentLight== "green":
    print("GO!")

""" 
ikinci ve üçüncü "if" "elif" de olabilirdi, 
fakat sadece sonuncu "else" olabilir. 
"""