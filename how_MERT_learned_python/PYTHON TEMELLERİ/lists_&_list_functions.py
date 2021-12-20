# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:17:26 2020

@author: ERTURK
"""

mylist0=[]
mylist1=[1,"1",1.0] ## can be made of different types

mylist2=[1,[1,2,3],2,]## may include another list


mylist1.extend(mylist2) #mylist1in sonuna mylist2nin elemanlarını ekler
print(mylist1)
print(len(mylist1))

####

sınıf=["öğrenci1","öğrenci2","öğrenci3","öğrenci4"]
print(sınıf[1])
sınıf.append("öğrenci5")# ekle
print(sınıf[4])
sınıf.remove(sınıf[3])# çıkar 3. eleman
print(sınıf)

####
şehirler=list(("istanbul","ankara"))# list constructor
print(len(şehirler))
şehirler.clear() # empties the list
print(şehirler)
#####


listem=["1","2","2","2","3","3"]
print(listem)
print(listem.count("2")) # how many "2" exist in listem

listem.pop(0)# remove 0th element
print(listem)
listem.insert(1,"1")# add element as 1th element
print(listem)

listem.reverse() #reverses list indexes
print(listem)



listem.sort()# alfabetik sıralar
print(listem)
listem.reverse()#tersinden alfabetik sıralar

"""
eğer dersem ki 
şehirler=şehirler1 listesi
ben bu koddan sonra şehirler üzerinde değişiklik yada şehirler1 üzerinde yaparsam
iki liste üzerinde değişiklil yapmış olurum. Listeler birbirlerini referans alamazlar.(KISAYOL GİBİ DAVRANIR)
ancak;
şehirler3=şehirler.copy() olduğunda şehirler üzerinde yapılan değişiklik şehirler3ü etkilemez.(GERÇEK Bİ KOPYA OLUR)
Bu durum tam tersi için de geçerlidir.
"""



