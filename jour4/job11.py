def augmenter_liste(liste):
    for i in range(len(liste)):
        liste[i] += 1

L = [7, 11, 42, 39, 2]

augmenter_liste(L)

print("Liste après avoir augmenté 1 :", L)
