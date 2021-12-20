# -*- coding: utf-8 -*-

import numpy as np


nums= np.array([0,5,10,15,20,25,30])

print(nums[6])
print(nums[0:3])

print("\n")


nums2=np.array([[0,5,10],[15,20,25]])
print(nums2[1])
print(nums2[1,2])
print(nums2[:,2]) # sol taraf satır sağ sütun
                  # her satırın 2. elemanı
print("\n")
print(nums2[:,0:2])



print(nums[::-1]) # tersten dizer


print(nums2[-1,:]) # son satır tüm stünlar