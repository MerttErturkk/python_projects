# -*- coding: utf-8 -*-
"""   Tue Jun 23 16:56:42 2020   @author: ERTURK
"""


unconfirmed_users=["alice","brian","candace"]
confirmed_users=[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying user: "+current_user.title())
    confirmed_users.append(current_user)
    
    


pets= ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while "cat" in pets:
    pets.remove("cat")

print(pets)