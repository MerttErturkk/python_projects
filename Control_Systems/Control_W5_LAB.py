# -*- coding: utf-8 -*-
"""   Wed Mar 24 18:03:45 2021   @author: ERTURK
"""


import numpy as np
import matplotlib.pyplot as plt
import control as ctl




p1= -6 + 8j
p2= -6 - 8j
# p1*p2= c ///// p1+p2= -b

K=100 # found later on

#G = ctl.tf([1],[1,12,100])
#G = ctltf([K],[1,-(p1+p2),p1*p2])
G = ctl.tf([K],np.poly([p1,p2]))


T= np.linspace(0,5,1001)
y=ctl.step_response(G,T)


plt.figure(1)
plt.plot(y[0],y[1])
plt.grid(True)
# =============================================================================
# 
# =============================================================================

P1=-.5+(8*np.pi)*1j
P2=np.conjugate(P1)

K2=np.real(P1*P2)
G2= ctl.tf(K2,np.poly([P1,P2]))
Y2=ctl.step_response(G2,T)


plt.plot(Y2[0],Y2[1],label="tao= 2 ((-1/real part of root)))")

# =============================================================================
# 
# =============================================================================
p3=-1+(8*np.pi)*1j
p4=np.conjugate(p3)

K3=np.real(p3*p4)
G3= ctl.tf(K3,np.poly([p3,p4]))
Y3=ctl.step_response(G3,T)

plt.plot(Y3[0],Y3[1],label="smaller tao= 1")

plt.legend()




















