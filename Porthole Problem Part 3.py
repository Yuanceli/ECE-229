from scipy import stats,integrate
import numpy as np
def conditional_prob_H0(x):
    '''
    evaluates the conditional probability density for the sensor return under the hypothesis of signal-absent  H0
    '''
    assert 0<=x<=np.sqrt(2)
    return stats.norm(0, 0.1).pdf(x)

def conditional_prob_H1(x):
    '''
    evaluates the conditional probability density for the sensor return under the hypothesis of signal-present  H1
    '''
    assert 0<=x<=np.sqrt(2)
    f = lambda t: np.piecewise(t, [0<=t<=1, 1<t<=np.sqrt(2)], [lambda r: 2/np.pi, lambda r: 2/np.pi / (np.sqrt(r**2-1)) * (2/r - r)])
    err = lambda t: stats.norm(0, 0.1).pdf(t)
    value,_ = integrate.quad(lambda L: err(x-L) * f(L), 0, np.sqrt(2))
    return value
