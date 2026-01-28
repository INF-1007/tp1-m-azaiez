# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)

# TODO: Lire les 4 valeurs (int)

# TODO: Valider les donnees (matchs >= 0, durees > 0)

# TODO: Calculer les minutes totales (football, soccer, total)

# TODO: Convertir en heures/minutes et afficher exactement 4 lignes

nom = input("Entrez votre nom complet : ")

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

if match_F_C < 0 or duree_F_C <= 0 or match_S_C < 0 or duree_S_C <= 0:
    print("Erreur - donnees invalides.")
else:
    temps_F = match_F_C * duree_F_C
    temps_S = match_S_C * duree_S_C
    temps_tot = temps_F + temps_S

    hf = temps_F // 60
    mf = temps_F % 60

    hs = temps_S // 60
    ms = temps_S % 60

    ht = temps_tot // 60
    mt = temps_tot % 60

    print(f"Bonjour {nom}")
    print(f"Football (Carabins): {match_F_C} match(s), {hf}h{mf:02d} de visionnage ")
    print(f"Soccer (Carabins): {match_S_C} match(s), {hs}h{ms:02d} de visionnage ")
    print(f"Total : {ht}h{mt:02d}")
