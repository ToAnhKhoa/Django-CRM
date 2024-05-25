import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    )
#preparing a cursor object
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute('CREATE DATABASE propy')
print('Database created successfully')
