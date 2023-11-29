import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='', port = 3306, database='mini_project')

mycursor = conn.cursor()

query = 'INSERT INTO patient (username, age, gender, password, email) VALUES (%s, %s, %s, %s, %s)'

insert_tuple = ("Patient2", 54, "Female", "patient2","patient2@gmail.com")

mycursor.execute(query, insert_tuple)

print("Done.")