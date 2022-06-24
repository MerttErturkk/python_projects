import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
fig, ax = plt.subplots(figsize=(8, 5))

c1 = '#cf630c' #dark orange
c2 = '#80f0e7' #turqoise

a = [] #gradients list
n=500
for x in range(n+1):
    a += [colorFader(c1,c2,x/n)]
    ax.axvline(x, color=colorFader(c1,c2,x/n), linewidth=4)
plt.show()

