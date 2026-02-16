from src.solver.solver import first_order, second_order, analytique
from src.postprocessing.plotter import plotter

def gen_symetrie(params:dict, n_points=30):

    '''
    Passe le test de symétrie et produit les graphiques associés
    
    :param params: paramètres de la simulation
    :param n_points: nombre de point sur le domaine
    '''
    if n_points % 2 !=0:
        n_points += 1

    params["RI"] = -params["RO"]
    
    discretization_first_order, concentration_vect_first_order = first_order(params,n_points)
    discretization_second_order, concentration_vect_second_order = second_order(params,n_points)
    discretization_a, concentration_a = analytique(params)

    plotter(params,discretization_first_order,concentration_vect_first_order,discretization_a,concentration_a,"1",'results/sym_ordre_1.png',True)
    plotter(params,discretization_second_order,concentration_vect_second_order,discretization_a,concentration_a,"2",'results/sym_ordre_2.png',True)

    return