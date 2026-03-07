# Fichier: analyse_de_convergence.py
#
# But: Tracer un graphique d'analyse de convergence avec regression en loi de puissance à partir des 
#      données contenues dans les fichiers "erreurs" et liste_des_resolutions. Ce dernier nom et les variables
#      0 et 100.0 seront remplacés par le script bash analyse_auto qui appelle ce programme python.

import numpy as np
import matplotlib.pyplot as plt
import os

# Fonction pour lire des fichiers de données
def reading_files():
    # 1. Lecture des erreurs absolues
    with open('src/bash/erreurs', 'r') as fichier1:
        errors = [float(ligne) for ligne in fichier1.read().splitlines() if ligne.strip()]

    # 2. Lecture des nœuds spatiaux (nr) et temporels (nt)
    with open('src/bash/liste_des_resolutions', 'r') as fichier2:
        lignes = fichier2.read().splitlines()
        nr_list = [int(ligne.split()[0]) for ligne in lignes if ligne.strip()]
        nt_list = [int(ligne.split()[1]) for ligne in lignes if ligne.strip()]

    return nr_list, nt_list, errors

nr_list, nt_list, errors = reading_files()

# Paramètres du domaine physique
RAYON = 0.5
TEMPS_FINAL = 100.0

# Création du dossier de résultats
os.makedirs("results", exist_ok=True)

# =========================================================
# ANALYSE SPATIALE
# =========================================================
max_nt = max(nt_list)
indices_spatiaux = [i for i, nt in enumerate(nt_list) if nt == max_nt]

# Si on a testé plusieurs nr pour ce temps gelé, on trace le graphique :
if len(set([nr_list[i] for i in indices_spatiaux])) > 1:
    h_values = [(RAYON - 0) / nr_list[i] for i in indices_spatiaux]
    e_values = [errors[i] for i in indices_spatiaux]
    
    # Tri croissant pour la régression
    h_values, e_values = zip(*sorted(zip(h_values, e_values)))
    
    # Régression linéaire sur le log (sur TOUS les points)
    coeffs = np.polyfit(np.log(h_values), np.log(e_values), 1)
    exp_spatial = coeffs[0]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(h_values, e_values, marker='o', color='blue', s=60, label='Données numériques')
    plt.plot(h_values, np.exp(coeffs[1]) * np.array(h_values)**exp_spatial, 'r--', linewidth=2, label='Régression')
    
    plt.title(f"Convergence Spatiale ($N_t$={max_nt})", fontsize=14, fontweight='bold', y=1.02)
    plt.xlabel(r'$\Delta x$ (Pas spatial)', fontsize=12, fontweight='bold') 
    plt.ylabel('Erreur $L_2$', fontsize=12, fontweight='bold')
    
    # Équation esthétique
    eq_text = rf'$L_2 \propto \Delta x^{{{exp_spatial:.4f}}}$'
    plt.text(0.5, 0.2, eq_text, fontsize=14, transform=plt.gca().transAxes, 
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
    
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    
    # Esthétique des axes
    for spine in plt.gca().spines.values(): spine.set_linewidth(2)
    plt.tick_params(width=2, which='both', direction='in', top=True, right=True, length=6)

    plt.savefig("results/convergence_spatiale.png", dpi=300)
    print("--> Graphique spatial généré : results/convergence_spatiale.png")


# =========================================================
# ANALYSE TEMPORELLE
# =========================================================
max_nr = max(nr_list)
indices_temporels = [i for i, nr in enumerate(nr_list) if nr == max_nr]

# Si on a testé plusieurs nt pour cet espace gelé, on trace le graphique :
if len(set([nt_list[i] for i in indices_temporels])) > 1:
    dt_values = [TEMPS_FINAL / nt_list[i] for i in indices_temporels]
    e_values = [errors[i] for i in indices_temporels]
    
    # Tri croissant pour la régression
    dt_values, e_values = zip(*sorted(zip(dt_values, e_values)))
    
    # Régression linéaire sur le log (sur TOUS les points)
    coeffs = np.polyfit(np.log(dt_values), np.log(e_values), 1)
    exp_temporel = coeffs[0]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(dt_values, e_values, marker='s', color='green', s=60, label='Données numériques')
    plt.plot(dt_values, np.exp(coeffs[1]) * np.array(dt_values)**exp_temporel, 'r--', linewidth=2, label='Régression')
    
    plt.title(f"Convergence Temporelle ($N_r$={max_nr})", fontsize=14, fontweight='bold', y=1.02)
    plt.xlabel(r'$\Delta t$ (Pas de temps)', fontsize=12, fontweight='bold') 
    plt.ylabel('Erreur $L_2$', fontsize=12, fontweight='bold')
    
    # Équation esthétique
    eq_text = rf'$L_2 \propto \Delta t^{{{exp_temporel:.4f}}}$'
    plt.text(0.5, 0.2, eq_text, fontsize=14, transform=plt.gca().transAxes, 
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
    
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    
    # Esthétique des axes
    for spine in plt.gca().spines.values(): spine.set_linewidth(2)
    plt.tick_params(width=2, which='both', direction='in', top=True, right=True, length=6)

    plt.savefig("results/convergence_temporelle.png", dpi=300)
    print("--> Graphique temporel généré : results/convergence_temporelle.png")