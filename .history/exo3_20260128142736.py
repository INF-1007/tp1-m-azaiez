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

# TODO: Lire les 4 valeurs

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)

# TODO: Afficher la phrase exacte


import math

try:
    match_F_C = int(
        input(
            "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
        )
    )
except ValueError:
    match_F_C = -1

try:
    duree_F_C = int(
        input("Entrez la duree moyenne d'un match de football suivi (en minutes) : ")
    )
except ValueError:
    duree_F_C = -1

try:
    match_S_C = int(
        input(
            "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
        )
    )
except ValueError:
    match_S_C = -1

try:
    duree_S_C = int(
        input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : ")
    )
except ValueError:
    duree_S_C = -1