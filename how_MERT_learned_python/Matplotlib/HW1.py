import numpy as np
import matplotlib.pyplot as plt

hb = 200
hm = 1.5
a = np.arange(1,8,0.3)
fc1 = 450
fc2 = 900
fc3 = 1800
fc4 = 1950

x1 = 69.55 + 26.16*np.log10(fc1) - 13.82*np.log10(hb) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-(6.55*np.log10(hb)))*np.log10(a) 
x2 = 69.55 + 26.16*np.log10(fc2) - 13.82*np.log10(hb) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-(6.55*np.log10(hb)))*np.log10(a) 
y1 = 46.3 + 33.9*np.log10(fc3)- 13.82*np.log10(hb) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(hb))*np.log10(a) + 3
y2 = 46.3 + 33.9*np.log10(fc4)- 13.82*np.log10(hb) - (3.2*(np.log10(11.75*hm)*np.log10(11.75*hm))-4.97) + (44.9-6.55*np.log10(hb))*np.log10(a) + 3

plt.plot(a,x1,"--",label= "fc=450 MHz Okumura Hata")
plt.plot(a,x2,".",label="fc=900 MHz Okumura Hata")
plt.plot(a,y1,"-",label="fc=1800 MHz Cost 231")
plt.plot(a,y2,".-",label="fc=1950 MHz Cost 231")

plt.grid(True)
plt.xlim(1,8)
plt.xlabel("Range(km)",fontsize=14)
plt.ylabel("Path Loss(dB)",fontsize=14)
plt.legend(loc="lower right")
plt.title("HW1  hb=20 m hm=1.5 m  Urban Area")
plt.show()


