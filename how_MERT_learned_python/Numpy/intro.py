# -*- coding: utf-8 -*-
"""   Sat Sep 12 22:36:36 2020   @author: ERTURK
"""

import numpy as np

a= np.arange(15)

print(a)

print(type(a))


print("\n")



b=a.reshape(3,5) # matrix form

print(b)

print("\n")


print(b.shape)
print(b.ndim)