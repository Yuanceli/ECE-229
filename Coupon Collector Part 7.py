#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def get_mean_boxes(probs):
    '''
    compute the mean number of boxes until all coupons are collected
    '''
    assert isinstance(probs, list)
    assert 2<=len(probs)<=10
    assert sum(probs)==1
    n = 2**len(probs)
    trans = np.zeros((n, n))
    for i,p in enumerate(probs):
        for j in range(n):
            trans[j][j|(1<<i)] += p
    start = np.zeros((1, n-1))
    start[0][0] = 1
    ans = np.mat(start) * (np.mat(np.eye(n-1, n-1))-trans[0:n-1, 0:n-1]).I * np.ones((n-1, 1))
    return ans[0,0]

