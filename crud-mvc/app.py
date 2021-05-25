from flask import Flask, render_template
from flask_migrate import Migrate

from App.models.tables import db
from App.routes.config_routes import config_routes

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(config_routes, url_prefix='/receitas')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    ##db.create_all()
    app.run(debug=True)