# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



###############
"""
Tuple listelere benzer fakat içerisindeki elementler ile oynanamaz bu 
veri yapısı performansı arttırır.
tuple = READ ONLY
"""
#####
my_tuple=(1,(1,3,4),[4,56,7],3)
my_tuple1=(1,"elem",1.0)
print(my_tuple1)
print(str(type(my_tuple))+ " " + str(len(my_tuple)))
print(my_tuple[2])
print(my_tuple[-2])



isim=("mert",)## virgül koymazsak tuple yerine string sayılır
isim1=("mertz")
print(str(isim) +str(type(isim)))
print(type(isim1))
