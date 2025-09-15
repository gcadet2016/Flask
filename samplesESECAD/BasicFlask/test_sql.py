from mysql import connector

db = connector.connect(
	user='root',
	password='root',
	database='FlaskSql',
	host='localhost'
)
#print(type(connector.connect))
ma_bdd = db.cursor()

req_users = "SELECT * FROM users"
ma_bdd.execute(req_users)

resultat = ma_bdd.fetchall()
print(resultat)

for ligne in resultat:
	print(str(ligne))


def afficher(a_afficher='Message de base'):
	print(a_afficher)

afficher()
afficher(a_afficher='Je veux afficher ce message')