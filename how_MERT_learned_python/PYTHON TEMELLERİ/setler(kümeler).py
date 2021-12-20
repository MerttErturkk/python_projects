# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


""""
Set = Küme

 liste ve tuple dan daha performanslıdır.
 Tüm elemanlar eşsizdir ve tekrar edilmezler.
 """
 
 
 
 
my_set={1,(1,2),"yaho"}
print(my_set)

for bişeyler in my_set:
    print(bişeyler)
 
print("yaho" in my_set) ## True ya da false sonuç verir

if 1 in my_set:
    print("listemizde 1 var paşam rahat")


my_set.add("yeni string")# yeni eleman ekler
print(my_set)

my_set.update([123,"paşam",()]) #bir liste dolusu eleman ekleyebilir
print(my_set)
print(len(my_set))

my_set.remove("paşam")# elementi çıkar (bulamazsa error verir)
my_set.discard("paşam") # eğer böyle bi element varsa çıkar

x=my_set.pop() # kendi belirlediği son elemanı siler(rasgele)
y=my_set.clear()
print(y)
del y ## y diye bi variable artık yok


"""
Birleşim(UNION) kesişim(INTERSECTION) fark(DIFFERENCE) farklar toplamı(SYMMETRIC DIFFERENCE) kümeleri
"""
A={1,2,3,4}
B={3,4,5,6}
C=A|B
D=A&B
E=A-B
F=A^B
print(C)
print(D)
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
