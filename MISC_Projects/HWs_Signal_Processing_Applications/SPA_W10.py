# -*- coding: utf-8 -*-
"""   Wed May  5 19:05:27 2021   @author: ERTURK
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import sounddevice as sd




#%% =============================================================================
# PART 1
# =============================================================================

fs = 500
t = np.arange(4*fs)/fs     # 2000 sample = 0 to 4 seconds
x = np.cos(2*np.pi*50.25*t)

fft_x1=abs(fft(x,500))
fft_x2=abs(fft(x,1000))
fft_x3=abs(fft(x,2000))


plt.figure(1) # resolution is 1hz
plt.plot(fft_x1)
plt.title("M = 500")

plt.figure(2)  # resolution is 0.5hz
plt.plot(fft_x2)
plt.title("M = 1000")

plt.figure(3)  # resolution is 0.25hz
plt.plot(fft_x3)  
plt.title("M = 2000")



#%% =============================================================================
# PART 2
# =============================================================================

fs = 8000

n = np.arange(4*fs)
t = n/fs
x = np.cos(2000*np.pi*t*(t+2))


#sd.play(x,8000)
plt.figure(4)
plt.specgram(x,NFFT = int(0.125*fs),noverlap = 500, Fs=8000)