# -*- coding: utf-8 -*-
"""   Mon Mar 22 12:15:31 2021   @author: ERTURK
"""


import numpy as np
import control as ctl
import matplotlib.pyplot as plt


G1=ctl.tf([50],[1,50])
G2= ctl.tf([150],[1,150])

T=np.linspace(0,0.1,1001)

# =============================================================================
# 
# =============================================================================

h1=ctl.impulse_response(G1,T)
h2=ctl.impulse_response(G2,T)
 

plt.figure(1)
plt.title("impulse responses")
plt.plot(h1[0],h1[1],label="h1")
plt.plot(h2[0],h2[1],label="h2")


plt.legend()
plt.grid()
plt.xlabel("time(s)")

# plt.xlim([0,0.1])


# =============================================================================
# 
# =============================================================================

y1= ctl.step_response(G1,T)
y2= ctl.step_response(G2,T)

plt.figure(2)
plt.title("step responses")
plt.plot(y1[0],y1[1],label="y1")
plt.plot(y2[0],y2[1],label="y2")


plt.grid()
plt.xlabel("time(s)")

# =============================================================================
# Cascade connection
# =============================================================================

G_cascade=G1*G2
y_cas=ctl.step_response(G_cascade,T)
plt.plot(y_cas[0],y_cas[1],label="y_cas")



# =============================================================================
# Parallel connection
# =============================================================================

G_parallel =0.5*(G1+G2)
y_par=ctl.step_response(G_parallel,T)
plt.plot(y_par[0],y_par[1],label="y_par")

#plt.legend()

plt.legend()
































