import mysql.connector

def check(username, password, type):
    database = mysql.connector.connect(host='localhost', user='root', passwd='', port = 3306, database='mini_project')
    mycursor = database.cursor()
    query_patient = 'SELECT password FROM patient where username=%s'
    query_user = 'SELECT password FROM user where username=%s'
    query_doctor = 'SELECT password FROM doctor where username=%s'
    if(type=='patient'):
        mycursor.execute(query_patient, (username, ))
        for row in mycursor:
            if(row[0] == password):
                return True
            else:
                return False
        
    elif(type=='admin'):
        mycursor.execute(query_user, (username, ))
        for row in mycursor:
            if row[0] == password:
                return True
            else:
                return False
        
    
    elif(type=='doctor'):
        mycursor.execute(query_doctor, (username, ))
        for row in mycursor:
            if row[0] == password:
                return True
            else:
                return False

