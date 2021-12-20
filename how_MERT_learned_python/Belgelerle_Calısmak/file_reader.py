# -*- coding: utf-8 -*-
"""   Wed Jun 24 23:03:15 2020   @author: ERTURK
"""


with open("num_pi.txt") as file_object:
    contents = file_object.read()
    print(contents)
    
    print("--------------------")
    print(contents.rstrip()) # rstrip removes whitespace characters from the 
                             # right side of a string. and now it matches 
                             # the original version of the file.
    
    
""" 
   Notice how we call open() in this program but not close(), 
   we could do it that way . But a better way is the keyword "with" 
   which closes the file once access to it is no longer needed.
"""
    