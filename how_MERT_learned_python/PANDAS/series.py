# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = np.array(["mert","engin","salih"])
s = pd.Series(data)

data2 = {"matematik":10,"fizik":20,"kimya":100}
s2 = pd.Series(data2,index = ["fizik","matematik","kimya"])
#index verir istersen yerleri değiştirir.
print(s2[0])# fizik 0. eleman olarak atandı, indexi 0.


s3 = pd.Series(5, index=[1])
print(s3[1]) # 5 in indexi 1 default olsaydı 0 dı.

print("\n")
print(s2)