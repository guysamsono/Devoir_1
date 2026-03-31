from src.solver import solver_first_order, solver_second_order
from src.plotter import temperature_plotter
import numpy as np

def test_symmetrie(order, input_dict):

    assert order in ['1', '2'], "Order must be either 1 or 2"

    if order == '1':
        t_normal_order = solver_first_order(input_dict)
        temperature_plotter(t_normal_order, input_dict, 'normal_domain_test_first_order.png')
    else:
        t_normal_order = solver_second_order(input_dict)
        temperature_plotter(t_normal_order, input_dict, 'normal_domain_test_second_order.png')

    c0 = input_dict['c']
    ny0 = input_dict['ny']

    input_dict['c'] = 2 * c0
    input_dict['ny'] = 2 * ny0

    if order == '1':
        t_sym = solver_first_order(input_dict, True)
        temperature_plotter(t_sym, input_dict, 'symmetrised_domain_test_first_order.png')
    else:
        t_sym = solver_second_order(input_dict, True)
        temperature_plotter(t_sym, input_dict, 'symmetrised_domain_test_second_order.png')
        
    l2_norm = np.linalg.norm(t_normal_order - t_sym[ny0*input_dict['nx']:ny0**2*input_dict['nx']])
    print(f"norme L2 de l'erreur sur le domaine symétrisé: {l2_norm}")

    return