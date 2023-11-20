def contient_e(chaine):
    if 'e' in chaine:
        return True
    else:
        return False

mot = input("Entrez une chaîne de caractères : ")
if contient_e(mot):
    print("La chaîne contient la lettre 'e'.")
else:
    print("La chaîne ne contient pas la lettre 'e'.")