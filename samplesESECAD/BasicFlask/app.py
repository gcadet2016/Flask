from mysql import connector

from flask import Flask

app = Flask(__name__)

@app.route('/')
def routePrincipale():
	return 'Hello World'

@app.route('/test')
def routeTest():
	return 'Bonjour, je suis la route de test'

@app.route('/retoursql')
def routeRetourSql():
	db = connector.connect(
		user='root',
		password='root',
		database='FlaskSql',
		host='localhost'
	)
	ma_bdd = db.cursor()

	req_users = "SELECT * FROM users"
	ma_bdd.execute(req_users)

	resultat = ma_bdd.fetchall()
	ligne_a_retourner = ""
	for ligne in resultat:
		ligne_a_retourner = ligne_a_retourner + str(ligne)
	return ligne_a_retourner