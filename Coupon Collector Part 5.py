#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import itertools
import random
def sim_nxgraph_coupon(probs,nsteps):
    '''
    simulate iterating nsteps into the Markov chain
    '''
    assert isinstance(probs, list)
    assert sum(probs)==1
    assert isinstance(nsteps, int)
    assert nsteps > 0
    states = [()]
    for c in range(1, len(probs)+1):
        for x in itertools.combinations(range(0, len(probs)),c):
            states.append(x)
                
    trans = np.zeros((2**len(probs),2**len(probs)))
    for i, start in enumerate(states):
        for j, end in enumerate(states):
            if len(start) + 1 == len(end) and all(ele in end for ele in start):
                trans[i,j] = probs[next(iter((set(end)-set(start))))-1]
            if i==j:
                useful = 0
                for c in start:
                    useful += probs[c-1]
                trans[i,i] = useful
                
    outlist = [()]
    for t in range(nsteps):
        start = states.index(outlist[-1])
        outlist.append(random.choices(list(states), weights=trans[start,:])[0])
    return outlist

