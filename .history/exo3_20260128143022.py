# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math
import math

# TODO: Lire les 4 valeurs
distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
attente_navette = float(
    input("Entrez le temps d'attente de la navette (en minutes) : ")
)
temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))

# TODO: Validation
if distance < 0 or attente_navette < 0 or temps_metro < 0 or controle < 0:
    print("Erreur - donnees invalides.")
else:
    # TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
    # Calcul des temps
    # marche: distance * 60 / 5 + controle
    temps_marche_brut = distance * 60 / 5 + controle
    temps_marche = math.ceil(temps_marche_brut)

    # navette: attente + distance * 60 / 18 + controle
    temps_navette_brut = attente_navette + (distance * 60 / 18) + controle
    temps_navette = math.ceil(temps_navette_brut)

    # metro: temps_metro + controle
    temps_metro_brut = temps_metro + controle
    temps_metro_final = math.ceil(temps_metro_brut)

    # Trouver le minimum
    minimum = min(temps_marche, temps_navette, temps_metro_final)

    # Identifier les gagnants
    gagnants = []
    if temps_marche == minimum:
        gagnants.append("marcher")
    if temps_navette == minimum:
        gagnants.append("navette")
    if temps_metro_final == minimum:
        gagnants.append("metro")

    # TODO: Afficher la phrase exacte
    if len(gagnants) == 1:
        print(f"Option la plus rapide : {gagnants[0]}.")
    elif len(gagnants) == 2:
        print(f"Egalite : {gagnants[0]} et {gagnants[1]}.")
    else:
        # 3 gagnants
        print("Egalite : marcher, navette et metro.")
