#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def get_3coupon_MarkovMatrix(probs):
    '''
    return a Markov Chain transition matrix (Numpy array) for the probs (Numpy array) coupons
    '''
    assert isinstance(probs, np.ndarray)
    assert sum(probs)==1
    coupons = len(probs)
    assert coupons==3
    '''
    keys = [()]
    for c in range(1, coupons+1):
        for x in itertools.combinations(range(1, coupons+1),c):
            keys.append(x)
    values = [i for i in range(2**coupons)]
    state = dict(zip(keys,values))
    '''
    trans = np.zeros((2**coupons,2**coupons))
    trans[0,1:coupons+1] = probs
    trans[1, [1,4,6]] = probs[[0,1,2]]
    trans[2, [2,4,5]] = probs[[1,0,2]]
    trans[3, [3,5,6]] = probs[[2,1,0]]
    trans[4, [4,7]] = [probs[0]+probs[1], probs[2]]
    trans[5, [5,7]] = [probs[1]+probs[2], probs[0]]
    trans[6, [6,7]] = [probs[0]+probs[2], probs[1]]
    trans[7, 7] = 1
    return trans

