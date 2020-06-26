#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats,integrate
def false_alarm_probability(thresh):
    '''
    return P(fa)
    '''
    assert isinstance(thresh,(float,int))
    assert 0<=thresh<=np.sqrt(2)
    err = lambda t: stats.norm(0, 0.1).pdf(t)
    value,_ = integrate.quad(lambda c: err(c), thresh, np.sqrt(2))
    return value

