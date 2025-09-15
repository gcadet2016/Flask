# Exéction:
#   cd 2-BasicFlask
#   flask run
# Browse to http://127.0.0.1:5000

from flask import Flask
from mysql import connector
from sqlConnect import connectSQL, closeSQLConnection

# Déclaration de l'application Web Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon site Flask !"

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
    db = connectSQL()
    mabdd = db.cursor()

    # Récupérer les données du formulaire
    # username = request.form.get('username')
    # email = request.form.get('email')

    # Insérer les données dans la base de données
    req_insert = "INSERT INTO users (nom, prenom, mail) VALUES (%s, %s, %s)"
    data = ('Lu', 'Dovic', 'dovic.lu@mail.fr')
    mabdd.execute(req_insert, data)

    db.commit()
    closeSQLConnection(db)
    return "Données insérées avec succès !"
