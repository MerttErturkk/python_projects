# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:14:11 2021

@author: mertt
"""

import re

#%% find-all method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
num_list=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(num_list)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
num_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(num_list)

#%% decimal more than 1 / whitespace / word characters

xmasRegex = re.compile(r'\d+\s\w+')

xmas_list = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(xmas_list)

#%% find vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)

#%% find consonants
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonants = consonantRegex.findall('RoboCop eats baby food. BABY FOOD \n.')
print(consonants)

#%% begins with hello?
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.') == None)
#%% ends with a number of any length?
endsWithNumber = re.compile(r'\d+$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

#%% begins and end with num?
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)

#%% "."  == wildcard character(any char except newline)
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#%% find name and surname of any length
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo)
print(mo.group(1))
print(mo.group(2))
#%% non-greedy "(.*)"
#non-greedy means shortest possible string // without "?" it returns the longest
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())  
#%%
"""
The ? matches zero or one of the preceding group.
•	 The * matches zero or more of the preceding group.
•	 The + matches one or more of the preceding group.
•	 The {n} matches exactly n of the preceding group.
•	 The {n,} matches n or more of the preceding group.
•	 The {,m} matches 0 to m of the preceding group.
•	 The {n,m} matches at least n and at most m of the preceding group.
•	 {n,m}? or *? or +? performs a nongreedy match of the preceding group.
•	 ^spam means the string must begin with spam.
•	 spam$ means the string must end with spam.
•	 The . matches any character, except newline characters.
•	 \d, \w, and \s match a digit, word, or space character, respectively.
•	 \D, \W, and \S match anything except a digit, word, or space character, 
      respectively.
•	 [abc] matches any character between the brackets (such as a, b, or c).
•	 [^abc] matches any character that isn’t between the brackets.
"""
# newlineRegex = re.compile('.*', re.DOTALL) // re.DOTALL includes 
# obocop = re.compile(r'robocop', re.I) ignore case sensitivity