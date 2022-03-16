# -*- coding: utf-8 -*-
"""   Thu May 20 18:06:01 2021   @author: ERTURK
"""

import numpy as np
import control as ctl
import matplotlib.pyplot as plt


#%%
G = ctl.tf([1,5],[1,3])

# ctl.root_locus(G)




Ks=np.hstack((np.arange(0,1,.1),np.logspace(0,2,20)))

T = np.linspace(0,2,1001)

#%%
for K in Ks:
    Gclosed = ctl.feedback(K*G)
    y = ctl.step_response(Gclosed,T)
    
    p= Gclosed.pole()
    plt.subplot(1,2,1)
    plt.plot(np.real(p),np.imag(p),'.',color='b')
    plt.xlim([1,6])
    plt.xlim([-10,10])
    plt.grid(True)
    plt.title('System polse for Ks from 0 to 100')
    
    plt.subplot(1,2,2)
    plt.plot(y[0],y[1])
    plt.title("step response")
    plt.xlabel("time")
    plt.grid(True)
    plt.ylim([0,5])
    plt.pause(.3)
    


#%%
plt.figure()
G=ctl.tf([1],[1,2,-8])
Ks = np.hstack((np.arange(0,10,.5),np.logspace(1,2,20)))

T= np.linspace(0,3,1001)

ctl.root_locus(G)




#%%

G = ctl.tf([1,0],[1,4,0,1])
plt.figure()

Ks = np.hstack((np.arange(0,5,.25),np.logspace(1,2,20)))


for K in Ks:
    Gclosed = ctl.feedback(K*G)
    y = ctl.step_response(Gclosed,T)
    
    p= Gclosed.pole()
    plt.subplot(1,2,1)
    plt.plot(np.real(p),np.imag(p),'.',color='b')
    plt.xlim([1,6])
    plt.xlim([-10,10])
    plt.grid(True)
    plt.title('System polse for Ks from 0 to 100')
    
    plt.subplot(1,2,2)
    plt.plot(y[0],y[1])
    plt.title("step response")
    plt.xlabel("time")
    plt.grid(True)
    plt.ylim([0,5])
    plt.pause(.3)
