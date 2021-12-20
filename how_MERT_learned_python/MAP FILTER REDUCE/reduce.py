# -*- coding: utf-8 -*-

nums = [1,2,3,4,5]

from functools import reduce

nums_factor = reduce(lambda x,y: x*y , nums)
print(nums_factor)