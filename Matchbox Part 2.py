#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rd
def sim_chain(init_state=(2,2),pL=1/2):
    '''
    generator should yield the next  si,j  state as a tuple
    '''
    assert (isinstance(init_state, tuple) and len(init_state)==2)
    for x in init_state:
        assert isinstance(x,int)
        assert x>=0
    assert 0<=pL<=1
    s = init_state
    while s[0]*s[1] != 0:
        if rd.random() <= pL:
            s = (s[0]-1, s[1])
        else:
            s = (s[0], s[1]-1)
        yield s

