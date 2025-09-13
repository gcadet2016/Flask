# Exéction:
#   cd 2-BasicFlask
#   flask run
# Browse to http://127.0.0.1:5000

from flask import Flask, redirect, url_for, request
from mysql import connector
from sqlConnect import connectSQL, closeSQLConnection
from flask import render_template
import os

# Déclaration de l'application Web Flask
app = Flask(__name__)
isConnected = False
connectedUsersList = []

@app.route('/', methods=['GET'])
def home():
    global isConnected, connectedUsersList
    return render_template('main.html',
        titre='Page d\'accueil',
        message = f'Bonjour {connectedUsersList[0]}' if isConnected else 'Bonjour utilisateur anonyme',
        is_connected = isConnected)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global isConnected, connectedUsersList
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        SQLsecretKey = os.environ.get('MYSQL_KEY')
        # Vérification des identifiants dans SQL
        db = connectSQL()
        mabdd = db.cursor()
        req = "SELECT * FROM users WHERE mail = %s AND password = AES_ENCRYPT(%s, %s)"
        mabdd.execute(req, (email, password, SQLsecretKey))
        user = mabdd.fetchone()
        closeSQLConnection(db)
        if user:
            isConnected = True
            connectedUsersList.append(email)
            return redirect(url_for('home'))
        else:
            return render_template('sign-in.html',
                titre='Page de connexion',
                error='Identifiants invalides. Veuillez réessayer.',
                is_connected = isConnected)
    return render_template('sign-in.html',
        titre='Page de connexion',
        is_connected = isConnected)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global isConnected, connectedUsersList
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return render_template('sign-up.html',
                titre='Page d\'inscription',
                error='Les mots de passe ne correspondent pas. Veuillez réessayer.',
                is_connected = isConnected)
        SQLsecretKey = os.environ.get('MYSQL_KEY')
        # Enregistrement des nouveaux utilisateurs dans SQL
        db = connectSQL()
        mabdd = db.cursor()
        req_insert = "INSERT INTO users (nom, prenom, mail, password) VALUES (%s, %s, %s, AES_ENCRYPT(%s, %s))"
        data = (name, '', email, password, SQLsecretKey)
        mabdd.execute(req_insert, data)
        db.commit()
        closeSQLConnection(db)
        connectedUsersList.append(email)
        isConnected = True
        return redirect(url_for('home'))
    # request method == 'GET'
    return render_template('sign-up.html',
        titre='Page d\'inscription',
        is_connected = isConnected)

@app.route('/logout', methods=['GET'])
def logout():
    global isConnected, connectedUsersList
    isConnected = False
    connectedUsersList = []
    return redirect(url_for('home'))

@app.route('/readSQL')
def routeReadSql():
    db = connectSQL()
    mabdd = db.cursor()

    req_users ="SELECT * FROM users;"
    mabdd.execute(req_users)

    result = mabdd.fetchall()

    ligne_a_retourner = ""
    for row in result:
        ligne_a_retourner += str(row) + "\n"

    closeSQLConnection(db)
    
    return ligne_a_retourner

@app.route('/insertSQL', methods=['POST'])
def routeInsertSql():
    # Insert a new user in MySQL database
    db = connectSQL()
    mabdd = db.cursor()

    # Récupérer les données du formulaire
    # username = request.form.get('username')
    # email = request.form.get('email')

    # Insérer les données dans la base de données
    req_insert = "INSERT INTO users (nom, mail, password) VALUES (%s, %s, %s)"
    data = ('Lu', 'Dovic', 'dovic.lu@mail.fr')
    mabdd.execute(req_insert, data)

    db.commit()
    closeSQLConnection(db)
    return "Données insérées avec succès !"
