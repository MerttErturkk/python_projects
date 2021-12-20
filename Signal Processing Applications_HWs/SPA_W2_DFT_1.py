import numpy as np

import matplotlib.pyplot as plt

"""
We dont need fs or Ts
"""

M=400
n=np.arange(400)




k1=4

u4 = np.exp(1j*2*np.pi*k1*n/M)

u4_real = np.real(u4) #cos(2*np.pi*k*n/M)
u4_imag = np.imag(u4) #sin(2*np.pi*k*n/M)

plt.subplot(2,1,1)
plt.plot(u4_real)
plt.plot(u4_imag,label="imag k=4")
plt.legend(loc="lower right")

# =============================================================================
# =============================================================================

k2=8

u8 = np.exp(1j*2*np.pi*k2*n/M)

u8_real = np.real(u8) #cos(2*np.pi*k*n/M)
u8_imag = np.imag(u8) #sin(2*np.pi*k*n/M)

plt.subplot(2,1,2)
plt.plot(u8_real)
plt.plot(u8_imag,label="imag k=8")
plt.legend(loc="lower right")


# =============================================================================
# 
# =============================================================================
print("u4 norm")
print(np.dot(u4,np.conj(u4)) / M) 

print("u8 norm")
print(np.dot(u8,np.conj(u8)) / M) 
print("\n u4 and u8 have self projection on their selves \n but u4 and u8 have no projection on each other")


print("\n u4 * u8 norm")

print(np.dot(u4,np.conj(u8)) / M) 
print("the result is a very small number (assume it is zero)")