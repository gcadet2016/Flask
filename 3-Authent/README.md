# Flask
Exemple de site web crée à l'ai de Flask: création de compte et authentication  

Configuration de développement:
- Python sous Windows 11 + VsCode  
- MySQL sous WSL

Les lignes de commande ci-dessous ont été exécutées dans un terminal VsCode "cmd" ou sous bash (WSL)  


## Prérequis  
### Packages python
```
pip install Flask
pip install mysql-connector-python  
```
### Générer les clés de cryptage (encryption keys)  
Les valeurs des variables d'environnement MYSQL_KEY et FLASK_SECRET_KEY peuvent être générées par la commande bash:  
```
openssl rand -base64 32
```
Commande equivalente powerShell:
```
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
[Convert]::ToBase64String($bytes)
```

### Variables d'environnement
Ajouter 3 variables d'environnement à l'aide de la console (Windows cmd) 
- MYSQL_FLASK_PWD: mot de passe de l'utilisateur SQL 'flaskusr'.
- MYSQL_KEY: clé secrète pour cryptage des mots de passe dans la base de données.
- FLASK_SECRET_KEY: clé secrète pour les sessions de l'application Flask.


Créer les variables d'environnement.  
Ouvrir un compte de commande Windows cmd (terminal dans VsCode):
```
set MYSQL_FLASK_PWD=<mot de passe du compte flaskusr>
set MYSQL_KEY=<clé de cryptage 1>
set FLASK_SECRET_KEY=<clé de cryptage 2>
```
Remarque: le lancement du serveur Flask à l'aide de la commande 'flask run', devra se faire dans ce même prompt de commande.

# Configuration MySQL
## Création de la base de données
Lancer un outil de gestion de BDD (phpMyAdmin par exemple)  
Exécuter le fichier __.\sql\flaskSql.sql__

Configuration du compte de service utilisé par le serveur web pour accéder à la base de données.  
- Compte: __flaskusr__  
- Mot de passe: dans l'étape précédente, le mot de passe a été configuré dans la variable d'environnement __MYSQL_FLASK_PWD__.

Configurer les droits pour l'utilisateur SQL 'flaskuser':  
- Sous WSL, ourvrir un prompt de commande Linux.  
- Lancer les commande bash suivantes:
```
sudo mysql

mysql> CREATE USER 'flaskusr'@'localhost' IDENTIFIED BY '<mot de passe de flaskusr>';
mysql> GRANT SELECT, INSERT, UPDATE, DELETE, ALTER ON `flaskSql`.* TO `flaskusr`@`localhost`;
 ou 
mysql> GRANT ALL PRIVILEGES ON `flaskSql`.* TO `flaskusr`@`localhost`;
```
# Configuration de l'application web
Pour information, la connexion à la base de données 'flaskSql' hébergée dans MySQL est configurée dans le fichier python : __.\sqlConnect.py__  
Aucun changement n'est requis si cette procédure est suivie sans erreur.

# Démarrer le serveur web
Dans le terminal cmd de vsCode (précédemment utilisé pour configurer les variables d'environnement)
```
cd 3-Authent
flask run
```
# Test

Naviguer sur la page: [Page d'accueil](http://127.0.0.1:5000)  

