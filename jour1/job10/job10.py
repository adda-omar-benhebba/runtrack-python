class Investissement:
    def __init__(self, montant_initial, taux_rendement):
        self.montant_initial = montant_initial
        self.taux_rendement = taux_rendement / 100  # Conversion décimal

    def gain_annuel(self):
        gain = self.montant_initial * self.taux_rendement
        return gain

    def augmentation_capital(self, montant_augmentation, augmentation_taux):
        self.montant_initial += montant_augmentation
        self.taux_rendement += augmentation_taux / 100

    def retrait_capital(self, pourcentage_retrait, diminution_taux):
        retrait = self.montant_initial * (pourcentage_retrait / 100)
        self.montant_initial -= retrait
        self.taux_rendement -= diminution_taux / 100

    def montant_final(self):
        return self.montant_initial

montant_initial = float(input("Entrez le montant initial de l'investissement : "))
taux_rendement = float(input("Entrez le taux de rendement annuel en pourcentage : "))
investissement = Investissement(montant_initial, taux_rendement)
print(f"Gain annuel initial : {investissement.gain_annuel()} €")
investissement.augmentation_capital(5000, 2)
print(f"Gain annuel après l'augmentation : {investissement.gain_annuel()} €")
investissement.retrait_capital(10, 1)
print(f"Montant final de l'investissement : {investissement.montant_final()} €")
