from src.plotter import temperature_plotter
from src.solver import solver_first_order, solver_second_order, compute_conservation_of_energy, mms_Temperature
from input import gen_input
from src.symmetry import test_symmetrie
from src.mms import generer_mms_simple, mms_convergence_analysis
from src.error import *
from src.convergence import*

if __name__ == "__main__": 

    input_dict = gen_input()

    type_simul = 'temperature_mms'        #type de simulation à réaliser : 'symmetry_test' ou 'temperature' ou 'temperature_mms'
    order = '1'                         #ordre de la simulation : '1' pour ordre 1 et '2' pour ordre 2     

    if type_simul == 'symmetry_test':
        print('Test de symétrie en cours...')
        test_symmetrie(order, input_dict)
    
    if type_simul == 'temperature':
        print(f'Simulation de température en cours à ordre {order}...')
        if order == '1':
            temperature = solver_first_order(input_dict)
            srq = compute_conservation_of_energy(temperature, input_dict)
            print(f"Résidu de la conservation de l'énergie : {srq}")
        else:
            temperature = solver_second_order(input_dict)
            srq = compute_conservation_of_energy(temperature, input_dict)
            print(f"Résidu de la conservation de l'énergie : {srq}")
        
        temperature_plotter(temperature, input_dict)

    if type_simul == 'temperature_mms':

        f_T_MMS, f_source, f_bc_left, f_bc_right, f_bc_bottom, f_tinf_top = generer_mms_simple(input_dict, afficher_graphiques=True)

        temperature = solver_first_order(input_dict, sym_test = False, source_mms = f_source, 
                                         bc_left=f_bc_left, bc_right=f_bc_right, bc_bottom=f_bc_bottom, bc_top_tinf=f_tinf_top)

        mms_convergence_analysis(input_dict)

