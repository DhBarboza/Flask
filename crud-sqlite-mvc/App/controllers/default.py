from App import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
def index():
    receitas = Receitas.query.all()
    return render_template('index.html', receitas=receitas)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        receita = Receitas(request.form['receita'], request.form['ingredientes'])
        db.session.add(receita)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    receita = Receitas.query.get(id)
    if request.method == 'POST':
        receita.receita = request.form['receita']
        receita.ingredientes = request.form['ingredientes']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', receita=receita)

@app.route('/delete/<int:id>')
def delete(id):
    receita = Receitas.query.get(id)
    db.session.delete(receita)
    db.session.commit()
    return redirect(url_for('index'))
