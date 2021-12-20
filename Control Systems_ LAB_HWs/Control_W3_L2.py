# -*- coding: utf-8 -*-
"""   Mon Mar  8 17:05:50 2021   @author: ERTURK
"""

import numpy as np
import control as ctl
import matplotlib.pyplot as plt

G=ctl.tf([1],[1,1]) #nomin. coeff , denomin. coeff


#%% Impulse Response Function

h=ctl.impulse_response(G) # is a low pass filter

plt.figure()
plt.plot(h[0],h[1],label="impulse response h()") #h[0] array is time variable
                    #h[1] is output

#%% Plot stuff             
plt.grid(True)
plt.xlim([0,4.5])
plt.legend(loc="upper right")

#%% Step Response function

y=ctl.step_response(G)

plt.plot(y[0],y[1],label="step response y() ")
plt.legend(loc="upper right")

# =============================================================================
# 
# =============================================================================

#%% EXAMPLE 2
# High Pass Filter
G2= ctl.tf([1,0],[1,1])
plt.figure()
h2=ctl.impulse_response(G2) # is a high pass 

y2=ctl.step_response(G2)

plt.plot(h2[0],h2[1],label="impulse response h2()")
plt.plot(y2[0],y2[1],label="step response y2() ")
plt.grid(True)
plt.xlim([0,4.5])
plt.legend(loc="upper left")



#%% Forced Response

G3=ctl.tf([1],[1,1])

#Lets generate a sine wave and use it as input
T=np.linspace(0,1,1001)
f=10
w=2*np.pi*f
signal=np.sin(w/10*T)

#plot both the input and the forced response

plt.figure()
plt.plot(T,signal,label="input")

Y3=ctl.forced_response(G3,T,signal)
plt.plot(Y3[0],Y3[1],color="r",label="forced response of G3(s)")
plt.legend(loc="upper right")

#%% Cut off Frequency Example (same as upper one)

#Lets generate a sine wave and use it as input
T2 = np.linspace(0,1,1001)
f2 = 10
w2 = 2*np.pi*f2
signal_2 = np.sin(w2*T)

#We add a cut off freq Wc
Wc=2*np.pi*10 # 10Hz is cut off freq anything more is
              # attenuated. (at 10hz power is half)

G4=ctl.tf([1],[1/Wc,1]) #low pass
Y4=ctl.forced_response(G4,T2,signal_2)

plt.figure()
plt.plot(T2,signal_2,label="input")


plt.plot(Y4[0],Y4[1],label="forced response")
plt.legend(loc="upper right")








































