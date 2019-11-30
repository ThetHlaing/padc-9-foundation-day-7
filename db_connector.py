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

    cursor.execute('create database if not exists hrapp')
    cursor.execute('use hrapp')
    cursor.execute(
        'create table if not exists employees(id int auto_increment,name text,position text, department_id int, salary int, primary key(id))')
    cursor.execute(
        'create table if not exists departments(id int auto_increment,name text, primary key(id))')
    return cursor, mydb
