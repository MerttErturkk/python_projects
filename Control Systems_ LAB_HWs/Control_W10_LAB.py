# -*- coding: utf-8 -*-
"""   Tue Apr 27 18:28:49 2021   @author: ERTURK
"""
import numpy as np
import control as ctl
import matplotlib.pyplot as plt


# =============================================================================
# PART I  (TRY TO RUN CELL BY CELL)
# =============================================================================
G= ctl.tf(5,[1,5])  
  
T= np.linspace(0,10,101)

#%%  OPEN LOOP (with no feedback)  UNIT STEP
#  STEADY STATE ERROR === 5-1 = 4
y = ctl.step_response(G,T)

plt.figure(1) 

plt.plot(y[0],y[1],label = "step response")
plt.plot(y[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()


#%% WITH NO FEEDBACK RAMP FUNC

#STEADY STATE ERROR == INF.

r  = T
yr= ctl.forced_response(G,T,r)

plt.figure(2) 

plt.plot(yr[0],yr[1],label = "ramp forced response")
plt.plot(yr[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()


#%% CLOSED LOOP TRANSFER FUNCTIONS

Gclosed = ctl.feedback(G)

yc=ctl.step_response(Gclosed,T)
ycr= ctl.forced_response(Gclosed,T,r)

plt.figure(3) 

plt.plot(yc[0],yc[1],label = "closed step response")
plt.plot(yr[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()


plt.figure(4) 

plt.plot(ycr[0],ycr[1],label = "closed forced ramp response")
plt.plot(yr[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()

#%%

# =============================================================================
# PART 2 
# =============================================================================

G2= ctl.tf(5,[1,5])
G2closed = ctl.feedback(G2)

# T= np.linspace(0,10,101)
# r  = T

y2 = ctl.step_response(G2,T)
yr2= ctl.forced_response(G2,T,r)
yc2=ctl.step_response(G2closed,T)
ycr2= ctl.forced_response(G2closed,T,r)

plt.figure(5)
#---------
plt.subplot(221)
plt.plot(y2[0],y2[1],label = "step response")
plt.plot(y2[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()

#------
plt.subplot(222)
plt.plot(yr2[0],yr2[1],label = "ramp forced response")
plt.plot(yr2[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()

#--------
plt.subplot(223)
plt.plot(yc2[0],yc2[1],label = "closed step response")
plt.plot(yr2[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()

#------------
plt.subplot(224)
plt.plot(ycr2[0],ycr2[1],label = "closed forced ramp response")
plt.plot(ycr2[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()
#------------
#%%
# =============================================================================
# PART 3 SECOND ORDER SYSTEM (USES THE SAME CODE ABOVE)
# (RUN CELL)
# =============================================================================

G2 = ctl.tf(25,[1,5,0])
G2closed = ctl.feedback(G2)

T = np.linspace(0,10,101)
r = T
p = (T**2)/2

y2 = ctl.step_response(G2,T)
yr2= ctl.forced_response(G2,T,r)
yc2=ctl.step_response(G2closed,T)
ycr2= ctl.forced_response(G2closed,T,r)


plt.figure(6)
#---------
plt.subplot(221)
plt.plot(y2[0],y2[1],label = "step response")
plt.plot(y2[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()

#------
plt.subplot(222)
plt.plot(yr2[0],yr2[1],label = "ramp forced response")
plt.plot(yr2[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()

#--------
plt.subplot(223)
plt.plot(yc2[0],yc2[1],label = "closed step response")
plt.plot(yr2[0],np.ones(T.shape),label = "unit step")
plt.xlabel("time")
plt.legend()

#------------
plt.subplot(224)
plt.plot(ycr2[0],ycr2[1],label = "closed forced ramp response")
plt.plot(ycr2[0],r,label = "ramp")
plt.xlabel("time")
plt.legend()
#------------

#%% PARABOLIC INPUT FORCED RESPONSE

ycp= ctl.forced_response(G2closed,T,p)

plt.figure(7) 

plt.plot(ycp[0],ycp[1],label = "closed forced parabolic response")
plt.plot(ycp[0],p,label = "parabol")
plt.xlabel("time")
plt.legend()
