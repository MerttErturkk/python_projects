# -*- coding: utf-8 -*-
"""

@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 7


import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd

"""
Question 1)

A person claps hands beyond a wall and hears a single echo. The person-wall distance is 21.25 meters. Consider that sound is attenuated by a factor of 30%.

We want to simulate this acoustic environment via a digital single echo filter.

Then (for fs = 48000 Hz and velecity of sound = 340 m/s),

- Determine the delay "R" of the echo filter,

- Plot the impulse response of this filter
"""

v = 340. #m/s
d = 21.25
delay = 2*d/v # distance/velocity = time. Sound wave reflected from the wall and goes back again, so it travels 22.5 x 2 meters

fs = 48000.
R = int(delay*fs) # this value should be an integer because it is the number of samples for the echo filter
alpha = 0.7
print "Value of R =",R
b = np.hstack((1,np.zeros(R-1),alpha))
plt.figure(1)
plt.stem(b)
plt.xlim(-500,6500)
plt.xlabel('Samples [n]')
plt.title("Impulse Response R=6000, $ \\alpha $=0.7")

"""
Question 2)

- For fs = 8kHz, using Comb Filter frequency response theory, generate a digital harmonic filter for multiples of 400 Hz  (What is R?).

- Min and max magnitude response values should be 0 and 2 (What is alpha?).

- Generate a 5 seconds of white noise and apply this filter. Verify your result.

(- Search: how to generate a white noise?)



# ------ SOLUTION ----------


DeltaF = 400.
fs = 8000.
R = fs/DeltaF
print "R = ", R
alpha = 1 
b = np.hstack((1,np.zeros(R-1),alpha))

# Frequency Response Plotting
w = np.linspace(0,np.pi/2,1000) # f will be in the interval -> 0 to 2000 Hz 
H = 1 + alpha*np.exp(-1j*w*R)
fr = w*fs/(2*np.pi)
plt.figure(1)
plt.plot(fr,abs(H))
plt.xlabel("Frequency (Hz)")
plt.grid(True)
plt.title("Frequency Response")
plt.xlim(-200,2200)

# Generation of Noise
from numpy.random import randn
noise = randn(5*fs)
#snd.play(noise,samplerate=8000)

# Filtering
from scipy.signal import lfilter
y = lfilter(b,1,noise)
#snd.play(y,samplerate=8000)

# Compare FFTs
from numpy.fft import fft
plt.figure(2)
M=len(y)
freals = np.hstack((np.arange(M/2+1),np.arange(-M/2 + 1,0)))*fs/M
plt.subplot(2,1,1)
plt.plot(freals,abs(fft(noise)))
plt.xlabel("Frequency (Hz)")
plt.title("FFT of Noise Signal")
plt.subplot(2,1,2)
plt.plot(freals,abs(fft(y)))
plt.xlabel("Frequency (Hz)")
plt.title("FFT of Filtered Signal")
"""