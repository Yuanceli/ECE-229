#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats,integrate
def true_detection_probability(thresh):
    '''
    return P(D)
    '''
    assert isinstance(thresh,(float,int))
    assert 0<=thresh<=np.sqrt(2)
    f = lambda t: np.piecewise(t, [0<=t<=1, 1<t<=np.sqrt(2)], [lambda r: 2/np.pi, lambda r: 2/np.pi / (np.sqrt(r**2-1)) * (2/r - r)])
    value,_ = integrate.quad(lambda c: f(c), thresh, np.sqrt(2))
    return value

