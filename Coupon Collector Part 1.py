#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
def sim_avg_coupons(probs,ntrials=1000):
    '''
    Write a simulation to compute the average number of boxes required if all  n  coupons do not have the same probability.
    '''
    assert isinstance(probs, np.ndarray)
    assert sum(probs)==1
    assert isinstance(ntrials, int)
    assert ntrials > 0
    s = 0
    for t in range(ntrials):
        trys = 0
        taken = []
        while sum(set(taken)) != 1:
            taken.append(random.choices(list(probs), weights=probs)[0])
            trys += 1
        s += trys
    return s / ntrials

