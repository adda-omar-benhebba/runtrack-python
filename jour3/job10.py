def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return f"{nombre} est pair."
        else:
            return f"{nombre} est impair."
    else:
        return "Veuillez saisir un nombre entier positif."

print(verifier_pair_impair(8))

