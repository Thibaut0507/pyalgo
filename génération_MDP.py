# Génération d'un mot de passe aléatoire respectant ces conditions : 
# - nombre de caractères compris entre 8 et 12 
# - au moins 1 lettre majuscule 
# - au moins 1 chiffre 
# - au moins 1 élément de ponctuation 

# Utilisation de la fonction random

"""
Password Generator
@author Aélion
@version 0.0.1
"""

import random

minuscule = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
majuscule = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ponctuation = ['*', ',', ';', '/', '+', '-', ')', '(', '[', ']']

# Détermination de la longueur du mot de passe 

longueur = random.randint(8, 12)
print(longueur)

# Détermination des caractères obligatoires
    # 1 majuscule 
    # 1 chiffre
    # 1 élément de ponctuation 

theMaj = random.choice(majuscule)
theChi = random.choice(chiffre)
thePonct = random.choice(ponctuation)
password = [theMaj, theChi, thePonct]
print(password)

# Détermination des autres élements du mot de passe 

while len(password) < longueur:
    i = random.randint(0, 3)
    if i == 0 :
        ajout = minuscule 
    elif i == 1:
        ajout = majuscule
    elif i == 2:
        ajout = chiffre
    elif i == 3: 
        ajout = ponctuation
    
    password.append(random.choice(ajout))
print(password)

# Mélange des éléments du mot de passe de manière aléatoire 
    # Pour mélanger facilement, peut aussi utiliser random.shuffle

finalPassword = [""] * len(password)   
while len(password) > 0:
    for j in range(len(password)):
        ajout2 = random.randint(0, len(password)-1)
        finalPassword [j] = password[ajout2]
        password.remove(password[ajout2])
print(finalPassword)

# Mise en forme pour afficher le mot de passe sous forme d'une chaine de caractères


mdp = "" # Créer une chaine de caractère vide
for h in range(longueur):
   mdp = mdp + str(finalPassword[h]) # Converti 1 à 1 les valeurs du tableau en caractère
print("")
print("***************************************")
print(" Votre mot de passe est : ",mdp)
print("***************************************")

# On peut aussi utiliser la fonction join 
    # print("".join(finalPassword))