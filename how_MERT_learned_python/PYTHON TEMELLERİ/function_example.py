# -*- coding: utf-8 -*-
"""   Tue Jun 23 17:11:40 2020   @author: ERTURK
"""

def describe_pet(pet_name,animal_type= "dog"): # "dog is now default value
    print ("\nI have a " + animal_type)
    print("My "+ animal_type +"'s name is " + pet_name.title())
    
    a=[animal_type,pet_name]
    return a # konsola b=describe_pet("tarçın") yazarsam
             # fonksiyon b sonucu olarak a listesini verir.




