from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.sqlite3'

db = SQLAlchemy(app)

class Receitas(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receita = db.Column(db.String(150))
    ingredientes = db.Column(db.String(150))

    def __init__(self, receita, ingredientes):
        self.receita = receita
        self.ingredientes = ingredientes


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)