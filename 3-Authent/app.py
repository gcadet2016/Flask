# Exéction:
#   cd 3-Authent
#   flask run
# Browse to http://127.0.0.1:5000

from flask import Flask, redirect, url_for, request, session
from mysql import connector
from sqlConnect import SQLdb
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
    homeHtmlContent = ''

    if isConnected and userEmail and userEmail not in connectedUsersList:
        # Ce cas de figure ne devrait pas arriver normalement
        # Envisager une gestion d'erreur plus robuste 
        # ou rediriger vers la page de logout
        connectedUsersList.append(userEmail)

    if not isConnected:
        # Utilisateur non connecté: afficher la page d'accueil avec les prérequis
        # et les vérifications

        # Verifier que la base de données est accessible
        dbAccessible = False
        try:
            sqlDB = SQLdb()
            db = sqlDB.connectSQL()
            dbAccessible = True
        except connector.Error as err:
            dbAccessible = False
            print(f"Erreur de connexion à la base de données: {err}")
            errMsg = str(err)

        # Vérifier l'existance des variables d'environnement
        missingEnvVars = []
        if not os.environ.get('MYSQL_FLASK_PWD'):
            missingEnvVars.append('MYSQL_FLASK_PWD')
        if not os.environ.get('MYSQL_KEY'):
            missingEnvVars.append('MYSQL_KEY')
        if not os.environ.get('FLASK_SECRET_KEY'):
            missingEnvVars.append('FLASK_SECRET_KEY')

        homeHtmlContent = '''
        <div class="home-content">
            <h2>Bienvenue sur notre site</h2>
            <p>Prerequis pour utiliser ce site :</p>
            <ul>
                <li>La base de données MySQL doit être opérationnelle</li>
                <li>3 variables d'environnement doivent être configurées :</li>
                <ul>
                    <li>MYSQL_FLASK_PWD=mot de passe de l'utilisateur SQL 'flaskusr'</li>
                    <li>MYSQL_KEY=clé secrète pour cryptage dans la base de données</li>
                    <li>FLASK_SECRET_KEY=clé secrète pour les sessions de l'application Flask</li>
                </ul>
            </ul>
            <p>Les valeurs des variables d'environnement MYSQL_KEY et FLASK_SECRET_KEY peuvent être générées par la commande bash:  openssl rand -base64 32</p>
            <p>Vérification des prérequis :</p>
        '''
        if dbAccessible:
            homeHtmlContent += '''
            <div class="alert alert-success" role="alert">
                Le test de connexion à la base de données MySQL a réussi !
            </div>
            '''
        else:
            homeHtmlContent += f'''
            <div class="alert alert-danger" role="alert">
                Le test de connexion à la base de données MySQL a échoué !<br>
                Veuillez vérifier que le serveur MySQL est opérationnel et que la variable d'environnement MYSQL_FLASK_PWD est correctement configurées.<br>
                Détails de l'erreur : {errMsg}
            </div>
            '''
        if len(missingEnvVars) == 0:
            homeHtmlContent += '''
            <div class="alert alert-success" role="alert">
                Toutes les variables d'environnement requises sont configurées.
            </div>
            '''
        else:
            homeHtmlContent += f'''
            <div class="alert alert-danger" role="alert">
                Les variables d'environnement suivantes sont manquantes : {', '.join(missingEnvVars)}.<br>
                Veuillez les configurer avant d'utiliser l'application.
            </div>
            '''
        homeHtmlContent += '</div>'

        # errorDiv = ''
        # if not isConnected:
        #     errorDiv += '''
        #         <div class="alert alert-danger" role="alert">
        #             <p>The error message goes here</p>
        #         </div>
        #     '''
    return render_template('home.html',
        titre_page='Page d\'accueil',
        message = f'Bonjour {userEmail}' if isConnected else 'Bonjour utilisateur anonyme',
        htmlContent = homeHtmlContent,
        # errorDiv = errorDiv,
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
        sqlDB = SQLdb()
        db = sqlDB.connectSQL()
        mabdd = db.cursor()
        req = "SELECT * FROM users WHERE mail = %s AND password = AES_ENCRYPT(%s, %s)"
        mabdd.execute(req, (email, password, SQLsecretKey))
        user = mabdd.fetchone()
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
        sqlDB = SQLdb()
        db = sqlDB.connectSQL()
        mabdd = db.cursor()
        req_insert = "INSERT INTO users (nom, prenom, mail, password) VALUES (%s, %s, %s, AES_ENCRYPT(%s, %s))"
        data = (name, '', email, password, SQLsecretKey)
        mabdd.execute(req_insert, data)
        db.commit()

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
        sqlDB = SQLdb()
        db = sqlDB.connectSQL()
        mabdd = db.cursor()
        req_users ="SELECT * FROM users;"
        mabdd.execute(req_users)
        result = mabdd.fetchall()

        htmlContent = "<div class='userList'>"
        htmlContent += "<h2>Liste des utilisateurs enregistrés dans la base de données SQL:</h2>"
        htmlContent += "<ul>"
        for row in result:
            htmlContent += f'<li>{str(row)}</li>'

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
        errorDiv = '''
            <div class="alert alert-danger" role="alert">
                <p>Authentification requise pour accéder à la liste des utilisateurs.</p>
            </div>
        '''
        return render_template('userList.html',
            titre_page='Liste des utilisateurs',
            errorDiv=errorDiv,
            active_page = 'userList',
            is_connected=isConnected
        ), 403

@app.errorhandler(404)
def route404(erreur):
    errorDiv = '''
        <div class="alert alert-danger" role="alert">
            <p>La page demandée n'existe pas.</p>
        </div>
    '''
    return render_template('home.html',
		titre_page='Erreur 404',
		errorDiv=errorDiv,
        active_page = 'home',
        is_connected = session.get('isConnected', False)
	), 404

@app.errorhandler(500)
def route500(erreur):
    errorDiv = '''
        <div class="alert alert-danger" role="alert">
            <p>Une erreur interne est survenue (500)</p>
            <p>Veuillez vérifier l'accès à la base de données et les variables d'environnement</p>
        </div>
    '''
    return render_template('home.html',
		titre_page='Erreur 500',
		errorDiv=errorDiv,
        active_page = 'home',
        is_connected = session.get('isConnected', False)
	), 500
