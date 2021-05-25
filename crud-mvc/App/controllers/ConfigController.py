import sys
from flask import Flask, render_template, request, redirect, url_for

from App.models.tables import Receitas

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    receitas = Receitas.query.all()
    return render_template('index.html', receitas=receitas)

def add():
    if request.method == 'POST':
        receita = Receitas(request.form['receita'], request.form['ingredientes'])
        db.session.add(receita)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


def edit(id):
    receita = Receitas.query.get(id)
    if request.method == 'POST':
        receita.receita = request.form['receita']
        receita.ingredientes = request.form['ingredientes']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', receita=receita)


def delete(id):
    receita = Receitas.query.get(id)
    db.session.delete(receita)
    db.session.commit()
    return redirect(url_for('index'))