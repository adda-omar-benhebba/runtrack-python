class Produit:
    def __init__(self, nom, prix_unitaire, quantite):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite
    def afficher_info(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} €")
        print(f"Quantité en stock : {self.quantite}")
    def mise_a_jour_stock(self, quantite_achetee):
        self.quantite += quantite_achetee
    def inflation_prix(self):
        self.prix_unitaire *= 1.1  # Augmentation de 10%
produit1 = Produit("Ordinateur", 550, 5)
produit1.afficher_info()
quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
produit1.mise_a_jour_stock(quantite_achetee)
produit1.inflation_prix()
print("\nAprès l'achat et l'inflation :")
produit1.afficher_info()
