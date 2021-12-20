# -*- coding: utf-8 -*-
"""   Thu Jun 25 23:56:21 2020   @author: ERTURK
"""

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first =input("\nPlease give me a first name: ")
    if first =="q":
        break
    last=input("Please give me a last name: ")
    if last =="q":
        break
    
    formatted_name = get_formatted_name(first,last)
    
    print("\tNeatly formatted name: " + formatted_name + ".")
