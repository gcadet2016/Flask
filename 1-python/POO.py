class Ville: 
    # Constructeur
    def __init__(self, nom, code_postal, nom_maire):
        print('Je suis dans le constructeur')
        self.nom = nom
        self.code_postal = code_postal
        self.nom_maire = nom_maire
        self.debug = False

    # Destructeur
    def __del__(self):
        print(f'Je suis dans le destructeur de la ville {self.nom}')

    def afficher(self):
        print(f'Ville: {self.nom}, Code postal: {self.code_postal}, Maire: {self.nom_maire}')

    def afficheNom(self):
        print(f'Nom de la ville: {self.nom}')

    def ChangeEtatDebug(self, nouvel_etat=None):
        if nouvel_etat is not None:
            self.debug = nouvel_etat
        else:
            self.debug = not self.debug
        print(f'Le mode debug est maintenant à {self.debug}')
        return self.debug
# -------------------------------------------------------------
class EcrireFichier:
    def __init__(self):
        print('J\'ouvre mon fichier')
        self.mon_fichier = open('./testfichier.txt', 'w')

    def ecrire(self, a_ecrire):
        self.mon_fichier.write(a_ecrire + '\n')

    def __del__(self):
        print('Je ferme mon fichier')
        self.mon_fichier.close()

PourEcrire = EcrireFichier()
PourEcrire.ecrire('Voici une ligne')
PourEcrire.ecrire('Voici une autre ligne')

# -------------------------------------------------------------

ma_classe = Ville("Paris", 75000, "Anne Hidalgo")
print(type(ma_classe))
ma_classe.afficher()

toulouse = Ville("Toulouse", "31000", "Jean-Luc Moudenc")
toulouse.afficher()
nouvel_etat_debug = toulouse.ChangeEtatDebug(True)
print("Nouvel état du mode debug :", nouvel_etat_debug)