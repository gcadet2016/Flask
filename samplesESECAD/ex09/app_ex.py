from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def routeLogin():
	addr_mail = "ex@emple.fr"
	mot_de_passe = "motdepasse"
	if request.method == 'POST':
		message = ''
		post_addr_mail = request.form['mail']
		post_mdp = request.form['password']
		if addr_mail == post_addr_mail and mot_de_passe == post_mdp:
			message='Connexion réussie ! Bravo !'
		elif addr_mail == post_addr_mail:
			message='Mot de passe incorrect'
		else:
			message='Identifiant et Mot de passe incorrects'
		return render_template('index_ex.html',message=message)
	return render_template('index_ex.html')

@app.route('/count/<id>')
def routeCount(id):
	return str(id)

@app.route('/compteur/<num>')
def routeCompteur(num):
	try:
		nombre = int(num)
	except:
		nombre = 0
	return render_template('compteur.html',num=nombre)

app.debug = True
app.run()