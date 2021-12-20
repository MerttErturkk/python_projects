# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 17:43:25 2021

@author: mertt
"""

import numpy as np

from scipy import sparse



eye = np.eye(4)
print("{}".format(eye))


sparse_matrix = sparse.csr_matrix(eye)
print("\n sparse :\n{}".format(sparse_matrix))

# =============================================================================
# FOR DENSE REPRESENTATION BETTER USE COO
# =============================================================================
data = np.ones(4)
row_indices=np.arange(4)
col_indices = np.arange(4)

eye_coo =sparse.coo_matrix((data, (row_indices, col_indices)),shape=(4,4))
print("\n COO: \n{}".format(eye_coo))


