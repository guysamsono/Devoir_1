import sympy as sp

def plotter():

    r = sp.symbols('r')
    concentration_analytique = 0.25*s*rayon**2*(r**2/rayon**2 - 1)/d_eff + ce

    concentration_vect_analytique = np.zeros(n_points*10)
    rayon_vect = np.linspace(ri,ro,n_points*10)
    for i in range(len(rayon_vect)):
        concentration_vect_analytique[i] = concentration_analytique.subs(r,rayon_vect[i])

    plt.plot(rayon_vect,concentration_vect_analytique, label = 'solution analytique')
    plt.plot(discretization,concentration_vect, label = 'solution approchée')
    plt.legend()
    plt.show()