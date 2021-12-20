# -*- coding: utf-8 -*-

import numpy as np




a= np.arange(10)

b=a 
""" 
b anın kopyası değildir aynı objeyi refere eder.
a yada b üzerinde yapılacak değişiklik ötekini etkiler.
bu yüzden bağımsız kopya oluştururuz.
"""
c= a.copy()
print(a)
print(b)
print(c)

print("\n")

c[0]= 1000
print(a)
print(b)
print(c)


"""
aynı verinin farklı şekilleriyle çalışmak isteyebiliriz.
view ile değerler aynıdır fakat şekil bağımsızdır.
"""
print("\n")

d=a.view()
print(a)
print(d)

print("\n")

d[0]=250
d.shape=2,5

print(a)
print(d)

a[0]=123

print(d)