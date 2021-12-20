# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:56:36 2021

@author: mertt
"""

with open("steam.txt",encoding = "utf8") as text:
    names = []
    temp = ""
    for line in text:
        if "kayıtlarda " in line:
            temp += line[46:54]
        if r'<div class="gameListRowItemName ellipsis "' in line:
            names.append(line.split('">')[1][:-7])
            
    temp = temp.replace(",","")
    hours = []
    
    for t in temp.split():
        try:
            hours.append(float(t))
        except ValueError:
            pass
    
n=0
for name in names:
    try:
        print(name+"\n" +str(hours[n]))
        n += 1
    except IndexError:
        print("\n\nNo hours logged:")
        print(names[n:])
        break
    
print("\n\nTotal playtime on steam == %.1f\n\n" %sum(hours))
    