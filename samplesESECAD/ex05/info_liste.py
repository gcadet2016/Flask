def affiche_info(mon_dict):
	equivalent_cle_phrase = {
		'nb_elem':'Le nombre d\'élements dans la liste:',
		'first':'Le premier élément de la liste:',
		'last':'Le dernier élément de la liste:'
	}

	for cle,valeur in mon_dict.items():
		phrase = equivalent_cle_phrase[cle]
		print(phrase,valeur)

def info_liste(ma_liste):
	taille_liste = len(ma_liste)
	dict_a_retourner = {}
	dict_a_retourner['nb_elem'] = taille_liste
	if taille_liste>0:
		premier = ma_liste[0]
		dernier = ma_liste[-1]
		dict_a_retourner['first'] = premier
		dict_a_retourner['last'] = dernier
	return dict_a_retourner

def traitement(ma_liste):
	retour_info = info_liste(ma_liste)
	affiche_info(retour_info)