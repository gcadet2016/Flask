# Exéction:
#   cd 2-BasicFlask
#   flask run
# Browse to http://127.0.0.1:5000

from flask import Flask, redirect, url_for, request, session
from mysql import connector
from sqlConnect import connectSQL, closeSQLConnection
from flask import render_template
import os

# Déclaration de l'application Web Flask
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')  
# app.secret_key: utilisée pour sécuriser les données de session.
# Elle permet de signer et chiffrer les cookies de session, afin d’empêcher leur modification ou falsification par les utilisateurs.
# Sans clé secrète, les sessions ne sont pas sûres et peuvent être compromises.
connectedUsersList = []

@app.route('/', methods=['GET'])
def home():
    global connectedUsersList
    isConnected = session.get('isConnected', False)
    userEmail = session.get('userEmail', None)

    if isConnected and userEmail and userEmail not in connectedUsersList:
        # Ce cas de figure ne devrait pas arriver normalement
        # Envisager une gestion d'erreur plus robuste 
        # ou rediriger vers la page de logout
        connectedUsersList.append(userEmail)

    return render_template('home.html',
        titre_page='Page d\'accueil',
        message = f'Bonjour {userEmail}' if isConnected else 'Bonjour utilisateur anonyme',
        active_page = 'home',
        is_connected=isConnected
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    global connectedUsersList
    isConnected = session.get('isConnected', False)
    userEmail = session.get('userEmail', None)

    if isConnected:
        # Utilisateur déjà connecté
        # Envisager une gestion d'erreur plus robuste
        return redirect(url_for('home'))
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
            session['isConnected'] = True
            session['userEmail'] = email
            connectedUsersList.append(email)
            return redirect(url_for('home'))
        else:
            return render_template('login.html',
                titre_page='Page de connexion',
                error='Identifiants invalides.\nVeuillez réessayer.',
                active_page = 'login',
                is_connected = isConnected
            )
    # request method == 'GET' et utilisateur non connecté
    return render_template('login.html',
        titre_page='Page de connexion',
        active_page = 'login',
        is_connected = isConnected
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global connectedUsersList
    isConnected = session.get('isConnected', False)
    userEmail = session.get('userEmail', None)
    if isConnected:
        # Utilisateur déjà connecté
        # Envisager une gestion d'erreur plus robuste
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return render_template('sign-up.html',
                titre_page='Page d\'inscription',
                error='Les mots de passe ne correspondent pas.\nVeuillez réessayer.',
                active_page = 'signup',
                is_connected = isConnected
            )
        SQLsecretKey = os.environ.get('MYSQL_KEY')
        # Enregistrement des nouveaux utilisateurs dans SQL
        db = connectSQL()
        mabdd = db.cursor()
        req_insert = "INSERT INTO users (nom, prenom, mail, password) VALUES (%s, %s, %s, AES_ENCRYPT(%s, %s))"
        data = (name, '', email, password, SQLsecretKey)
        mabdd.execute(req_insert, data)
        db.commit()
        closeSQLConnection(db)
        # Ici il faut afficher un bouton login !!!
        # connectedUsersList.append(email)
        # isConnected = True
        return redirect(url_for('home'))
    # request method == 'GET'
    return render_template('sign-up.html',
        titre_page='Page d\'inscription',
        active_page = 'signup',
        is_connected = isConnected
    )

@app.route('/logout', methods=['GET'])
def logout():
    global connectedUsersList
    session['isConnected'] = False
    # remove session['userEmail'] from
    connectedUsersList.remove(session.get('userEmail'))
    session.pop('userEmail', None)
    return redirect(url_for('home'))

@app.route('/userList', methods=['GET'])
def routeReadSql():
    isConnected = session.get('isConnected', False)
    if isConnected:
        db = connectSQL()
        mabdd = db.cursor()
        req_users ="SELECT * FROM users;"
        mabdd.execute(req_users)
        result = mabdd.fetchall()

        htmlContent = "<div class='userList'>"
        htmlContent += "<h2>Liste des utilisateurs enregistrés dans la base de données SQL:</h2>"
        htmlContent += "<ul>"
        for row in result:
            htmlContent += f'<li>{str(row)}</li>'

        closeSQLConnection(db)
        htmlContent += "</ul>"

        # Ajouter la liste des utilisateurs connectés
        htmlContent += "<h2>Utilisateurs connectés:</h2>"
        htmlContent += "<ul>"
        for user in connectedUsersList:
            htmlContent += f"<li>{user}</li>"
        htmlContent += "</ul>"

        htmlContent += "</div>"

        return render_template('userList.html',
            titre_page='Liste des utilisateurs',
            htmlContent=htmlContent,
            active_page = 'userList',
            is_connected=isConnected
        )
    else:
        htmlContent = ''
        msg = "Vous devez être connecté pour accéder à cette page."
        return render_template('userList.html',
            titre_page='Liste des utilisateurs',
            error=msg,
            active_page = 'userList',
            is_connected=isConnected
        ), 403

# @app.route('/insertSQL', methods=['POST'])
# def routeInsertSql():
#     # Insert a new user in MySQL database
#     db = connectSQL()
#     mabdd = db.cursor()

#     # Récupérer les données du formulaire
#     # username = request.form.get('username')
#     # email = request.form.get('email')

#     # Insérer les données dans la base de données
#     req_insert = "INSERT INTO users (nom, mail, password) VALUES (%s, %s, %s)"
#     data = ('Lu', 'Dovic', 'dovic.lu@mail.fr')
#     mabdd.execute(req_insert, data)

#     db.commit()
#     closeSQLConnection(db)
#     return "Données insérées avec succès !"
