from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config.from_object('config')

db = SQLAlchemy(app)

class Ingredientes(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    ingrediente_name = db.Column(db.String(1000))

    def __init__(self, ingrediente_name):
        self.ingrediente_name = ingrediente_name

class Receitas(db.Model):
    __tablename__ = "receitas"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receita_name = db.Column(db.String(150))
    ingrediente_id = db.Column(db.Integer, db.ForeignKey("ingredientes.id")) 

    ingrediente = db.relationship("Ingredientes", foreign_keys=ingrediente_id)

    def __init__(self, receita_name, ingredientes):
        self.receita_name = receita_name
        self.ingrediente_id = ingrediente_id

## Rota da lista de Receitas
@app.route('/')
def receitas():
    receitadb = Receitas.query.all()
    return render_template("receitas.html", receitadb=receitadb)

## Rota da lista de Ingredientes
@app.route('/ingredientes')
def ingredientes():
    ingredientedb = Ingredientes.query.all()
    return render_template("ingredientes.html", ingredientedb=ingredientedb)

## Rota para adicionar ingrediente:
@app.route('/add-ingrediente', methods=['GET', 'POST'])
def add_ingrediente():
    if request.method == 'POST':
        ingredientedb = Ingredientes(request.form['ingrediente_name'])
        db.session.add(ingredientedb)
        db.session.commit()
        return redirect(url_for('ingredientes'))
    return render_template('add-ingrediente.html')

## Rota para editar Ingrediente:
@app.route('/edit-ingrediente/<int:id>', methods=['GET', 'POST'])
def edit_ingrediente(id):
    ingredientedb = Ingredientes.query.get(id)
    if request.method == 'POST':
        ingredientedb.ingrediente_name = request.form['ingrediente_name']
        db.session.commit()
        return redirect(url_for('ingredientes'))
    return render_template('edit-ingrediente.html', ingredientedb=ingredientedb)


## Rota ação para deletar ingrediente:
@app.route('/delete-ingrediente/<int:id>')
def delete_ingrediente(id):
    ingredientedb = Ingredientes.query.get(id)
    db.session.delete(ingredientedb)
    db.session.commit()
    return redirect(url_for('ingredientes'))



if __name__ == '__main__':
    db.create_all()
    app.run()