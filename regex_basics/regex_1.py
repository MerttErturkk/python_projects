# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:27:46 2021

@author: mertt
"""

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
"""

Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing 
'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'

"""

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# mo stands for "match object"

#%%  group with multiple pa

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

#%%    "(" as escape character == "\(" 
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))