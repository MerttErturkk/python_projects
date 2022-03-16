import numpy as np

import matplotlib.pyplot as plt

from numpy.fft import fft

M=1000

n=np.arange(M)


#proof of following two signals are the same
x=np.exp(1j*0.02*np.pi*n)
u10=np.exp(1j*2*np.pi*n*10/M)


plt.stem(abs(fft(x)))
plt.title("Magnitute of FFT(x)")