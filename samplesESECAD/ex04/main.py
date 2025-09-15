print(5 < 10)

premier_chiffre = 4
second_chiffre = 10

print(premier_chiffre == second_chiffre)

temps_actuel = "pluie"

if temps_actuel == 'beau':
	print('temps actuel :', temps_actuel, 'je dois prendre une casquette')
elif temps_actuel == 'pluie':
	print('temps actuel :', temps_actuel, 'je dois prendre un parapluie')
elif temps_actuel == 'orage':
	print('temps actuel :', temps_actuel, 'je ne dois pas sortir')
else:
	print('temps actuel :', temps_actuel, 'je dois prendre un manteau')

def affiche_temps_actuel(temps):
	if temps_actuel == 'beau':
		print('temps actuel :', temps_actuel, 'je dois prendre une casquette')
	elif temps_actuel == 'pluie':
		print('temps actuel :', temps_actuel, 'je dois prendre un parapluie')
	elif temps_actuel == 'orage':
		print('temps actuel :', temps_actuel, 'je ne dois pas sortir')
	else:
		print('temps actuel :', temps_actuel, 'je dois prendre un manteau')

affiche_temps_actuel('pluie')

nombre = 2

if nombre < 3 or nombre > 10:
	print(nombre)
else:
	print('Mauvaise zone')

compteur = 0
while compteur != 5:
	print(compteur)
	compteur = compteur + 1

compteur = 0
while compteur <= 10:
	if compteur<5:
		print('debut')
	elif compteur == 5:
		print('milieu')
	else:
		print('fin')
	compteur = compteur + 1

for char in "Hello World":
	print(char)

def is_number(to_test):
	if to_test >= '0' and to_test <= '9':
		return True
	else:
		return False

for char in "Hell0 W0rld 1":
	if is_number(char) == True:
		print('C\'est un chiffre')
	else:
		print('Ce n\'est pas un chiffre')

ma_liste = []

ma_liste = ['Element1', 'Element2', '...']
print(ma_liste)

element_liste = ma_liste[2]
print(element_liste)

recup_index = ma_liste.index('...')
print(recup_index)

nouvelle_liste = []
nouvelle_liste.append('Element_a_ajouter')
print(nouvelle_liste)

valeur_depart = 0
liste_a_remplir = []
while valeur_depart <= 10:
	liste_a_remplir.append(valeur_depart)
	valeur_depart = valeur_depart + 1
print(liste_a_remplir)

troisieme_element = liste_a_remplir[3]
print(troisieme_element)

taille_texte = len('Hello')
print(taille_texte)
taille_liste = len(liste_a_remplir)
print(taille_liste)

taille_liste = len(liste_a_remplir) - 1
while taille_liste > 0:
	element_actuel = liste_a_remplir[taille_liste]
	if element_actuel >= 1 and element_actuel <= 3:
		liste_a_remplir.remove(element_actuel)
	taille_liste = taille_liste - 1
print(liste_a_remplir)

premiere_liste = [0,1,2]
seconde_liste = [3,4,5]

liste_finale = premiere_liste + seconde_liste
print(liste_finale)
liste_finale = liste_finale * 2
print(liste_finale)

nouveau_tuple = ('Bonjour', 'Tout', 'Le', 'Monde')
print(nouveau_tuple)

tuple_diff_types = ('Bonjour',2,'Monde')
print(tuple_diff_types)

print(tuple_diff_types[2])

print(tuple_diff_types + tuple_diff_types)
print(tuple_diff_types * 2)

tuple_decompo = (10,3,1)
dix,trois,un = tuple_decompo

mon_dictionnaire = {}

mon_autre_dict = {
	'Paris': 2187526,
	'Marseille': 863310,
	'Lyon': 516092
}

var_paris = mon_autre_dict['Paris']
print(var_paris)

mon_autre_dict['Toulouse'] = 479553
mon_autre_dict['Paris'] = 479553

mon_autre_dict.pop('Paris')
print(mon_autre_dict)

cles = mon_autre_dict.keys()
valeur = mon_autre_dict.values()

print(cles,valeur)

var_items = mon_autre_dict.items()

for element in var_items:
	print(element)

for cle,valeur in var_items:
	print(cle,valeur)

for cle,valeur in var_items:
	print('Ville:',cle,'-> Population:',valeur)
