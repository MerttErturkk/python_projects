# -*- coding: utf-8 -*-
"""   Wed May  5 20:39:13 2021   @author: ERTURK
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
w = np.linspace(0,2*np.pi,100)

H= np.exp(1j*w)-np.exp(1j*0.4*np.pi)


plt.plot(w/np.pi,abs(H)) # or np.sqrt(H*np.conj(H))

plt.title("NORM OF H(e^jw)")
plt.grid()

#%%

from scipy.signal import freqz


b = [1,-2*np.cos(0.4*np.pi),1]

a=[0,0,1]

w,H = freqz(b,a)
