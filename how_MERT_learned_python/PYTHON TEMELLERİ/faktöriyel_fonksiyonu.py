# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:25:15 2020

@author: ERTURK
"""
def factor(a):
    faktör=1
    if a<0:
        print("negatif sayının faktöriyali olmaz")
    elif a==0:
        print(faktör)
    else:
        for i in range(1,int(a)+1):
            faktör=faktör*i
        print(faktör)
      

