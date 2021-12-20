# -*- coding: utf-8 -*-
"""

@author: Guray
"""
# EE0813 Signal Processing Applications
# Homework 2

import numpy as np
import matplotlib.pyplot as plt

# Questions

# 1) Generate the basis functions u0(n), u4(n), u8(n) and u56(n) for 64 points (M=64) of DFT calculation. Number of samples is also 64 (n=0,1, .., 63).

M = 64
n = np.arange(64)

u0 = np.exp(1j*2*np.pi*0*n/M) # or directly 1
u4 = np.exp(1j*2*np.pi*4*n/M)
u8 = np.exp(1j*2*np.pi*8*n/M)
u56 = np.exp(1j*2*np.pi*56*n/M)

# 2) Calculate the mutual projections and self projections (refering to lecture slides).
print "*** Self Projections ***"  
print " u0 and  u0: ", np.sum(u0*np.conjugate(u0))
print " u4 and  u4: ", np.sum(u4*np.conjugate(u4))
print " u8 and  u8: ", np.sum(u8*np.conjugate(u8))
print "u56 and u56: ", np.sum(u56*np.conjugate(u56))
print " "
print "*** Mutual Projections of u0 ***"  
print " u0 and  u4: ", np.sum(u0*np.conjugate(u4))
print " u0 and  u8: ", np.sum(u0*np.conjugate(u8))
print " u0 and  u56: ", np.sum(u0*np.conjugate(u56))
print " "
print "*** Mutual Projections of u4 ***"  
print " u4 and  u0", np.sum(u4*np.conjugate(u0))
print " u4 and  u8: ", np.sum(u4*np.conjugate(u8))
print " u4 and  u56: ", np.sum(u4*np.conjugate(u56))
print " "
print "*** Mutual Projections of u8 ***"  
print " u8 and  u0", np.sum(u8*np.conjugate(u0))
print " u8 and  u4: ", np.sum(u8*np.conjugate(u4))
print " u8 and  u56: ", np.sum(u8*np.conjugate(u56))

print " "
print "*** Mutual Projections of u56 ***"  
print " u56 and  u0", np.sum(u56*np.conjugate(u0))
print " u56 and  u4: ", np.sum(u56*np.conjugate(u4))
print " u56 and  u8: ", np.sum(u56*np.conjugate(u8))

#  3) Plot the real parts of basis functions on the same graph with different colors and put a legend for each curve.

plt.figure(1)
plt.plot(np.real(u0))
plt.plot(np.real(u4))
plt.plot(np.real(u8))
plt.plot(np.real(u56))
plt.grid()
plt.legend(("$u_0(n)$","$u_4(n)$","$u_8(n)$","$u_{56}(n)$"))
plt.title("Real parts of generated basis functions")
plt.ylim(-1.5,1.5)
plt.xlabel("Samples")

# 4) How many curves exist? Why?

# Answer: There exists 4 curves, however since the real parts of u8(n) and u56(n) are equal, they overlap.

# 5)  On a new figure, plot the complex parts of u8(n) and u56(n) basis functions with time if fs=128 Hz. (This time, x-axis will be in "seconds" unit, not in samples). What is your comment?

plt.figure(2)
t = n/128.
plt.plot(t,np.imag(u8))
plt.plot(t,np.imag(u56))
plt.grid()
plt.legend(("$u_4(n)$","$u_56(n)$"))
plt.title("Complex parts (Sine components)")
plt.ylim(-1.5,1.5)
plt.xlabel("Time (sec)")
# Complex parts of u8 and u56 are sin. functions with equal frequencies but different signs.

# 6) By using the figure in (3), detect the real period/frequency of the basis functions.

# answer: 8 cycles exist in 0.5 sec so frequency is 16 Hz.

# 7) Proof your answer in (6) with theoretical knowledge.

# Norm. ang. freq. of u8(n) is 2pi*8/64 = 0.25*pi
# So normalized frequency is 0.125
# So for fs = 128 Hz, fr = fN*fs = 0.125 * 128 = 16 Hz.



