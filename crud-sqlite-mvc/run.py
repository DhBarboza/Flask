from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from App import manager

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.sqlite3'

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    manager.run(debug=True)