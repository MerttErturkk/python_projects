# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,4)))

print(a.shape)

b= a.ravel() # flattens the array
print(b.shape)

c=a.reshape(2,6)
d=a.reshape(2,-1) # -1 >> auto-column count
print(c.shape)


print(c)
print("\n")
print(c.T) # transpose of c