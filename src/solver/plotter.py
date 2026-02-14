import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plotter(discretization,concentration_vect,discretization_anal,concentration_analy, order, ri=0, ro=0.5, s=2e-8, d_eff=1e-10,ce=20):

    '''
    Fonction qui trace la solution approchée ainsi que la solution analytique
    
    :param discretization: position sur le rayon
    :param order: ordre du schéma (str)
    :param concentration_vect: résultat de concentration
    :param ri: rayon initial
    :param ro: rayon final
    :param s: terme source s = 2e-8
    :param d_eff: concentration de sel dans la structure poreuse d_eff = 1e-10
    :param ce: concentration de sel à la surface du béton
    '''
  
    

    plt.plot(discretization_anal,concentration_analy, label = 'solution analytique')
    plt.scatter(discretization,concentration_vect, label = 'solution approchée', color = 'orange')
    plt.title(f"Profil de concentration dans une colone de béton grâce à un schéma d'ordre {order}")
    plt.legend()
    plt.show()

    