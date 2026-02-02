# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)
try:
    n = int(input("Entrez le nombre de billets necessaires : "))
    statut_etudiant = str(input("Entrez le statut etudiant (O/N) : ")).upper()
except:
    print("Erreur - donnees invalides.")
    raise SystemExit
# TODO: Validation (n >= 0 et statut dans {O, N})
if n >= 0 and statut_etudiant in ("O", "N"):
    pass
else:
    print("Erreur - donnees invalides.")
    raise SystemExit

# TODO: Chercher la meilleure combinaison (A, B, C, D)
forfait_24 = 66.00
forfait_12 = 36.00
forfait_5 = 15.75
billet_uni = 3.60

if statut_etudiant == "O":
    forfait_24 *= 0.88
    forfait_12 *= 0.88
    forfait_5 *= 0.88
else:
    pass
maxA = n // 24
maxB = n // 12
maxC = n // 5

test = None
for A in range(maxA + 1):
    for B in range(maxB + 1):
        for C in range(maxC + 1):
            billet_forfaits = (24 * A) + (12 * B) + (5 * C)
            D = n - billet_forfaits
            if D < 0:
                D = 0
            prix_final = (A * forfait_24) + (B * forfait_12) + (C * forfait_5) + (D * billet_uni)
            meilleure_issue = (prix_final, n, A, B, C, D)

            if test is None or meilleure_issue < test:
                test = meilleure_issue

(prix_final, n, A, B, C, D) = test

# TODO: Calculer et afficher le resultat exact (6 lignes)

print("Forfaits de 24 billets -", A)
print("Forfaits de 12 billets -", B)
print("Forfaits de 5 billets -", C)
print("Billets unitaires -",D)
print("Total billets -",n)
print("Prix total - ",prix_final,"$")