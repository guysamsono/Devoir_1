import numpy as np

from src.solver.solver import*
from src.solver.plotter import*
from src.Verification.error import*
import matplotlib.pyplot as plt

N_list = np.unique(np.round(np.logspace(1, 4, 9)).astype(int))  


# discretization, concentration_vect = second_order(10000)
# discretization_anal, concentration_analytique = analytique(10000)

# plotter_sol(discretization,concentration_vect,discretization_anal,concentration_analytique,2)

# normL2 = normL2(discretization,concentration_vect,concentration_analytique)

# print(normL2)

###Analyse de convergence

E1 = []
E2 = []
Einf = []
h_list = []

for N in N_list:
    dis_num, c_num = first_order(N)
    dis_ana, c_ana = analytique(N)


    h = abs(dis_num[1] - dis_num[0])
    h_list.append(h)

    E1.append(normL1(dis_num,c_num,c_ana))
    E2.append(normL2(dis_num,c_num,c_ana))
    Einf.append(norm_Infinity(dis_num,c_num,c_ana))


plt.figure()
plt.loglog(h_list, E1, 'o-', label='L1')
plt.loglog(h_list, E2, 's-', label='L2')
plt.loglog(h_list, Einf, '^-', label='L∞')
plt.gca().invert_xaxis()  # h diminue vers la droite (optionnel mais courant)
plt.xlabel("h")
plt.ylabel("Erreur")
plt.title("Convergence (erreur vs h)")
plt.grid(True, which="both")
plt.legend()
plt.show()