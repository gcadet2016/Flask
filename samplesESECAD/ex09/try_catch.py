chaine = "Chaine de caractere que je vais convertir en int"

try:
	nombre = int(chaine)
except:
	nombre = len(chaine)

print(nombre)