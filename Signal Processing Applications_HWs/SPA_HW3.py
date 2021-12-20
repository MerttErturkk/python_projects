# -*- coding: utf-8 -*-
"""

@author: Guray
"""

# EE0813 Signal Processing Applications
# Homework 3


import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

"""
A continuous time signal:
x(t) = cos(120*pi*t) + sin(440*pi *t)
is sampled at fs = 2000 Hz.
"""

# - Generate 500 samples of this signal

M = 500.
fs = 2000.
n = np.arange(M)
x = np.cos(120*np.pi*n/fs) + np.sin(440*np.pi*n/fs)

# - Calculate the non-zero FFT bins by hand.
# - Verify your previous answer via plotting norm of fft of x(n) versus FFT bins (k values).

fftx = abs(fft(x))
k = np.hstack((np.arange(M/2 + 1),np.arange(-M/2 + 1,0)))

plt.figure(1)
plt.plot(k,fftx)
plt.title("FFT magnitude")
plt.xlabel("FFT bins")
plt.grid(True)

# - What are the frequencies of the components?, calculate by hand.
# - Verify your previous result by plotting norm of fft of x(n) versus freal (real frequencies).
# - Replot the norm of fft by normalizing (dividing it)  by 500.

freal =k*fs/M 
plt.figure(2)
plt.plot(freal, fftx/M)
plt.title("FFT magnitude")
plt.xlabel("Frequency (Hz)")
plt.grid(True)

# If we produce a new signal by
# y(n) = x(n) - 2
# what's going to differ in plot of norm of fft of y(n) ? Answer this question by plotting the norm of fft of y(n)

y = x + 2
ffty = abs(fft(y))
plt.figure(4)
plt.plot(freal, ffty/M)
plt.title("FFT magnitude of y(n)")
plt.xlabel("Frequency (Hz)")
plt.grid(True)
