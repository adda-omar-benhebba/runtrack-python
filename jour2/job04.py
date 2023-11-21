try:
    N = int(input("Entrez un entier supérieur à zéro : "))
    if N <= 0:
        raise ValueError("N doit être supérieur à zéro.")
    else:
        for i in range(1, N + 1):
            print(f"Table de multiplication de {i}:")
            for j in range(1, 11):
                print(f"{i} * {j} = {i * j}")
            print()
except ValueError as e:
    print(f"Erreur : {e}. Veuillez saisir un entier supérieur à zéro.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
