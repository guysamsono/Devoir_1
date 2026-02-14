import numpy as np


def normL1(discretization,concentration,concentration_analytique):
    norm = 0
    nb_points = len(discretization)

    for i in range(len(discretization)):
        
        norm += abs(concentration[i] - concentration_analytique[i])
    norm /= nb_points

    return norm

def normL2(discretization,concentration,concentration_analytique):

    norm = 0 
    nb_points = len(discretization)
    for i in range(len(discretization)):
        norm += (concentration[i] - concentration_analytique[i])**2
        
    norm /= nb_points
    norm  = norm**(1/2)
    return norm


def norm_Infinity(discretization,concentration,concentration_analytique):
    norm = 0
    error = 0

    for i in range(len(discretization)):
        error = abs(concentration[i] - concentration_analytique[i])
        if error > norm:
            norm = error
    return norm


