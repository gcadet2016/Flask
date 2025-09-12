class Ville:
	def __init__(self,nom,code_postal,nom_maire):
		print('Je suis dans le constructeur')

		self.nom = nom
		self.code_postal = code_postal
		self.nom_maire = nom_maire
		self.debug = False
		numero_tel = "0122334455"
		self.commentaires = ""

	def afficheNom(self):
		print(self.nom)

	def changeEtatDebugIncorrect(self,nouvel_etat):
		debug = nouvel_etat
		return debug

	def changeEtatDebug(self,nouvel_etat):
		self.debug = nouvel_etat
		return self.debug

	def majCommentaire(self, nouveau_com, garderOuEffacer):
		if nouveau_com[-1] != '.':
			nouveau_com+='.'
		if garderOuEffacer == True:
			self.commentaires = nouveau_com
		else:
			self.commentaires = self.commentaires + ' ' + nouveau_com

Ville("Paris","75000","Anne Hidalgo")

ma_classe = Ville("Paris","75000","Anne Hidalgo")
print(type(ma_classe))

#print(ma_classe.numero_tel)


toulouse = Ville("Toulouse", "31000", "Jean-Luc Moudenc")
toulouse.afficheNom()

nouvel_etat_debug = toulouse.changeEtatDebug(True)
print(nouvel_etat_debug)
toulouse.changeEtatDebugIncorrect(False)
print(toulouse.debug)


toulouse.debug = True

toulouse.majCommentaire("Je viens de visiter la ville de Toulouse et je dois écrire un commentaire pour montrer que ma méthode marche comme il faut", True)
print(toulouse.commentaires)

toulouse.majCommentaire("À bientôt", False)
print(toulouse.commentaires)

toulouse = Ville("Toulouse", "31000", "Jean-Luc Moudenc")
paris = Ville("Paris","75000","Anne Hidalgo")

liste_de_villes = [ toulouse, paris ]

for ma_ville in liste_de_villes:
	print('Le code postal de',ma_ville.nom,'est',ma_ville.code_postal)

class Chaise:
	def __init__(self):
		print('Je suis dans le constructeur de la classe Chaise')

	def __del__(self):
		print('Je suis dans le destructeur de la classe Chaise')

ma_chaise = Chaise()
print('Test')


class EcrireFichier:
	def __init__(self):
		print('J\'ouvre mon fichier')
		self.mon_fichier = open('./testfichier.txt', 'w')

	def ecrire(self, a_ecrire):
		self.mon_fichier.write(a_ecrire)

	def __del__(self):
		print('Je ferme mon fichier')
		self.mon_fichier.close()

PourEcrire = EcrireFichier()
PourEcrire.ecrire('Voici une ligne')
PourEcrire.ecrire('Voici une autre ligne')


class Dessert:
	def __init__(self,nom,date_limite,identifiant,quantite,):
		self.nom = nom
		self.date_limite = date_limite
		self.id = identifiant
		self.quantite = quantite

	def __repr__(self):
		return 'Il reste ' + str(self.quantite) + ' ' + self.nom + ' qui expirent le ' + self.date_limite

tarte_pomme = Dessert('Tarte aux Pommes','01/09/2020','123',20)
tarte_chocolat = Dessert('Tarte au Chocolat','03/09/2020','122',2)

magasin = [ tarte_pomme, tarte_chocolat ]
print(magasin)