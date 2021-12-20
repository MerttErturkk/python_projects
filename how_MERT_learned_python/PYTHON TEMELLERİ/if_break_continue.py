# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:09:56 2020

@author: ERTURK
"""




"""
şehirler=["ankara","istanbul","izmir"]

for şehir in şehirler:
    print(şehir+" için kod " +şehir[0:3])
    del şehir
"""


#### ankara olduğunda hiçbirşey yapma devam et (CONTINUE)

# şehirler=["ankara","istanbul","izmir"]

# for şehir in şehirler:
#     if şehir =="ankara":
#         continue
#     print(şehir+" için kod " +şehir[0:3])
    
    
    
""" 
 
 ###istanbul olduğunda meraba yaz loopu bitir (BREAK)
 

 
şehirler=["ankara","istanbul","izmir"]

for şehir in şehirler:
    if şehir =="istanbul":
        print("meraba")
        break
    print(şehir+" için kod " +şehir[0:3])  
    
"""
şehirler=["ankara","istanbul","izmir"]

for şehir in şehirler:
    if şehir !="ankara":
        print("bize heryer ankaradır")
        continue
    print(şehir+" için kod " +şehir[0:3])