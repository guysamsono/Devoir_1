"""
Module de calcul de la MMS (conditions frontières)
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


Ce = 20
R = 0.5
D_eff = 1e-10
K = 4e-9

# Définition des variables symboliques
t, r,R = sp.symbols('t r R')

# Solution manufacturée
C_MMS = Ce + 10*sp.exp(-t*0.001)*(1-(r/R)**2)  


# Calcul des dérivées
C_t = sp.diff(C_MMS, t)
C_r = sp.diff(C_MMS, r)
C_rr = sp.diff(C_MMS, r, r)

#Calcul du terme source S(t,r)
source = C_t - D_eff*(C_rr + (1/r)*C_r) + K*C_MMS

#Conditions aux limites et initiales
C_initial = C_MMS.subs(t, 0)
C_boundary_re = C_MMS.subs(r, R)
dCdr_boundary_ri = sp.diff(C_MMS, r).subs(r, 0)


# Affichage des dérivées
print("Dérivée en temps :")
print(C_t)
print("Dérivée première :")
print(C_r)
print("Dérivée seconde :")
print(C_rr)
print("Terme source :")
print(source)
print("\nCondition initiale T(0, x) :")
print(C_initial)
print("\nCondition frontière T(t,1) :")
print(C_boundary_re)
print("\nCondition frontière Neumann dT/dx(t,0) :")
print(dCdr_boundary_ri)

# Conversion en fonctions Python
f_C_MMS = sp.lambdify([t, r], C_MMS, "numpy")
f_source = sp.lambdify([t, r], source, "numpy")

# Définition des paramètres
tmin, tmax = 0, 2000
rmin, rmax = 0, 0.5
nt, nr = 100, 100

# Création des maillages temporel et spatial
tdom = np.linspace(tmin, tmax, nt)
rdom = np.linspace(rmin, rmax, nr)
ti, ri = np.meshgrid(tdom, rdom, indexing='ij')

# Évaluation des fonctions sur le maillage
z_MMS = f_C_MMS(ti, ri)
z_source = f_source(ti, ri)  # Supposons alpha = 1 pour visualisation

# Tracé de la solution manufacturée
plt.figure()
contour1 = plt.contourf(ri, ti, z_MMS, levels=50)
cbar1 = plt.colorbar(contour1)
cbar1.set_label('Concentration [mol/m³]')
plt.title('Solution manufacturée C(t,r)')
plt.xlabel('r [m]')
plt.ylabel('t [s]')
plt.show()


# Tracé du terme source
plt.figure()
contour2 = plt.contourf(ri, ti, z_source, levels=50)
cbar2 = plt.colorbar(contour2)
cbar2.set_label('Source S(t,r) [mol m⁻³ s⁻¹]')
plt.title('Terme source de la MMS')
plt.xlabel('r [m]')
plt.ylabel('t [s]')
plt.show()