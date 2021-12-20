# -*- coding: utf-8 -*-
"""   Wed Mar 24 20:10:10 2021   @author: ERTURK
"""

import numpy as np
from numpy import cos,pi
import matplotlib.pyplot as plt
from numpy.fft import fft

fs=8000  #sample freq
n=np.arange(16000) # 2 second worth sample

t=n/fs
x=cos(2000*pi*t) # +cos(1000*pi*t)

# =============================================================================
# fr/fs=k/M ///// fr=k*fs/M
# =============================================================================

M=len(x)
k=np.arange(M)
fr=k*fs/M


plt.plot(fr,abs(fft(x)))
plt.xlim(0,fs/2)



from sounddevice import *
#play(x,samplerate=8000)


########################################################
#EXP2  FREQ CHANGE IN TIME

phi= 1000*pi*(t**2) + 2000*pi*t
phi2=2000*pi*t +-25*cos(3*pi*t)

y=cos(phi2)
plt.plot(fr,abs(fft(y)))

play(y,samplerate=8000)

