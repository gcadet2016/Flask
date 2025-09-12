from flask import Flask
from datetime import datetime

from flask import render_template

from mysql import connector

app = Flask(__name__)

@app.route('/')
def routePrincipale():
	message = 'Mon application Web Flask'
	return render_template('main.html',
	contenu=message,
	titre='Page principale')

@app.route('/date')
def routeDate():
	message = str(datetime.now())
	return render_template('main.html',
	contenu=message,
	titre='Date')

@app.route('/users')
def routeUsers():
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
	premier_utilisateur = resultat[0]
	nom = premier_utilisateur[2]
	prenom = premier_utilisateur[1]

	db.close()

	return render_template('main.html',
	utilisateur_bdd_nom=nom,
	utilisateur_bdd_prenom=prenom,
	titre='Utilisateurs')