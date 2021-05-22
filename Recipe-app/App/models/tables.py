from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    ingredientes = db.Column(db.String, nullable=False)

    ## Definir que os Campos sejam obrigatórios:
    def __init__(self, nome, ingredientes):
        self.nome = nome
        self.ingredientes = ingredientes
    


