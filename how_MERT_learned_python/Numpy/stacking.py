# -*- coding: utf-8 -*-

import numpy as np

a=10* np.random.random((2,3))
b= np.floor(a)

c=10* np.random.random((2,3))
d= np.floor(c)


e=np.vstack((b,d)) # vertical stack


f=np.hstack((b,d)) # horizontal stack