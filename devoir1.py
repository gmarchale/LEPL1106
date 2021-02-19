import numpy as np
import matplotlib.pyplot as plt

a = -5
b = 15
n = np.arange(a,b+1)
print("indices n :",n)

def Heavyside_step(n):
    """
    Calcule la fonction échelon (Heavyside step function en anglais),
    définie comme u[n] = 1 si n >= 0, u[n] = 0 sinon.
    
    Arguments
    ---------
    n: numpy array contenant des indices (entiers) auxquels on applique la fonction échelon.
    
    Retourne
    --------
    result: numpy array de même taille contentant les valeurs u[n]
    """
    ## Version "noob"
    ## ==============
    # result = np.zeros(n.shape) # crée un array de zéros de la même taille que n
    # for i in range(n.size):    # (quelle est la différence entre "size" et "shape" ?)
    #     if n[i] >= 0:
    #         result[i] = 1.
    # return result
    
    ## Version "pro"
    ## ==============
    # return (n >= 0).astype(float)  # (n >= 0) est un array de booléens qu'on convertit en 0./1. via astype
    
    ## Version "compromis efficacité <-> interprétabilité"
    ## ==============
    result = np.zeros(n.shape) 
    result[n >= 0] = 1.        # modifie "result" aux indices où "n>=0" vaut "True"
    return result
    

# On applique la fonction à notre vecteur n calculé plus haut
u = Heavyside_step(n)
print("échelon appliqué aux indices n :",u)

# Creation de ma figure en précisant la taille
plt.figure(figsize=(7,5))

## LES INDISPENSABLES

# On récupère les différentes composantes du plot (markerline, stemlines, baseline) pour les modifier par après
markerline, stemlines, baseline = plt.stem(n,u)

# Axes
fs_text = 16 # Taille du texte
plt.xlabel("$n$ [-]", fontsize=fs_text)
plt.ylabel("$u[n]$ [-]", fontsize=fs_text)

# Titre
plt.title("Echelon discret $u[n]$", fontsize=fs_text)

## LES TOUCHES BONUS
effectuer_touches_bonus = True # Essayez de passer ceci en "False" pour voir la différence
if effectuer_touches_bonus:
    # Gestion de la "baseline" (axe horizontal)
    baseline.set_color('k')   # Baseline noir (par défaut c'est rouge, pas très beau)
    baseline.set_linewidth(1) # Diminuer la largeur de la baseline (par défaut = 2), un peu imposante par défaut
    
    # Gestion des "markerlines" ("bouboules")
    markerline.set_markersize(9) # On grossit un peu pour mettre en évidence la forme du signal
    
    # "De-zoomer" l'axe y pour être moins écrasés
    plt.ylim((-0.1,1.25))
    
    # Gestion des 'ticks' (valeurs chiffrées attachées aux axes)
    fs_ticks = 14 # Taille des chiffres (un peu petits par défaut)
    # En x, on demande de mettre un "tick" tous les multiples de 5 (par défaut ici c'était tous les multiples de 2.5)
    # mais vu que n est un entier, ça a peu de sens d'afficher des valeurs non-entières !
    plt.xticks(n[::5],fontsize=fs_ticks)
    # En y, comme il n'y a que deux valeurs possibles (0 et 1), on n'affiche que ces valeurs-là
    plt.yticks([0,1],fontsize=fs_ticks)
    

# Affichage de la figure
plt.show()
