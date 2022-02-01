# -*- coding : utf-8 -*- 
import numpy as np
import math

####################
###Excercice 3####
####################

def bsm_call_value(S0, K, T, r, sigma): 
    S0 = float(S0)
    d1 = (np.log(S0 /K) + (r + 0.5 * sigma**2) * T )/(sigma * np.sqrt(T))
    d2 = (np.log(S0 /K) + (r - 0.5 * sigma**2) * T )/(sigma * np.sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * stats.norm.cdf(d2, 0, 1))
    return value
    

def bsm_vega(S0, K, T, r, sigma): 
    S0 = float(S0)
    d1 = (np.log(S0/K)) + (r+0.5*sigma**2)*T /(sigma*sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0, 1) * np.sqrt(T)
    return vega
 

