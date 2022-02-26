# -*- coding: utf-8 -*-
"""
@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 4

import numpy as np
import matplotlib.pyplot as plt

# - Derive the instantaneous frequency definition of the signal. 

# Answer:  
# should be calculated as f(t) = 6000*(2*t^2 + 2)

# - Calculate the maximum frequency if the duration is 200 ms.

tmax = 0.2
fmax = 6000*(2* (tmax**2) + 2) 
print "Maximum frequency is",fmax , " Hz"

#- Using Python, verify your answer by plotting time vs. inst. freq. for fs=44100 Hz.
fs = 44100.
t = np.arange(0.2*fs)/fs # 200 ms

f = 6000*(2* (t**2) + 2) 
plt.plot(t,f)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Instant. Frequency (Hz)') 
plt.ylim(11800,12700)
# - Generate the signal x(t)
x = np.sin(12000*np.pi*((2/3.)*t**3+2*t))

# - Listen to this signal. Are you able to hear?  Use "sounddevice" module.
import sounddevice as snd
snd.play(x,samplerate = 44100)