import numpy as np
import control as ctl


print("QUESTION 1\n------------------------")

#Use the np.poly function

roots=np.array([-1,2])
coeffs=np.poly(roots) # generates a polynomial depending on roots

print("the polynomial coeffs are " ,coeffs)



#np.array is faster than ordinary list
roots2= np.roots(np.array([1,-1,-2])) #generates roots from poly coefficients

print("the roots of the polynomial are",roots2)

# =============================================================================
# 
# =============================================================================

print("\nQUESTION 2\n----------------------")

# Generate the transfer function "G" with ctl.tf()

a=[1,3,2]
b=[1,4]

G=ctl.tf(b,a)   # we can write "help(ctl.tf)" to console for more info

print("G(s)\n",G) # or we can just "G" in console for better picture

z=np.roots(b) # zeros
p=np.roots(a) # poles
print("G(s) ===> zeros ",z,"// poles",p)



z2=ctl.zero(G) # is the same as z but found from G(s) which is better...
p2=ctl.pole(G) # same goes for this one p1 == p


z3=G.zero() # they can also be found using class function
p3=G.pole()  

