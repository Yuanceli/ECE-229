#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import numpy as np
import itertools
def get_coupon_Markov_graph(probs):
    '''
    return a Networkx graph (i.e., NetworkX DiGraph) with edges corresponding to the transition probabilities
    '''
    assert isinstance(probs, list)
    assert sum(probs)==1
    states = [()]
    for c in range(1, len(probs)+1):
        for x in itertools.combinations(range(1, len(probs)+1),c):
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
    
    G = nx.DiGraph()
    G.add_nodes_from(states)
    for i, origin_state in enumerate(states):
        for j, destination_state in enumerate(states):
            if trans[i][j] > 0:
                G.add_edge(origin_state, destination_state, weight=trans[i][j],)
    return G

