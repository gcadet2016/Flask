# Module

# Extraire les informations d'une liste
# retourner un ditionnaire avec le nombre d'éléments, le premier et le dernier élément
def extraire_info(ma_liste):
    taille_liste = len(ma_liste)
    dict_a_retourner = {}
    dict_a_retourner['nb_elem'] = taille_liste
    if taille_liste > 0:
        premier = ma_liste[0]
        dernier = ma_liste[-1]
        dict_a_retourner['first'] = premier
        dict_a_retourner['last'] = dernier
    return dict_a_retourner

# Afficher les informations extraites d'une liste
# le dictionnaire en entrée doit contenir les clés: nb_elem, first, last
def affiche_info(mon_dict):
    equivalent_cle_phrase = {
        'nb_elem': 'Le nombre d\'éléments dans la liste: ',
        'first': 'Le premier élément de la liste: ',
        'last': 'Le dernier élément de la liste: '
    }
    for cle, valeur in mon_dict.items():
        phrase = equivalent_cle_phrase[cle]
        print(phrase, valeur)

# Traiter une liste: extraire les informations et les afficher
def traitement(ma_liste):
    retour_info_dict = extraire_info(ma_liste)
    affiche_info(retour_info_dict)
