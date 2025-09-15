from info_liste import traitement 
liste_ville = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Bordeaux']
liste_vide = []
liste_saisons = ['Printemps', 'Été', 'Automne', 'Hiver']
liste_finale = [ liste_ville, liste_vide, liste_saisons ]

for liste_courante in liste_finale:
    traitement(liste_courante)