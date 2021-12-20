# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:24:21 2021

@author: ERTURK
"""

import os 
os.path.join("usr","bin","spam")


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join("C:\\Users\\asweigart",filename))
    
print(os.getcwd()) # get directory 

try: # change direction
    os.chdir('C:\\ThisFolderDoesNotExist')
except FileNotFoundError:
    print("#### Raise.. FileNotFoundError")
    
#os.makedirs(r'C:\deliciouss\walnut\waffles')




print(os.path.abspath("."))
print(os.path.abspath(".\\Scripts"))

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

#%%
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.path.sep))
#%%
print(os.path.getsize("C:\\Windows\\System32\\calc.exe"))
print(os.listdir('C:\\Windows\\System32')[:5])


totalSize = 0
for filename in os.listdir(r"C:\Windows\System32"):
    totalSize = totalSize + os.path.getsize(os.path.join(r"C:\Windows\System32",filename))
print(totalSize)
"""
Calling os.path.exists(path) will return True if the file or folder referred 
to in the argument exists and will return False if it does not exist.

Calling os.path.isfile(path) will return True if the path argument exists 
and is a file and will return False otherwise.

Calling os.path.isdir(path) will return True if the path argument exists 
and is a folder and will return False otherwise.

"""
