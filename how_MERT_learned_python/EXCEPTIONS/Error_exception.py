# -*- coding: utf-8 -*-
"""   Thu Jun 25 16:09:05 2020   @author: ERTURK
"""


             ########  ERROR EXCEPTION  #############


"""
We can not divide a number by 0. So if user tries to do it instead of showing
error we can except that command and warn the user and avoid the crash.
"""


"""
try:
    #something
except ZeroDivisionError:
    # do or print something
"""    
    
## Example
print("give me two numbers")
print("enter 'q' to quit")
while True:
    first_number =input("\n First number:")
    if first_number == "q":
        break
    ans= second_number = input("\n Second number:")
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by 0!")
    else:
        print (ans)
        
""" TRY WORKS THE SAME WAY 'IF' DOES."""
    

