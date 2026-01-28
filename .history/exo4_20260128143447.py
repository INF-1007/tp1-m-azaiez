# -*- coding: utf-8 -*-
# Exercice 04 - Verification d'une rampe d'accessibilite (gabarit)
"""
Objectif :
- DEMANDER : hauteur (cm, float) et longueur (m, float)
- Valider : hauteur >= 0 et longueur > 0
- Calculer :
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle = atan(hauteur_m / longueur_m) en degres
- Verifier la conformite : pente <= 8.00

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT :
    Pente: PP.PP%
    Angle: AA.AA deg
    Conforme: OUI|NON
Si NON, afficher une 4e ligne :
    Depassement: DD.DD%

Prompts EXACTS :
1) "Entrez la hauteur a franchir (en centimetres) : "
2) "Entrez la longueur horizontale (en metres) : "
"""
# TODO: Importer math
# TODO: Lire hauteur_cm et longueur_m

# TODO: Validation
# TODO: Calcul pente et angle
# TODO: Affichage exact (+ ligne depassement si necessaire)
import math

try:
    # 1) Demander les valeurs
    hauteur_cm = float(input("Entrez la hauteur a franchir (en centimetres) : "))
    longueur_m = float(input("Entrez la longueur horizontale (en metres) : "))

    # 2) Valider
    if hauteur_cm < 0 or longueur_m <= 0:
        # On lève une erreur pour aller dans le except ou on gère ici
        # Le plus simple est de print et quitter, ou lever une ValueError
        raise ValueError

    # 3) Calculs
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle_rad = math.atan(hauteur_m / longueur_m)
    angle_deg = math.degrees(angle_rad)

    # 4) Affichage
    print(f"Pente: {pente:.2f}%")
    print(f"Angle: {angle_deg:.2f} deg")

    if pente <= 8.0:
        print("Conforme: OUI")
    else:
        print("Conforme: NON")
        depassement = pente - 8.0
        print(f"Depassement: {depassement:.2f}%")

except ValueError:
    print("Erreur - donnees invalides.")
