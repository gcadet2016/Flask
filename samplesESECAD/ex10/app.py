from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def routeBase():
	return 'Texte de mon choix'

@app.errorhandler(404)
def route404(erreur):
	return render_template(
		'tp_erreur.html',
		code = 404,
		message = "La page que vous avez demandé n\'est pas disponible.")