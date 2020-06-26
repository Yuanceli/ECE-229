#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import itertools
def get_coupon_MarkovMatrix(probs):
    '''
    return a Markov Chain transition matrix (Numpy array) for the probs (Numpy array) coupons
    '''
    assert isinstance(probs, list)
    assert 1<=len(probs)<=10
    assert sum(probs)==1
    states = [()]
    for c in range(1, len(probs)+1):
        for x in itertools.combinations(range(1, len(probs)+1),c):
            states.append(x)
            
    trans = np.zeros((2**len(probs),2**len(probs)))
    for i, start in enumerate(states):
        for j, end in enumerate(states):
            if len(start) + 1 == len(end) and all(ele in end for ele in start):
                trans[i,j] = probs[next(iter((set(end)-set(start))))-1]
            if i==j:
                useful = 0
                for c in start:
                    useful += probs[c-1]
                trans[i,i] = useful
    return trans

