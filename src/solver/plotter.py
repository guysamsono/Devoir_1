"""
Fonctions servant à afficher les résultats.
"""
import matplotlib.pyplot as plt

def plotter(params:dict, discretization, concentration_vect,
            discretization_a, concentration_a,
            order, save_path="results/temp.png",
            show_fig=False):
    '''
    Fonction qui trace la solution approchée ainsi que la solution analytique.
    
    :param params: paramètres du problème
    :param discretization: position sur le rayon
    :param concentration_vect: résultat de concentration
    :param discretization_a: position sur le rayon analytique
    :param concentration_a: résultat de concentration analytique
    :param order: ordre du schéma (str)
    :save_path: path de sauvegarde de la figure
    :show_fig: option pour afficher le graphique
    '''
    n_points = len(discretization)
    plt.figure(figsize=(8,6))
    plt.plot(discretization_a, concentration_a, label='Solution analytique')
    plt.scatter(discretization, concentration_vect, label='Solution approchée', color='orange')
    plt.title(f"Profil de concentration dans une colonne de béton\n"
             f"approximé par un schéma d'ordre {order} avec {n_points} points\n"
             f"utilisant ri={params['RI']}, ro={params['RO']}, "
             f"s={params['S']}, d_eff={params['D_EFF']}, ce={params['CE']}")
    plt.xlabel(r"Rayon $r$ [$m$]")
    plt.ylabel(r"Concentration $C$ [$mol/m^3$]")
    plt.grid()
    plt.legend()
    plt.savefig(save_path, dpi=300)
    if show_fig:
        plt.show()
    plt.close()

def graph_error_log(params:dict, discretization,
                    l1_list, l2_list, linf_list,
                    order, save_path="results/temp.png",
                    show_fig=False):
    '''
    Fonction qui affiche les erreurs par rapport à la solution analytique.
    
    :param params: paramètres du problème
    :param discretization: position sur le rayon
    :param l1_list: normes l1 aux positions
    :param l2_list: normes l2 aux positions
    :param linf_list: normes linfini aux positions
    :param order: ordre du schéma (str)
    :save_path: path de sauvegarde de la figure
    :show_fig: option pour afficher le graphique
    '''
    plt.figure(figsize=(8,6))
    plt.loglog(discretization, l1_list, 'o-', label=r"$L_1$")
    plt.loglog(discretization, l2_list, 's-', label=r"$L_2$")
    plt.loglog(discretization, linf_list, '^-', label=r"$L_\infty$")

    plt.xlabel(r"Taille de maille $\Delta r$ [$m$]")
    plt.ylabel(r"Erreur")
    plt.title(f"Convergence de la solution numérique d'ordre {order}\n"
              f"utilisant ri={params['RI']}, ro={params['RO']}, "
              f"s={params['S']}, d_eff={params['D_EFF']}, ce={params['CE']}")
    plt.grid()
    plt.legend()
    plt.savefig(save_path, dpi=300)
    if show_fig:
        plt.show()
    plt.close()

def graph_error_radius(params:dict, discretization, concentration_vect,
                    concentration_a, order,
                    save_path="results/temp.png",
                    show_fig=False):
    '''
    Docstring for graph_error_radius
    
    :param params: paramètres du problème
    :param discretization: position sur le rayon
    :param concentration_vect: résultat de concentration
    :param discretization_a: position sur le rayon analytique
    :param order: ordre du schéma (str)
    :save_path: path de sauvegarde de la figure
    :show_fig: option pour afficher le graphique
    '''
    error_local = concentration_vect - concentration_a
    plt.figure(figsize=(8,6))
    plt.plot(discretization, error_local)
    plt.title(f"Profil spatial de l'erreur de la solution numérique d'ordre {order}\n"
              f"utilisant ri={params['RI']}, ro={params['RO']}, "
              f"s={params['S']}, d_eff={params['D_EFF']}, ce={params['CE']}")
    plt.xlabel(r"Rayon $r$ [$m$]")
    plt.ylabel(r"Erreur $C_{num} - C_{analytique}$")
    plt.grid(True)
    plt.savefig(save_path, dpi=300)
    if show_fig:
        plt.show()
    plt.close()
