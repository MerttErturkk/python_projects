# -*- coding: utf-8 -*-
"""   Tue Apr 20 18:37:10 2021   @author: ERTURK
"""


import numpy as np

import control as ctl

import matplotlib.pyplot as plt

#%%
M=1    # MASS
B=2    # Friction coeff.
K=1    # Spring coeff.

#CHANGE THESE PARAMETERS AND OBSERVE

G=ctl.tf(1,[M,B,K])
print(G)


T= np.linspace(0,30,3001)
x=np.linspace(0,30,3001) 


y= ctl.step_response(G,T)
r= ctl.forced_response(G,T,x) # x=T rampf func


#%% STEP RESPONSE

plt.figure(1)

plt.plot(y[0],y[1])

plt.plot(T,np.ones(y[0].shape))
         # 'array'.shape gives the shape == (3001,)
plt.grid(True)
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.title("Step Response")
#%% FORCED RESPONSE with RAMP

plt.figure(2)
plt.plot(r[0],r[1])

plt.plot(T,x)
plt.title("Ramp Function")

plt.grid(True)
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.title("Forced Response")


