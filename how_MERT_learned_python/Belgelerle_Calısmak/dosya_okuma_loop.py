# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:12:00 2020

@author: ERTURK
"""
a=open("isimler.txt")

print("******")

print(a.readline()) #ilk satırı okur



#########
# alttaki fonksiyon yazmada tek başına yeterli olur.
for l in a:      #geri kalan satırları loop olarak okur.
    print(l)
########  
    
###ÖRNEK 2
a.close() #dosyayla işimiz bitince kapatırız.


filetoappend= open("müşteriler.txt","w") #boş dosyayı aç "write"
filetoappend.write("engin") # ilk satıra "engin" yaz
filetoappend.write("\nsalih") #ikinci satıra "salih" yaz
filetoappend.close() # dosyayı kapatır

###ÖRNEK 3

### DOSYAMIZ VAR MI? EĞER VARSA SİLELİM.
import os

if os.path.exists("müşteriler.txt"):
    os.remove("müşteriler.txt")# dosyayı silip atar
    


##ÖRNEK 4
    #EĞER Bİ KLASÖR SİLMEK İSTERSEK
   # os.rmdir("empty") #remove directory
    