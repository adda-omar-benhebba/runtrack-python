def job6(liste):
    if liste:  
        liste[0], liste[-1] = liste[-1], liste[0]


ma_liste = [1, 2, 3, 4, 5]
print("Liste avant l'échange :", ma_liste)

job6(ma_liste)
print("Liste après l'échange :", ma_liste)
