import numpy as np
def gen_transition_matrix(init_state=(2,2),pL=0.5):
    '''
    There is a matchbox containing  N  matches in both the left and right-side pockets. 
    A box is selected uniformly at random and a match is taken and discarded.
    We can enumerate the states,  si,j  where there are  i  matches in the left box and  j  in the right.
    '''
    assert (isinstance(init_state, tuple) and len(init_state)==2)
    for x in init_state:
        assert isinstance(x,int)
        assert x>=0
    assert 0<=pL<=1
    state = {}
    for i in range(init_state[0]+1):
        for j in range(init_state[1]+1):
            if i==0 and j==0:
                continue
            state[(i,j)] = i*(init_state[1]+1) + j-1
    mat = np.zeros((len(state),len(state)))
    for i in range(init_state[0]+1):
        for j in range(init_state[1]+1):
            if i+j==0:
                continue
            elif i*j==0:
                mat[state[(i,j)],state[(i,j)]] = 1
            else:
                mat[state[(i,j)],state[(i-1,j)]] = pL
                mat[state[(i,j)],state[(i,j-1)]] = 1-pL
    return mat,state

