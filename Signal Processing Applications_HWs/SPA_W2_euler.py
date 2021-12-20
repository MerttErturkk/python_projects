# -*- coding: utf-8 -*-
"""   Sat Feb 27 12:11:49 2021   @author: ERTURK
"""


import numpy as np

import matplotlib.pyplot as plt

fs=60  # sampling frequency

n=np.arange(fs)

fr=3  # real frequency

euler= np.exp(1j*2*np.pi*fr*(n/fs))



plt.plot(np.real(euler),label="real")
plt.plot(np.imag(euler),"r",label="complex")
 
plt.ylim(-2,2)

plt.grid(True)
plt.legend(loc="lower right")

