from flask import Flask,render_template
from hashlib import sha256
import sqlite3

con=sqlite3.connect("hsoft.db")
cur=con.cursor()

app=Flask(__name__)

@app.route("/")

def index(name):
	return render_template('index.html')