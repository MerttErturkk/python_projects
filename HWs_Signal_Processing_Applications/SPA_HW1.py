# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:20:24 2017

@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 1

import numpy as np
import matplotlib.pyplot as plt


#Question 1:
Ts = 0.025 # 25 ms sampling period
fs = 1/Ts
n = np.arange(20)
t = n/fs
x = 2*np.cos(8*np.pi*t)
plt.plot(t,x)
plt.xlabel('Time (sec)')
plt.grid(True)
plt.title("Plot of the signal $ x(t)=2cos(8\pi t)$")


# Question 2
"""
Answers
 - normalized period = 10 samples
 - normalized frequency = 1/10 = 0.1
 - normalized angular frequency = 2pi*(0.1) = 0.2pi
 - real frequency = fnormalized*fs or fnormalized/Ts = 0.1/ 0.001 = 100 Hz
 - cont. tiime formula  y = cos(200 pi t)

 PS: You may plot the question 2's figure using below codes
"""
n = np.arange(20)
x = np.cos(2*np.pi*.1*n)
plt.figure(2)
plt.stem(x)
plt.grid(True)
plt.xlabel("Samples")
plt.xlim([-1,21])
plt.ylim(-1.2,1.2)

