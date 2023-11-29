import mysql.connector as mysqlcon

mydb = mysqlcon.connect(host='localhost', user='root', passwd='', database='dental_clinic')

mycursor = mydb.cursor()

mycursor.execute("select password,type from auth where name")