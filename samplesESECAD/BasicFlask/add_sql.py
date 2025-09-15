from mysql import connector

db = connector.connect(
	user='root',
	password='root',
	database='FlaskSql',
	host='localhost'
)

ma_bdd = db.cursor()

req_add = "INSERT INTO users (nom, prenom, mail) VALUES (%s, %s, %s)"
data = ('Lu', 'Dovic', 'dovic.lu@mail.fr')
ma_bdd.execute(req_add, data)

db.commit()
