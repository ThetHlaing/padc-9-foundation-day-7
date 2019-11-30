# pip install mysql-connector-python
import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        passwd='123456',
        auth_plugin='mysql_native_password'
    )

    cursor = mydb.cursor()
    return cursor,mydb
