"""
@name manip_tableau.py
@author Aélion
@version 0.0.1
    Algorithmique spécifique sur les collections
"""

#Déclaration du tableau de démonstration

monTablo = [15, 3, 25, 12, 7, -15, 45, -25, 71, 14, -78, 21, 1]

#
# Simple poor loop
#
for indice, val in enumerate(monTablo):
    print(monTablo[indice]*2)

print("*****************")

# More complex loop with condition
for indice, val in enumerate(monTablo):
    if indice % 2 == 0:
        print(monTablo[indice]*2)

#The Same 
indice = 0
for val in monTablo:
    if indice % 2 == 0:
        print(monTablo[indice] * 2)
    indice = indice + 1

print("*****************")

# Trouver la valeur la plus petite du tableau
initiale = monTablo[0]
for indice, val in enumerate(monTablo):
    if initiale > monTablo[indice]:
        initiale = monTablo[indice]
print(initiale)

# Trouver la valeur la plus grande du tableau
initiale = monTablo[0]
for indice, val in enumerate(monTablo):
    if initiale < monTablo[indice]:
        initiale = monTablo[indice]
print(initiale)

# Bit more complex loop : find a min
mayBeImTheMin = monTablo[0] # Just initialize the min as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    if val < mayBeImTheMin: # Check if the current value in the array is lower than the current
        mayBeImTheMin = val
# Fianlly... 
print("And the min is : ", mayBeImTheMin)

# Bit more complex loop : find a max
mayBeImTheMax = monTablo[0] # Just initialize the max as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    if val > mayBeImTheMax: # Check if the current value in the array is greater than the current
        mayBeImTheMax = val
# Fianlly... 
print("And the max is : ", mayBeImTheMax)

# Déterminer valeur min (fonction min)
Minimal = min(monTablo)
print("La valeur minimale est : ", Minimal)

# Déterminer valeur max (fonction max)
Maximal = max(monTablo)
print("La valeur maximale est : ", Maximal)