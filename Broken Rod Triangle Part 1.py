#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import random as rd
def sim_triangle(n=100):
    '''
    A rod of unit length is broken in two places uniformly at random.
    What is the probability that the 3 fragments form a triangle?
    Parameter: n (number of trials)
    Output: probability of success
    '''
    count = 0
    for i in range(n):
        t = []
        p1 = rd.random()
        p2 = rd.random()
        t.append(min(p1, p2))
        t.append(abs(p2 - p1))
        t.append(1 - max(p1, p2))
        order = sorted(t)
        if order[0] + order[1] > order[2]:
            count += 1
    return count/n

