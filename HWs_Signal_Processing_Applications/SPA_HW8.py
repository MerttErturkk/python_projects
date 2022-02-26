# -*- coding: utf-8 -*-
"""
@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 8

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd


#Reading an audio file

#In order to better understand the echo filters that will be created in this assignment, a real audio file will be used.

# 1) Firstly, scipy.io.wavfile module will be used for this.

import scipy.io.wavfile as wav

#2) The test.wav file under Resources should be downloaded to the computer (preferably the desktop).

#3) The file should be read with Python using the location of the downloaded file. Example code for username "Guray" in Windows operating system:

data = wav.read (r'C:/Users/Guray/Desktop/test.wav')

#At the end of the process, the data variable is formed as follows:

# data = (22050, array ([0, 0, 0, ..., 0, 0, 0], dtype = int16))
print data

#Here, the first element (index = 0) of the data is the number of 22050 (Hz), which is the sampling frequency of the sound, and the second element (index = 1) is the vector that carries the numbers that shape the sound wave.

#The last element, "dtype," specifies the data type, so the sound wave is represented by 16-bit signed integers (what is the largest value?).

#It is enough just to get the second element to get the audio data:

voice = data[1]

#As you know, the length of the audio data can be viewed with the len() function. The result is 4848192 samples. Since fs = 22050, this is an audio file with a duration of approximately 220 seconds.

#It is not possible to filter the entire audio file at once, so let's just pull out the data between the 1st and 7th seconds, for example:

voice = voice[22050: 22050 + 7 * 22050] # Data from 1st to 7th

#Listen to this data now :)

from sounddevice import *

play(voice, samplerate = 22050)

# Echo filter design:
# After reading and trimming the audio file, you will now create the filter.

# - Number of echoes is 4, echo rate (alpha) 0.5 and delay 200 ms.

# - Create numerator and denumerator vectors, then filter audio data as below.

# y = lfilter (numerator, denominator, sound / 32267.0)

# THIS PROCESS CAN TAKE LONG!!!!

# After filtering, listen y signal.


fs = 22050.
R = int(0.2*fs)
N = 5 # 4 echoes
alpha = .5

b = np.hstack((1, np.zeros(N*R-1), - (alpha**N)))
a = np.hstack((1, np.zeros(R-1),- alpha))
from scipy.signal import lfilter

#y = lfilter(b,a,voice/32267.0) # it is gonna take looooong!
#play(y, samplerate = 22050)

