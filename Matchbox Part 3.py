#!/usr/bin/env python
# coding: utf-8

# In[2]:


import functools
import numpy as np
@functools.lru_cache()
def get_Smk(m,n,k):
    '''
    Sm,n(k) is the probability of starting with m matches in the left pocket and n matches in the right pocket 
    and terminating with k matches in the not-selected pocket.
    
    Sm,n(k)=1/2 * Sm−1,n(k) + 1/2 * Sm,n−1(k)
        with boundary conditions
            Sm,0(m) = S0,n(n)=1
        and otherwise,
            Sm,0(k) = S0,n(k)=0
    '''
    assert isinstance(m,int) and m>=0
    assert isinstance(n,int) and n>=0
    assert isinstance(k,int) and 1<=k<=min(m,n)
    s = np.zeros((m+1,n+1))
    s[k,0] = s[0,k] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            s[i,j] = 1/2 * s[i-1,j] + 1/2 * s[i,j-1]
    return s[m,n]

