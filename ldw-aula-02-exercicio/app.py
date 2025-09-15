# importando o Flask
from flask import Flask, render_template

# Importando os Controller (routes.py)
from controllers import routes

from models.database import db
import os

# Criando uma instância do Flask
# __name__ representa o nome da aplicação
app = Flask(__name__, template_folder='views')

routes.init_app(app)
# Se for executado diretamente pelo interpretador
dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(dir, 'models/lumina.sqlite3')

if __name__ == '__main__':
    # Iniciando um servidor
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()

    app.run(host='localhost', port=5000, debug=True)  # iniciando o servidor
