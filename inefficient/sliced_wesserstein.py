import numpy as np
from sympy import mpmath
import os
from scipy.spatial.distance import cityblock
import pandas as pd
from itertools import combinations
import cPickle as pk

#-------------------------------------------------
def sliced_wesserstein(PD1,PD2, M=50):#,sigma
    diag_theta = np.array([mpmath.cospi(1/4.),mpmath.sinpi(1/4.)], dtype=np.float32)
    SWkernel = {}
    # get ids
    D1 = PD1[['birth','death']].values
    D2 = PD2[['birth','death']].values
    l_theta1 = map(lambda x: np.dot(diag_theta, x), D1)
    l_theta2 = map(lambda x: np.dot(diag_theta, x), D2)
    if (len(l_theta1)!=try1.shape[0]) or (len(l_theta2)!=try2.shape[0]):
	raise ValueError('The projected points and origin do not match') 
    PD_delta1 = np.array(map(lambda x: [np.sqrt(x**2/2.)]*2, l_theta1))
    PD_delta2 = np.array(map(lambda x: [np.sqrt(x**2/2.)]*2, l_theta2))
    del l_theta1,l_theta2, try1, try2
    # i have the input now to compute the SW
    SW = 0
    theta = .5
    step = 1./M
    for i in range(M):
	l_theta = np.array([mpmath.cospi(theta),mpmath.sinpi(theta)], dtype=np.float32)
	V1 = map(lambda x: np.dot(l_theta, x), D1)
	V1.extend(map(lambda x: np.dot(l_theta, x), PD_delta2))
	V2 = map(lambda x: np.dot(l_theta, x), D2)
	V2.extend(map(lambda x: np.dot(l_theta, x), PD_delta1))
	SW += step*cityblock(sorted(V1),sorted(V2))
	theta += step
    SWkernel.setdefault(E1,{})
    SWkernel.setdefault(E2,{})
    #top = - SW*step
    #bottom = 2.*sigma
    return SW
