# -*- coding: utf-8 -*-
"""   Tue Jun 23 17:49:59 2020   @author: ERTURK
"""


def get_formatted_name(first_name,last_name,middle_name=''):
    
    if middle_name: #OLAY BURADA BİTİYOR.
        
        full_name = first_name +" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()
    
musician=get_formatted_name("jimi","hendrix")
print(musician)
musician=get_formatted_name("john", "hooker","lee")
print(musician)

