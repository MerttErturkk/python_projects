# -*- coding: utf-8 -*-

import numpy as np

a=np.arange(20,51,10)
b= a/2
c= b**2
d= 10*np.sin(a)
print(d<7)
print(a*b)
print(a@b) # matris çarpımı
print(a.dot(b)) # bu da matris çarpımı

e = np.ones((1,6))
f= np.zeros((2,4))


g=np.random.random((2,4))

h= np.sum(b)

i = np.min(a)

j = np.max(a)

k= np.sqrt(c)