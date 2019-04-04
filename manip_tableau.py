"""
@name manip_tableau.py
@author Aélion
@version 0.0.1
    Algorithmique spécifique sur les collections
"""

"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

"""
getGreaterOf
return the greater value of two params
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else: 
        return secondVal

"""
compare function
@param firstVal First Value to compare
@param secondVal Second Value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends on desc params
"""
def compare(firstVal, secondVal, desc=True):
    if (desc):
        return getLowerOf(firstVal, secondVal)

    return getGreaterOf(firstVal, secondVal)

"""
min function
@param anArray The array from which i want to get the min value
@return the min value of anArray
"""
def min(anArray):
    theMin = anArray[0]
    for value in anArray[1:]:
        theMin = compare(theMin, value)

    return theMin

"""
max function
@param anArray The array from which i want to get the max value
@return the max value of anArray
"""
def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax, value, False)

    return theMax

"""
average function
@param anArray Array from which evaluate the average value
@return average value of an array
"""
def average(anArray):
    total = 0
    nbItems = 0
    for val in anArray:
        total = total + val
        nbItems = nbItems +1
    return total/nbItems

"""
Factorial function
"""
def factorial(anArray):
    total = 1
    for val in anArray:
        total = total * val
    return total

#Déclaration du tableau de démonstration

monTablo = [15, 3, 25, 12, 7, -15]

#
# Simple poor loop
#
for indice, val in enumerate(monTablo):
    print(monTablo[indice]*2)

print("*********************")

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

print("*********************")

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
# Finally... 
print("And the min is : ", mayBeImTheMin)

# Bit more complex loop : find a min with function
mayBeImTheMin = monTablo[0] # Just initialize the min as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    mayBeImTheMin = getLowerOf(mayBeImTheMin, val)
# Finally... 
print("And the min is : ", mayBeImTheMin)

# Bit more complex loop : find a min with function compare
mayBeImTheMin = monTablo[0] # Just initialize the min as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    mayBeImTheMin = compare(mayBeImTheMin, val)
# Finally... 
print("And the min is : ", mayBeImTheMin)

print("And the min is : ", min(monTablo))


print("*********************")


# Bit more complex loop : find a max
mayBeImTheMax = monTablo[0] # Just initialize the max as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element --> inutile de passer par le premier element vu qu'on le prend comme valeur de départ
    if val > mayBeImTheMax: # Check if the current value in the array is greater than the current
        mayBeImTheMax = val
# Finally... 
print("And the max is : ", mayBeImTheMax)

# Bit more complex loop : find a max with function
mayBeImTheMax = monTablo[0] # Just initialize the min as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    mayBeImTheMax = getGreaterOf(mayBeImTheMax, val)
# Finally... 
print("And the max is : ", mayBeImTheMax)

# Bit more complex loop : find a max with function compare
mayBeImTheMax = monTablo[0] # Just initialize the min as the first item in the array
for val in monTablo[1:]: # Loop over the array from second element
    mayBeImTheMax = compare(mayBeImTheMax, val, False)
# Finally... 
print("And the max is : ", mayBeImTheMax)

print("And the max is : ", max(monTablo))


print("*********************")

print("La moyenne du tableau est : ", average(monTablo))

print("*********************")

print("La factorielle du tableau est : ", factorial(monTablo))