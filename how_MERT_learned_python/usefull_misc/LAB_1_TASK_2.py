# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:19:02 2021

@author: mertt
"""

# There already exist  """bin()""" and """hex()"""" functions. 
# But i went ahead and wrote them again.
# In the first way that came to my mind.



# =============================================================================
# 1
# =============================================================================
def dec_to_bin(a):
    binary =""
    a=int(a)
    if a ==0:
        return "0"
    while a !=0:
        r= a%2
        binary +=str(r)
        a= int(a/2)
    return binary[::-1]

# =============================================================================
# 2
# =============================================================================
def bin_to_dec(a):
    temp = 0
    for i in range(len(a)):
        temp += (2**i)*int(a[-1-i])
    return temp
# =============================================================================
# 3
# =============================================================================
def dec_to_hex(a):
    a=int(a)
    b = dec_to_bin(a).rjust(32,"0")
    x=""
    for i in range(8):
        temp = b[4*i:4*i+4]
        if temp == "0000":
            x+="0"
        elif temp == "0001":
            x+="1"
        elif temp == "0010":
            x+="2"
        elif temp == "0011":
            x+="3"
        elif temp == "0100":
            x+="4"
        elif temp == "0101":
            x+="5"
        elif temp == "0110":
            x+="6"
        elif temp == "0111":
            x+="7"
        elif temp == "1000":
            x+="8"
        elif temp == "1001":
            x+="9"
        elif temp == "1010":
            x+="A"
        elif temp == "1011":
            x+="B"
        elif temp == "1100":
            x+="C"
        elif temp == "1101":
            x+="D"
        elif temp == "1110":
            x+="E"
        elif temp == "1111":
            x+="F"
    return x
# =============================================================================
# 4
# =============================================================================
def hex_to_dec(a):
    temp = 0
    for i in range(len(a)):
        try:
            temp += (16**i)*int(a[-1-i])
        except ValueError:
            if a[-1-i]=="A":
                temp += (16**i)*10
            elif a[-1-i]=="B":
                temp += (16**i)*11
            elif a[-1-i]=="C":
                temp += (16**i)*12
            elif a[-1-i]=="D":
                temp += (16**i)*13
            elif a[-1-i]=="E":
                temp += (16**i)*14
            elif a[-1-i]=="F":
                temp += (16**i)*15    
    return temp
# =============================================================================
# Test Lines
# =============================================================================
print(dec_to_bin(17))
print(bin_to_dec("1010"))
print(dec_to_hex(255))
print(hex_to_dec("FFAA"))