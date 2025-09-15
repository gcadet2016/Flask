from flask import Flask
from datetime import date

from flask import render_template

app = Flask(__name__)

@app.route('/')
def routePrincipale():
	lien = '<a href="/date">Lien vers la page date</a>'
	contenu = '<h1>Hello World</h1>'
	return lien + contenu

@app.route('/date')
def routeDate():
	date_actuelle = date.today()
	date_actuelle = str(date_actuelle)
	return date_actuelle

@app.route('/template-base')
def routeTemplateBase():
	return render_template('main.html',
		titre='Oui',
		mon_titre='Le titre est généré par Python',
		mon_paragraphe='Ce paragraphe est aussi généré par Python.',
		nombre=3,
		is_connected=False)