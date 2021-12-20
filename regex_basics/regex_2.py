# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:23:38 2021

@author: mertt
"""
import re
#%%

heroRegex = re.compile (r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')

print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

#%%
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#%%
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

#%%
batRegex = re.compile(r'Bat(wo)*man') #0 or more
batRegex = re.compile(r'Bat(wo)+man') # 1 or more

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

#%%
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

