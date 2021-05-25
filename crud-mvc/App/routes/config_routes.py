from flask import Blueprint

from App.controllers.ConfigController import index, add, edit, delete

config_routes = Blueprint('config_routes', __name__)

config_routes.route('/')(index)
config_routes.route('/add', methods=['GET', 'POST'])(add)
config_routes.route('/edit/<int:id>', methods=['GET', 'POST'])(edit)
config_routes.route('/delete/<int:id>')(delete)