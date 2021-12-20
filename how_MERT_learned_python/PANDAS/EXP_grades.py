# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")

notlar.columns =["isim","soyisim","ssn",
                 "test1","test2","test3","test4",
                 "final","harfnotu"]
print(notlar)
print(notlar.head())
print(notlar.tail())
print(notlar["isim"])

print(notlar.iloc[2]) # integer location
print(notlar.loc[2]) # normal location
print(notlar[1:5])