import numpy as np
import matplotlib.pyplot as plt

fc = 1950
hm = 1.5
a = np.arange(30,101)
r1=0.5
r2 = 1
r3 = 2
r4 = 3

y1 = 46.3 + 33.9*np.log10(fc)- 13.82*np.log10(a) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(a))*np.log10(r1) + 3
y2 = 46.3 + 33.9*np.log10(fc)- 13.82*np.log10(a) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(a))*np.log10(r2) + 3
y3 = 46.3 + 33.9*np.log10(fc)- 13.82*np.log10(a) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(a))*np.log10(r3) + 3
y4 = 46.3 + 33.9*np.log10(fc)- 13.82*np.log10(a) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(a))*np.log10(r4) + 3

plt.plot(a,y1,"--")
plt.plot(a,y2,".")
plt.plot(a,y3,"-")
plt.plot(a,y4,".-")
plt.legend(["R=0.5 km","R=1 km","R=2 km","R=3 km"])
plt.grid(True)
plt.xlim(30,100)
plt.xlabel("Base Station Effective Antenna Height(hb)")
plt.ylabel("Path Loss(dB)")


plt.savefig("HW2.png",bbox_inches = "tight" )