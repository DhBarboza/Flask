from App import db


class Receitas(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receita = db.Column(db.String(150))
    ingredientes = db.Column(db.String(150))

    def __init__(self, receita, ingredientes):
        self.receita = receita
        self.ingredientes = ingredientes