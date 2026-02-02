import math

try:

    hauteur_cm = float(input("Entrez la hauteur a franchir (en centimetres) : "))
    longueur_m = float(input("Entrez la longueur horizontale (en metres) : "))

    if hauteur_cm < 0 or longueur_m <= 0:
        raise ValueError

    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle_rad = math.atan(hauteur_m / longueur_m)
    angle_deg = math.degrees(angle_rad)

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
