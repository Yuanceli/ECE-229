#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
from scipy import stats
from statistics import mean
def sim_triangle_beta(n=100,a=1,b=1):
    '''
    A rod of unit length is broken in two places uniformly at random.
    breaking according to a Beta distribution with parameters a,b
    Parameter: n (number of trials)
    Output: probability of success
    '''
    assert isinstance(a, int) and isinstance(b, int) and isinstance(n, int)
    assert n>0 and a>0 and b>0
    df = pd.DataFrame(columns = ['x1','x2','l1','l2','l3'])
    df.x1, df.x2 = stats.beta(a,b).rvs([2,n])
    df.l1 = df[['x1','x2']].min(axis=1)
    df.l2 = abs(df.x2 - df.x1)
    df.l3 = 1 - df[['x1','x2']].max(axis=1)
    df['s'] = np.logical_and.reduce((df.l1<0.5, df.l2<0.5, df.l3<0.5))
    return mean(df.s)

