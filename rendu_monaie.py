"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input () function to get a user entry
"""
"""
#Accept an amount entry
somme = input("Insérez vitre billet")
"""

somme = 20
achat1 = 3*1
achat2 = 2*1.15
rendu = somme - (achat1 + achat2)
billet100 = rendu // 100
reste100 = rendu % 100
billet50 = reste100 // 50
reste50 = reste100 % 50
billet20 = reste50 // 20
reste20 = reste50 % 20
billet10 = reste20 // 10
reste10 = reste20 % 10
billet5 = reste10 // 5
reste5 = reste10 % 5
piece2 = reste5 // 2
reste2 = piece2 % 2

print("Vous avez acheté 3 croissants et 2 baguettes pour un total de", achat1 + achat2, "€. Vous avez donné un total de", somme, "€. La machine doit vous rendre", rendu, "€. Vous récupérez", billet100, "billets de 100€,", billet50, "billets de 50€,", billet20, "billets de 20€,", billet10, "billets de 10€,", billet5, "billets de 5€, et", piece2, "pièces de 2€. Merci de votre visite, et bonne journée.")

print("La machine vous rend", billet100, "billets de 100€,", billet50, "billets de 50€,", billet20, "billets de 20€,", billet10, "billets de 10€,", billet5, "billets de 5€, et", piece2, "pièces de 2€. Merci de votre visite")

if billet100 > 0:
    print("La machine vous rend", billet100, "billets de 100€")
else:
    print()
if billet50 > 0:
    print("La machine vous rend", billet50, "billets de 50€")
else:
    print()
if billet20 > 0:
    print("La machine vous rend", billet20, "billets de 20€")
else:
    print()
if billet10 > 0:
    print("La machine vous rend", billet10, "billets de 10€")
else:
    print()
if billet5 > 0:
    print("La machine vous rend", billet50, "billets de 5€")
else:
    print()
if piece2 > 0:
    print("La machine vous rend", piece2, "piece de 2€")
else:
    print()