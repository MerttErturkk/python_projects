# -*- coding: utf-8 -*-
"""   Tue Jun 23 19:03:25 2020   @author: ERTURK
"""



# COPYING A LIST AS AN INPUT TO A FUNCTION

# instead of puting the original list we can send the copy
# which would look like listem[:] , which is a list made
# from the first element to last element of 'listem'.

listem=["123","12","1"]
def function1(a):
    while a:
        x=a.pop()
        print(x)