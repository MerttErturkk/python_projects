# -*- coding: utf-8 -*-

import pandas as pd

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)



data2= [["mert",22,"istanbul"],["engin",33,"ankara"]]
df2=pd.DataFrame(data2,columns=["isim","yaş","şehir"],index=[1,2])
print(df2)

print("\n")


data3={"isim":["ahmet","mehmet"],
       "yaş":[58,60],
       "şehir":["istanbul","istanbul"]}
df3=pd.DataFrame(data3,columns=["isim","yaş","şehir"],index=[1,2])
print(df3["yaş"])
"""
print(df3)
print("\n")
del df3["şehir"] #  df2.pop("şehir")
print(df3)
"""

print(df3.loc[2])

df4 =df3.append(df2)
print("\n")
print(df4)

#df4.head() ilk datayı verir
#df4.tail() son datayı verir.