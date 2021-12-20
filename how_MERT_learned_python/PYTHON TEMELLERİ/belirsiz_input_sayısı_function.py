# -*- coding: utf-8 -*-
"""   Tue Jun 23 19:51:38 2020   @author: ERTURK
"""


# SAYISI BELLİ OLMAYAN INPUTLARI LİSTE OLARAK KABUL EDİYOR.

def make_pizza(*toppings):
    print("\nmaking pizzawith following toppings:")
    for topping in toppings:
        print("- "+topping)
        
        
        
        
        
make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")
