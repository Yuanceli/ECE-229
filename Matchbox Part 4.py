#!/usr/bin/env python
# coding: utf-8

# In[2]:


import functools
import numpy as np
@functools.lru_cache()
def get_Smn(m,n,i,j,pL=0.5):
    '''
    The more general case with unbalanced probabilities is a little more involved
        Sm,n(i,j)=pL Sm−1,n(i,j) + (1−pL) Sm,n−1(i,j)
    where  pL  is the probability of selecting the left pocket 
    and  Sm,n(i,j)  is the probability of starting with  m  matches in the left pocket and  n  matches in the right pocket 
    and terminating with  i  matches in the left pocket and  j  matches in the right pocket.
    
        the boundary conditions
            Sm,0(m,0) = S0,n(0,n)=1
        and
            Sm,0(i,j) = S0,n(i,j)=0
    '''
    assert isinstance(m,int) and m>=0
    assert isinstance(n,int) and n>=0
    assert isinstance(i,int) and 0<=i<=m
    assert isinstance(j,int) and 0<=j<=n
    assert 0<=pL<=1
    s = np.zeros((m+1,n+1))
    s[i,0] = s[0,j] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            s[i,j] = pL * s[i-1,j] + (1-pL) * s[i,j-1]
    return s[m,n]

