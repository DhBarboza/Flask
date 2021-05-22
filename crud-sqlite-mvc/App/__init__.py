from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.sqlite3'
db = SQLAlchemy(app)

## Controle das migrações:
migrate = Migrate(app, db)

## Controle de informações que se passa na execução:
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from App.controllers import default