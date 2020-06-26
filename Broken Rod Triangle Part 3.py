#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy import stats,integrate
import numpy as np
def beta_obj(a,b):
    '''
    A rod of unit length is broken in two places uniformly at random.
    Numerically evaluate the probability of a valid triangle for 1<= a <=20 and 1<= b <=20 over integers.
    Return the numerical probability of a valid triangle as a floating-point number given a and b.
    '''
    assert isinstance(a, int) and isinstance(b, int)
    assert 1<= b <=20 and 1<= b <=20
    x = np.linspace(stats.beta.ppf(0, a, b),stats.beta.ppf(1, a, b), 100)
    y = np.linspace(stats.beta.ppf(0, a, b),stats.beta.ppf(1, a, b), 100)
    value,_ = integrate.dblquad(lambda x,y: stats.beta.pdf(x,a,b) * stats.beta.pdf(y,a,b), 0.5, 1, lambda y: y-0.5, 0.5)
    return 2*value

