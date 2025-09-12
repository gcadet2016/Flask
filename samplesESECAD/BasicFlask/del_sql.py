from mysql import connector

db = connector.connect(
	user='root',
	password='root',
	database='FlaskSql',
	host='localhost'
)

ma_bdd = db.cursor()

req_del = "DELETE FROM users WHERE mail = 'dovic.lu@mail.fr'"
ma_bdd.execute(req_del)

db.commit()
