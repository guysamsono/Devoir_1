import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def first_order(n_points=100, ri=0, ro=0.5, s=2e-8, d_eff=1e-10,ce=20):

    discretization = np.linspace(ri, ro, n_points)
    dr = discretization[1] - discretization[0]

    a = np.zeros((n_points, n_points))
    b = np.ones(n_points)*s

    a[0][0] = -1
    a[0][1] = 1
    a[-1][-1] = 1
    b[-1] = ce

    for i in range(1,n_points-1):

        a[i][i-1] = d_eff/(dr**2)
        a[i][i] = -2*d_eff/(dr**2) - d_eff/(discretization[i]*dr) 
        a[i][i+1] = d_eff/(discretization[i]*dr) + d_eff/(dr**2)

    concentration_vect = np.linalg.solve(a,b)

    return discretization, concentration_vect

def second_order(n_points=100, ri=0, ro=0.5, s=2e-8, d_eff=1e-10,ce=20):

    discretization = np.linspace(ri, ro, n_points)
    dr = discretization[1] - discretization[0]

    a = np.zeros((n_points, n_points))
    b = np.ones(n_points)*s

    a[0][0] = -3
    a[0][1] = 4
    a[0][2] = -1
    a[-1][-1] = 1
    b[-1] = ce

    for i in range(1,n_points-1):

        a[i][i-1] = d_eff/(dr**2) - d_eff/(2*discretization[i]*dr)
        a[i][i] = -2*d_eff/(dr**2) 
        a[i][i+1] = d_eff/(2*discretization[i]*dr) + d_eff/(dr**2)

    concentration_vect = np.linalg.solve(a,b)
    

    return discretization, concentration_vect

discretization, concentration_vect = second_order()

