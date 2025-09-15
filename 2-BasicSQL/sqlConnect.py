from mysql import connector
import os
def connectSQL():
    password = os.environ.get('MYSQL_FLASK_PWD')
    db = connector.connect(
        user='flaskusr',
        password=password,
        database='flaskSql',
        host='localhost'
    )
    return db

def closeSQLConnection(db):
    db.close()
