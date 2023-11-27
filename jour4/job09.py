def maxmin(liste):
    maximum = max(liste)
    minimum = min(liste)
    valeur = sum(liste) / len(liste)
    return valeur, maximum, minimum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeur, maximum, minimum = maxmin(L)

print("La valeur moyenne des éléments de la liste est :", valeur)
print("Le maximum des éléments de la liste est :", maximum)
print("Le minimum des éléments de la liste est :", minimum)
