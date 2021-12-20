import numpy as np

import matplotlib.pyplot as plt

from numpy.fft import fft


#Time domain frequency
f=50
fs=2000

n= np.arange(200) # 5 cycle of 50hz for Ts=1/2000
                  #200 sample = 0.1 second= 5*0.02 second

y= 4*np.cos(2*np.pi*f*n/fs) + 5 
t= n/fs # or n*Ts
plt.plot(t,y)
plt.grid()



#FFT
plt.figure()

vector=fft(y)
M=len(vector) # M is the number of samples 
k=np.arange(M) # K is the iterations from 0 to 200 (0 to 2*pi)

fr=k*fs/M    # fr/fs == k/M

plt.stem(fr,abs(vector/M))

