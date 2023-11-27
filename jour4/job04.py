def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")
    return fruits

nouvelle_liste = ajouter_mangue()
print(nouvelle_liste)
