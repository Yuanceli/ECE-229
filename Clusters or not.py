from scipy import stats,integrate
import numpy as np
def compute_cdf(d):
    '''compute the cumulative density function of the squared distances between n points in your data'''
    assert isinstance(d,float) or isinstance(d,np.ndarray)
    if isinstance(d,float):
        f = lambda t: 2*(1-t) if 0<=t<=1 else 0
        value,_ = integrate.dblquad(lambda x,y: f(x) * f(y), 0, np.sqrt(d), lambda y: 0, lambda y: np.sqrt(d-y**2))
        return np.array(value)
    else:
        v=[]
        for ind,item in enumerate(d):
            f = lambda t: 2*(1-t) if 0<=t<=1 else 0
            value,_ = integrate.dblquad(lambda x,y: f(x) * f(y), 0, np.sqrt(item), lambda y: 0, lambda y: np.sqrt(item-y**2))
            v.append(value)
        return np.array(v)

def compute_test_pvalue(X):
    '''
    compute the p-value using the Kolmogorov-Smirnov test
    '''
    assert isinstance(X,np.ndarray)
    assert np.size(X,1)==2
    n = np.size(X,0)
    np.random.shuffle(X)
    D = np.zeros(n//2)
    for i in range(n//2):
        D[i] = (X[i,0] - X[i+n//2,0])**2 + (X[i,1] - X[i+n//2,1])**2
    '''
    D=[]
    for i in range(n-1):
        for j in range(i+1,n):
            D.append((X[i,0] - X[j,0])**2 + (X[i,1] - X[j,1])**2)
            '''
    _,p=stats.kstest(np.array(D),compute_cdf)
    return p