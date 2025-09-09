#importando o Flask
from flask import Flask, render_template 

#Importando os Controller (routes.py)
from controllers import routes

from models.database import db
# Importando a biblioteca para a manipulação do S.O
import os

#Criando uma instância do Flask
app = Flask (__name__, template_folder='views') # __name__ representa o nome da aplicação

routes.init_app(app)
# Se for executado diretamente pelo interpretador

# Extraindo o diretório absoluto do arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Criando o arquivo do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(dir, 'models/games.sqlite3')

if __name__ == '__main__':
    # Enviando flask para o sqlachemy
    db.init_app(app=app)
#  Verificar no inicio da aplicação se o banco já existe. Se não, ele cria.
    with app.test_request_context():
        db.create_all()
        
#Iniciando um servidor
    app.run(host='0.0.0.0', port=5000, debug=True) #iniciando o servidor
    


