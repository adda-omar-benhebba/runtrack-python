chaine = "abcdefghijklmnopqrstuvwxyz" * 10 
longueur = len(chaine) // 5 # le nombre de chaine 

for i in range(1, longueur * 2,2):
    if i <= longueur:
        print(chaine[:i])
