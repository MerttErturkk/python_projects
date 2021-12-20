# -*- coding: utf-8 -*-
"""   Tue Jun 23 20:40:45 2020   @author: ERTURK
"""

def make_pizza(size,*toppings):
    print("\nmaking "+str(size) +'" size pizza with following toppings:')
    for topping in toppings:
        print("- "+topping)
        
        
        
        
        
make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green peppers","extra cheese")




"""
PYTHON STORES THE FIRST CALUE IT RECIEVES IN THE PARAMETER SIZE. 
ALL OTHER VALUES THAT COME AFTER ARE STORED IN
TUPPLE(*toppings). THE FUNCTION CALLS INCLUDE AN ARGUMENT FOR THE 
SIZE FIRST, FOLLOWED BY AS MANY TOPPINGS AS NEEDED.
"""