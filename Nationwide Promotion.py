import numpy as np
import pandas as pd
from scipy.stats import multinomial, chi2

def compute_p_value(data):
    '''
    returns the p-value given input data
    '''
    assert isinstance(data, pd.DataFrame)
    n = np.array([sum(row) for _,row in data.iterrows()])
    total = sum(n)
    c = np.array([sum(data[idx]) for idx in data.columns])
    PH0 = c / total
    
    numer = np.sum([np.log(multinomial(sum(row), PH0).pmf(np.array(row))) for _,row in data.iterrows()])
    denom = np.sum([np.log(multinomial(sum(row), np.array(row)/sum(row)).pmf(np.array(row))) for _,row in data.iterrows()])
   
    chsq = chi2(6)
    logLambda = -2 * (numer-denom)
    
    return 1- chsq.cdf(logLambda)