from flask import Flask, request, render_template, redirect, url_for
import pymysql
import hashlib

app = Flask(__name__)

db_host = ""
db_port = ""
db_user = ""
db_password = ""
db_name = ""

def connect_db():
    connection = pymysql.connect(
        host = db_host,
        port = db_port,
        user = db_user,
        password = db_password,
        db = db_name
    )

    return connection

def login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    connection = connect_db()
    cursor = connection.cursor()

    query = 'SELECT contrasena FROM Users Where '