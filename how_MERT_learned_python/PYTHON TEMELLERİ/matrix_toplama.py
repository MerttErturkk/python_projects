# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:08:05 2020

@author: ERTURK
"""
a=[[1,3,5],[2,4,1],[1,5,7]]
b=[[3,3,4],[2,4,1],[3,5,4]]

sonuc=[[0,0,0],[0,0,0],[0,0,0]]

# sonuc[0][0]=a[0][0]+b[0][0]
# sonuc[0][1]=a[0][1]+b[0][1]
# sonuc[0][2]=a[0][2]+b[0][2]
# sonuc[1][0]=a[1][0]+b[1][0]
# sonuc[1][1]=a[1][1]+b[1][1]   # amelelelik yapmak yerine döngüye sok
# sonuc[1][2]=a[1][2]+b[1][2]
# sonuc[2][0]=a[2][0]+b[2][0]
# sonuc[2][1]=a[2][1]+b[2][1]
# sonuc[2][2]=a[2][2]+b[2][2]

for i in range(len(a)):
    for j in range(len(b)):
        sonuc[i][j]=a[i][j]+b[i][j]
        
        



# import numpy as np                      # numpy kullanırsan yukaridaki
# x=np.matrix([[1,3,5],[2,4,1], [1,5,7]]) # kodların hiçbirini kullanmana
# y=np.matrix([[3,3,4],[2,4,1],[3,5,4]])  # gerek kalmaz.

# c= x+y
# print(c)