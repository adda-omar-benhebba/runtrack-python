def intervalle(liste):
    produit = 1
    for valeur in liste:
        if 25 <= valeur <= 90:
            produit *= valeur
    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = intervalle(L)

print("Le produit des valeurs comprises dans l'intervalle [25, 90] est :", resultat)
