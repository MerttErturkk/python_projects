# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
stock = { "banana": 6, 
         "apple": 0, 
         "orange": 32, 
         "pear": 15 }

prices = { "banana": 4, 
          "apple": 2, 
          "orange": 1.5, 
          "pear": 3 }

def rechnung(order):
    """
    Takes order list as input,
    
    Returns (int bill) , (dict stock)
    """
    bill = 0
    for item in order:
        if (item in stock) and stock[item]>0:
            stock[item] -= 1
            bill += prices[item]
        else:
            print("item: '"+item+"' is OUT OF STOCK")
    
    return bill,stock

# # =============================================================================
# # Test line
# # =============================================================================
# print(stock)
# print("\n\n")
# 
# bill,stock =rechnung(["banana","apple","banana"])
# 
# print("your bill is " +str(bill))
# print("\n\n")
# print(stock)
# =============================================================================
