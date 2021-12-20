# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:21:49 2020

@author: ERTURK
"""



"""
d= open("müşteriler.txt","r") # read

f = open("müşteriler1.txt","w") # write - yoksa "w" bu dosyayı
                                # oluşturur üzerine yazar.

g=open("müşteriler2.txt","a")# read/append anlamına gelir üzerine
                             # ekleme yapar anlamına geliyor.

h=open("müşteriler3.txt","x")# create sadece oluştur demek
                             # eğer dosya mevcutsa error verir.
"""
a=open("isimler.txt")
# print(a.read())
print("******")
print(a.readline())      # a.read bütün metni okuduğu için
print(a.readline())      # a.readline a okuyacak satır kalmaz.
print(a.readline(3))     #
print(a.readline())
print(a.readline(6))
print(a.readline())      #okuyacak satır kalmadı boş satır atar.


