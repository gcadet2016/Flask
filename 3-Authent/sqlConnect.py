from mysql import connector
import os

# def connectSQL():
#     password = os.environ.get('MYSQL_FLASK_PWD')
#     db = connector.connect(
#         user='flaskusr',
#         password=password,
#         database='flaskSql',
#         host='localhost'
#     )
#     return db

# def closeSQLConnection(db):
#     db.close()

class SQLdb():
    def __init__(self):
        self.password = os.environ.get('MYSQL_FLASK_PWD')
        self.dbname = 'flaskSql'
        self.dbuser = 'flaskusr'
        self.host = 'localhost'
        self.db = None

    def connectSQL(self):
        # Ligne suivante pour debuggage seulement
        print("Connexion à la base de données MySQL...")
        print(f"Utilisateur: {self.dbuser}, Hôte: {self.host}, Base de données: {self.dbname}")
        self.db = connector.connect(
            user=self.dbuser,
            password=self.password,
            database=self.dbname,
            host=self.host
        )
        print("Connexion MySQL établie.")
        return self.db
    
    def __del__(self):
        if self.db:
            self.db.close()
            print("Connexion MySQL fermée.")
