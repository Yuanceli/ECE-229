#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy import stats
import pandas as pd
def sim_ngon(n=3,ns=100):
    '''
    breaking the unit length rod in n pieces uniformly at random 
    returning the corresponding probability of using the so-generated fragments to create a valid n+1 polygon using ns simulation trials.
    '''
    assert isinstance(n, int) and isinstance(ns, int)
    assert n>=2 and ns>0
    df = pd.DataFrame()
    for i in range(n):
        df['x{}'.format(i+1)] = stats.uniform.rvs(size=ns)
    df.values.sort()
    
    df['l1'] = df.x1
    for i in range(n):
        if i == n-1:
            df['l{}'.format(i+2)] = 1 - df['x{}'.format(i+1)]
            break
        df['l{}'.format(i+2)] = df['x{}'.format(i+2)] - df['x{}'.format(i+1)]
        
    df['s'] = (df['l1']<0.5)
    for i in range(n):
        df['s'] &= (df['l{}'.format(i+2)]<0.5)
    return np.mean(df.s)

def prob_n_breaks(n=4):
    '''                                                                        
    compute the probability of forming a nonzero area polygon with `n` breaks.                                          
    Note that `n` breaks creates a `n+1` polygon. 
    '''
    assert isinstance(n, int)
    assert n>=2
    return 1-(n+1)*(0.5)**n

