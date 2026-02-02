# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
SECTIONS = ["A","B", "C", "D", "E", "F", "G","H"]
MESSAGE = "Erreur - donnees invalides."
# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#      En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter
personne = []
try:
    for x in range(8):
        entree = int(input("Entrez une valeur entière positive: "))
        if entree < 0:
            print(MESSAGE)
            raise SystemExit
        personne.append(entree)
except (ValueError, EOFError):
    print(MESSAGE)
    raise SystemExit
# TODO: Calculer les intensites brutes (liste de 8 floats)
intensite = [personne[i] * FACTEURS[i] for i in range(8)]
# TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])
maxI = max(intensite)
if maxI == 0:
    niveau = [0] * 8
else:
    niveau = []
    for j in intensite:
        n = int((j / maxI) * 10 + 0.5)
        niveau.append(n)
# TODO: Afficher la grille (10 lignes) puis la ligne des labels
for colonne in range(10, 0, -1):
    ligne = []
    for n in niveau:
        if n >= colonne:
            ligne.append("❚")
        else:
            ligne.append(".")
    print(f"{colonne:2} | " + " ".join(ligne))
print("     " + " ".join(SECTIONS))