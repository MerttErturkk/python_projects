# -*- coding: utf-8 -*-
"""
@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 5

from numpy import *
from matplotlib.pyplot import *

# - Generate 6 seconds of signal x with sampling rate of 48kHz.
fs = 48000.
t = arange(6*fs)/fs
x = np.sin(6000*np.pi*(1-np.cos(4*np.pi*t))+20000*np.pi*t)

# - using sounddevice module, listen what you have generated
from sounddevice import *
play(x,48000)

"""
- Plot 4 different spectrograms in a common figure and compare them:

Using subplot, plot these spectrograms:

1) Window length= 250 ms, overlap = % 50 

2) Window length = 100 ms, overlap = % 50 

3) Window length = 50 ms, overlap = % 50 

3) Window length = 25 ms, overlap = % 50 

Which spectrogram is better?
"""
subplot(4,1,1)
specgram(x, NFFT = int(.25*fs), noverlap=.125*fs,Fs = fs)
title("Window length = 250 ms")
ylabel("Frequency (Hz)")

subplot(4,1,2)
specgram(x, NFFT = int(.1*fs), noverlap=.05*fs,Fs = fs)
title("Window length = 100 ms")
ylabel("Frequency (Hz)")

subplot(4,1,3)
specgram(x, NFFT = int(.05*fs), noverlap=.025*fs,Fs = fs)
title("Window length = 50 ms")
ylabel("Frequency (Hz)")

subplot(4,1,4)
specgram(x, NFFT = int(.025*fs), noverlap=.0125*fs,Fs = fs)
title("Window length = 25 ms")
ylabel("Frequency (Hz)")