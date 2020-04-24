# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # stops a deprecation warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eleclog.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)
