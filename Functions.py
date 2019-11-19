import numpy as np
import pandas as pd

k = 6

a2 = np.array([0.,0.5,3,9,99,99])
a3 = np.array([0.,0.5,1.,1.5,2.,2.5])
a4 = np.array([1.,2.,3.,4.,5.,6.])
a5 = np.array([1.,2.,4.,8.,16.,32.])
b3 = np.array([6.42,6.42,6.42,6.42,6.42,6.42])

def A1(sm):
    return pd.Series([np.prod(sm.T.iloc[:j+1])*(-1)**(j+1) for j in range(k)]).sum()

def A2(sm):
    return pd.Series([(np.abs(4*sm[j]-2)+a2[j])/(1+a2[j]) for j in range(k)]).product()

def A3(sm):
    return pd.Series([(np.abs(4*sm[j]-2)+a3[j])/(1+a3[j]) for j in range(k)]).product()

def A4(sm):
    return pd.Series([(np.abs(4*sm[j]-2)+a4[j])/(1+a4[j]) for j in range(k)]).product()

def A5(sm):
    return pd.Series([(np.abs(4*sm[j]-2)+a5[j])/(1+a5[j]) for j in range(k)]).product()

def A2b(sm,sn):
    return pd.Series([(np.abs(4*(sm[j]+sn[j]-np.modf(sm[j]+sn[j])[1])-2)+a2[j])/(1+a2[j]) for j in range(k)]).product()

def B1(sm):
    return pd.Series([(k-sm[j])/(k-0.5) for j in range(k)]).product()
        
def B2(sm):
    return ((1+1/k)**k)*pd.Series([sm[j]**(1/k) for j in range(k)]).product()
        
def B3(sm):
    return pd.Series([(np.abs(4*sm[j]-2)+b3[j])/(1+b3[j]) for j in range(k)]).product()
        
def C1(sm):
    return pd.Series([np.abs(4*sm[j]-2) for j in range(k)]).product()
        
def C2(sm):
    return sm.product(axis=1)*2**k

def Ishigami(sm):
    return np.sin(sm[0]) + 7.*np.sin(sm[1])**2 + 0.1*sm[2]**4 * np.sin(sm[0])

