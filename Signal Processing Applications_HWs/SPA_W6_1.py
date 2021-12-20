# -*- coding: utf-8 -*-
"""   Thu Apr  1 20:32:59 2021   @author: ERTURK
"""


import numpy as np
from numpy import sin,pi
from numpy.fft import fft
import matplotlib.pyplot as plt



fs=100
n=np.arange(10*fs)
t=n/fs
x=sin(2*pi*t**2 + 10*pi*t)
#plt.plot(t,x)

###########################################
for m in range(1,11):
    indices= np.arange((m-1)*100,m*100) #window length = 100

    winX=x[indices]
    #plt.plot(indices,winX)

    plt.plot(abs(fft(winX)),label=str(m))
   
    plt.xlim(0,50)
    
plt.legend()    
######################################  
nWin = 100
plt.figure()
plt.specgram(x,NFFT= nWin,Fs=100,noverlap=50)