# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:16:17 2021

@author: ERTURK
"""
import shelve
#%%

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()


#%%
shelfFile = shelve.open('mydata')
print(type(shelfFile))
cats=shelfFile['cats']
cats[1]="mister lobaloba"
shelfFile['cats'] = cats

shelfFile.close()
#%%
shelfFile = shelve.open("mydata")
print(list(shelfFile.keys()))
print(list(shelfFile.values()))


#%%  store variables to a .py file
###  using pretty printing

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# pprint.pformat(cats)

fileObj = open("myCats.py","w")
fileObj.write("cats = " + pprint.pformat(cats)+"\n")

fileObj.close()

#%%
import myCats
print(myCats.cats)
print(myCats.cats[0]["name"])