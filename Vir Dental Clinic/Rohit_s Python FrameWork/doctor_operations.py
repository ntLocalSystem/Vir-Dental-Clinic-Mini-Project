import mysql.connector


def doctor_add(qual, doc_username, gender, email, speciality, password, user_username):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='', port=3306, database='mini_project')
    cursor = conn.cursor()
    query = 'insert into doctor (qualification, doc_username, gender, email, speciality, password, user_username) values (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (qual, doc_username, gender, email, speciality, password, user_username))
    conn.commit()
    conn.close()


def doctor_remove(doc_username):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='', port=3306, database='mini_project')
    cursor = conn.cursor()
    query = 'delete from doctor where doc_username=%s'
    cursor.execute(query, (doc_username,))
    conn.commit()
    conn.close()



#doctor_add('MD', 'docsys', 'Male', 'doc.surname@gmail.com', 'Mess ups', 'password', 'admin123' )
#doctor_add('MD', 'docsys1', 'Male', 'doc.surname@gmail.com', 'Mess ups', 'password', 'admin123')
#doctor_remove('docsys')