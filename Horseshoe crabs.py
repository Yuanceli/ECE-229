#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statsmodels.api as sm
def horseshoe1(data):
    '''
    fit a Generalized Linear Model with a Poisson family and y as a function of width
    '''
    assert isinstance(data,pd.DataFrame)
    model = sm.GLM(data['y'],data['width'],family=sm.families.Poisson())
    res = model.fit()
    return res.deviance

def horseshoe2(data):
    '''
    y as a function of width and weight
    '''
    assert isinstance(data,pd.DataFrame)
    model = sm.GLM(data['y'],data[['width','weight']],family=sm.families.Poisson())
    res = model.fit()
    return res.deviance

def horseshoe3(data):
    '''
    :param data:
    :return:
    '''
    assert isinstance(data,pd.DataFrame)
    model = sm.GLM(data['y'],data[['width','weight']],family=sm.families.NegativeBinomial())
    res = model.fit()
    return res.deviance

