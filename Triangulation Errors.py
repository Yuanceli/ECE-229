import numpy as np
from scipy.optimize import minimize

def get_corrections(h1,h2,h3,theta1,theta2,theta3):
    '''
    returns a tuple of the corrections as  (δ1,δ2,δ3)
    '''
    fun = lambda phi : (theta1-phi[0])**2 + (theta2-phi[1])**2 + (theta3-phi[2])**2
    cons = {'type': 'eq', 'fun': lambda phi: (np.tan(phi[0])-np.tan(phi[1]))*(h3-h1)-(np.tan(phi[0])-np.tan(phi[2]))*(h2-h1)}
    # cons = {'type': 'eq', 'fun': lambda phi: a*(phi[0]-phi[2])-b*(phi[0]-phi[1])}
    phi0 = np.array([theta1, theta2, theta3])
    res = minimize(fun, phi0, method='SLSQP', constraints=cons)
    return(tuple(res.x-phi0))
def get_x(h1, h2, h3, the1, the2, the3):
    '''
    return x based on recounstruction of phi
    '''
    d1, d2, d3 = get_corrections(h1, h2, h3, the1, the2, the3)
    phi1 = the1+d1
    phi2 = the2+d2
    phi3 = the3+d3
    #print(d1, d2, d3)
    return (h3-h1) / (np.tan(phi1) - np.tan(phi3))
def get_z(h1, h2, h3, the1, the2, the3):
    '''
    return x based on recounstruction of phi
    '''
    d1, d2, d3 = get_corrections(h1, h2, h3, the1, the2, the3)
    phi1 = the1+d1
    phi2 = the2+d2
    phi3 = the3+d3   
    return ((h3-h1) / (np.tan(phi1) - np.tan(phi3))) * np.tan(phi1) + h1
    
def get_stats_x(h1,h2,h3,phi1,phi2,phi3,sigma):
    '''
    returns the mean and variance for x as a numerical tuple
    '''
    phi = np.array([phi1, phi2, phi3])
    thetas = np.random.randn(2000, 3)*sigma + phi
    print(thetas[0])
    x = np.array([get_x(h1, h2, h3, th[0], th[1], th[2]) for th in thetas])
    return (np.mean(x), np.var(x))


def get_stats_z(h1,h2,h3,phi1,phi2,phi3,sigma):
    '''
    returns the mean and variance for z as a numerical tuple
    '''
    phi = np.array([phi1, phi2, phi3])
    h = np.array([h1, h2, h3])
    thetas = np.random.randn(2000, 3)*sigma + phi
    tans = np.tan(thetas)
    z = np.array([get_z(h1, h2, h3, th[0], th[1], th[2]) for th in thetas])
    return (np.mean(z), np.var(z))