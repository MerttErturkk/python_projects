# -*- coding: utf-8 -*-
"""   Thu May  6 18:22:35 2021   @author: ERTURK
"""


import numpy as np

import control as ctl

import matplotlib.pyplot as plt



Gc = ctl.tf(10,[1,10])

Gp = ctl.tf(100,[1,16,100])


Gr = ctl.feedback(Gc*Gp)

Gd = ctl.feedback(Gp,Gc)

t = np.linspace(0,5,501)


D = 0.01*np.ones(t.shape) #0.1 u(t)

R = np.ones(t.shape)  #input


y_r = ctl.forced_response(Gr,t,R)

y_d = ctl.forced_response(Gd,t,D)


Y = y_r[1] - y_d[1]

plt.figure(1)
plt.plot(t,Y)
plt.plot(t,R,label ="r=u(t)")
plt.grid()
plt.title("Y(s)")
plt.legend()




plt.figure(2)
e = R - Y  # Error
plt.plot(t,e)
plt.title("Error signal E(s)")


plt.figure(3)
plt.plot(t,y_d[1])
plt.plot(t,R)
plt.grid()
plt.title("D(s)")
