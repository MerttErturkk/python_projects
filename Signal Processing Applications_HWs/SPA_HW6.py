# -*- coding: utf-8 -*-
"""
@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 6

from numpy import *
from matplotlib.pyplot import *

#  Derive the formula of inst. frequency f(t). Be careful about the peak value of sinusoidal term.

# Answer: f(t) = 2000sin(4 pi t) + 3000
# you can user below codes to plot the given inst. freq. figure
"""
t = arange(0,5,0.01)
f = 2000*sin(4*pi*t) + 3000
plot(t,f)
title("Target instantaneous frequency")
xlabel("Time (sec)")
ylabel("Frequency (Hz)")
grid(True);
ylim([0, 6000])
"""

# - Using f(t), derive phase function.
# Answer: phase= 6000*pi*t - 2000*cos(2*pi*t)


# - Using phase function, generate signal x with fs = 22050 Hz (and duration of 5 seconds). You can use sin() or cos().

fs = 22050.0
t = arange(5*fs)/fs
x = cos(6000*pi*t - 1000*cos(4*pi*t) )

# - Listen what you have generated via sounddevice module. 
from sounddevice import *
# play(x,samplerate=22050)

# - Plot the spectrogram of x using specgram() command for NFFT = 500 and noverlap = 250 samples. (Fs = 22050)
figure(1)
specgram(x,Fs=22050,NFFT=500,noverlap=250)
xlabel("Time (sec)")
ylabel("Frequency (Hz)")

# Regenerate x for fs = 8000 Hz.
fs = 8000.0
t = arange(5*fs)/fs
x = cos(6000*pi*t - 2000*cos(4*pi*t) )
# - Listen new signal (samplerate = 8000)
#play(x,samplerate=8000)

# - Also plot the spectrogram of new x using specgram() command for NFFT = 500 and noverlap = 250 samples. (Fs = 8000)
figure(2)
specgram(x,Fs=8000,NFFT=500,noverlap=250)
xlabel("Time (sec)")
ylabel("Frequency (Hz)")











