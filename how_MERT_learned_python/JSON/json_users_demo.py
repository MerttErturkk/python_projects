# -*- coding: utf-8 -*-
"""   Mon Jun 22 19:01:39 2020   @author: ERTURK
"""

import json

with open("users.json") as users:
    data = json.load(users)
    print(data)
print("\n\n\n\n\n\n")

for x in range(5):
    print (data[x])
    print (data[x]["username"])
    print (data[x]["address"])
    print (data[x]["address"]["street"])
    print (data[x]["address"]["geo"]["lat"])
    print("\n")

