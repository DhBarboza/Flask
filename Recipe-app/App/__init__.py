from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


## Configurações de Banco:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/recipe'
db = SQLAlchemy(app)

from app.controllers import default
