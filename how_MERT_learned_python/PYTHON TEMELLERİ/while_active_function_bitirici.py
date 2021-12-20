# -*- coding: utf-8 -*-
"""   Tue Jun 23 16:26:13 2020   @author: ERTURK
"""

prompt= "\nTell me something, and I will repeat it back to you:"
prompt +="\n Enter 'quit' to end the program. "

active = True
while active:
    message=input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)



###### daha güzeli
        
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to "+ city.title()+"!")