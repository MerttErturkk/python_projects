# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:27:57 2020

@author: ERTURK
"""


sayı1=int(input("sayı1 lütfen\n"))
sayı2=int(input("sayı2 lütfen\n"))
sayı3=int(input("sayı3 lütfen\n"))
liste=[sayı1,sayı2,sayı3]
liste.sort()
print("en büyük sayı",liste[-1])
# anlamsız ram kullanır

if sayı1>sayı2 and sayı1>sayı3:
    print("en baba sayı",sayı1)

elif sayı2>sayı1 and sayı2>sayı3:
    print("en baba sayı",sayı2)
else:
    print("en baba sayı",sayı3)
    