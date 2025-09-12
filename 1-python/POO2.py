class Dessert : 
    def __init__(self, nom, date_limite, identifiant, quantite) : 
        self.nom = nom 
        self.date_limite = date_limite 
        self.id = identifiant 
        self.quantite = quantite 

    # Méthode spéciale pour la représentation de la classe en chaîne de caractères
    def __repr__(self):
        return f'Il reste {self.quantite} {self.nom} qui expirent le {self.date_limite}'

tarte_pomme = Dessert('Tarte aux Pommes', '01/09/2020', '123', 20)
tarte_chocolat = Dessert('Tarte au Chocolat', '03/09/2020', '122', 15)

magasin = [tarte_pomme, tarte_chocolat]
print(magasin) 