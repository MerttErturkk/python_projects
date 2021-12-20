# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:30:50 2020

@author: ERTURK
"""





numbers = [6,4,4,3,1,2,2,1,1]
şehirler=["Ankara","İstanbul","İzmir"]




#######
doplam=0
for val in numbers:
    doplam=doplam+val
    
print("toplamın",doplam)





########
for sayı in numbers:
    print(sayı)
    
    
    
    
    
#####
for sayı in numbers:
      if sayı==4:
          print("dördümüz var")
      if sayı !=4:
          print("bu dört değil")
    
 
    
    
    
#####
for şehir in şehirler:
    print(şehir + " için kod= "+ şehir[0:3])