# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:14:05 2020

@author: ERTURK
"""



"""
FONKSIYONLARA GIRIŞ
"""

def selamver(isim="ziyaretçi",soyisim="efendi"): # Konsola selamver() yazıp ,
                                 # çağırırsan ziyaretçi efendiyi selamlar
    print("merhaba",isim,soyisim)
 
a=input("isminiz nedir?\n")
selamver(a)    

def diküçgenalanhesapla(a,b):
    return a*b/2
diküçgenalanhesapla(2,3)# konsola a=diküçgenalanhesapla(2,3)
                        # dersem a yı a*b/2 olarak atar