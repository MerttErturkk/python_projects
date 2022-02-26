# -*- coding: utf-8 -*-
"""   Fri Feb 26 13:36:52 2021   @author: ERTURK
"""


# =============================================================================
#  GENERATE AND PLOT COS AND SIN SAMPLED AT FS=60HZ AND REAL FREQ OF 3HZ
#  
#  x1(t)=cos(2pi*3t)   x2(t)=sin(2pi*3t)
#
# Real and Complex Parts of Euler
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

Ts= 1/60

n=np.arange(60)


x1=np.cos(2*np.pi*3*n*Ts)
x2=np.sin(2*np.pi*3*n*Ts)

plt.plot(n,x1,x2)

