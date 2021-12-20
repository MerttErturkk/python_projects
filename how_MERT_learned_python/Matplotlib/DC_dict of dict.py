# -*- coding: utf-8 -*-
"""   Wed Jun 16 16:18:12 2021   @author: ERTURK
"""


europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


print(europe["france"]["capital"])

# Create sub-dictionary data
data={"capital":"rome","population":59.83}

# Add data to europe under key 'italy'
europe["italy"]=data
print(europe)


print("\n\n")
print("italy" in europe)



del(europe["italy"])
print("\n\n")
print("italy" in europe)