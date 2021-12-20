# -*- coding: utf-8 -*-
"""   Mon Jun 22 17:05:39 2020   @author: ERTURK
"""






import json

# string bi datayı json a çevirmek
data = '{"firstname":"mert","lastname":"erturk"}'
y =json.loads(data)
print(type(y))




#dictionary to json conversion

customer ={"firstname":"engin",
           "email":"engin@hotmail.com"
           }
customer_json=json.dumps(customer)
print(customer)
print("")
print(customer_json)


