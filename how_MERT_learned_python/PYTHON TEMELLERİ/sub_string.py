# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:44:57 2020

@author: ERTURK
"""


mesaj = "merhaba dünya"

print(mesaj[:5]) #print 0 and 1th unit

print(mesaj[5]) #see as char array and print unit 2 "r"

subString= mesaj[9:12] #9th 10th 11th unit

print(subString)

##  length
print(mesaj[len(mesaj)-3:len(mesaj)])#print last 3 char


## replace characters
print(mesaj)
print(mesaj.replace("ü","u"))
print(mesaj.replace("dü",""))#removes 



## split ve strip

bilgi="mert;ertürk;22;izmit"
bilgiAyrık=bilgi.split(";")## default splits at "space"

print (bilgiAyrık)
FirstElement=bilgi.split(";")[0]
print(FirstElement)


örnek="     bişiler bişiler mert ertürk  ".strip()# gets rid of misc spaces
print(örnek)

