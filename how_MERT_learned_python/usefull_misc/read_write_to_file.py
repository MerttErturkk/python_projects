# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:20:54 2021

@author: ERTURK
"""

helloFile = open(r'C:\Users\ERTURK\Desktop\hello.txt',"r")
# print(helloFile.readlines())
# print(helloFile.read())
helloFile.close()
#%% overWrite
helloFile = open(r'C:\Users\ERTURK\Desktop\hello.txt',"w")
helloFile.write('Hello world1!\n')
helloFile.close()
#%% append
helloFile = open(r'C:\Users\ERTURK\Desktop\hello.txt',"a")
helloFile.write('Hello world2!\n')
helloFile.close()