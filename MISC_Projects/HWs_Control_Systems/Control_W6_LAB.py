# -*- coding: utf-8 -*-
"""   Tue Mar 30 18:03:35 2021   @author: ERTURK
"""


import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# =============================================================================
# 
# s1= -2 + 4*np.pi*1j
# s2= -2 - 4*np.pi*1j
# 
# 
# 
# 
# t=np.linspace(0,3,3001)
# K=162
# G=ctl.tf([K],np.poly([s1,s2]))
# Y=ctl.step_response(G,t)
# 
# 
# s3=3*s1
# s4=3*s2
# 
# G=ctl.tf([K],np.poly([s1,s2]))
# Y=ctl.step_response(G,t)
# 
# =============================================================================

# =============================================================================
# G1=ctl.tf(1,[1,10,169])
# G2=ctl.step_response(G1)
# 
# plt.plot(G2[0],G2[1])
# =============================================================================


G=ctl.tf(-4,[1,5,1,-1])
t=np.linspace(0,30,3001)

Gc=ctl.feedback(G)
Y=ctl.impulse_response(Gc,t)

plt.plot(Y[0],Y[1])