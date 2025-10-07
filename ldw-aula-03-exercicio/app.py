from flask import Flask
from controllers import routes
from models.database import db, Lumina
import os
import pymysql

DB_NAME = 'lumina'

# Criando uma instância do Flask
app = Flask(__name__, template_folder='views', static_folder='static')

app.config['DATABASE_NAME'] = DB_NAME

# Configuração do banco de dados
dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Função para popular o banco de dados com dados iniciais
def populate_db():
    # Verifica se já existem produtos na tabela
    if Lumina.query.count() == 0:
        print("Banco de dados vazio. Populando com produtos iniciais...")
        produtos_iniciais = [
            Lumina(name="Creme Hidratante Lumina Glow", year=2022, description="Hidrata profundamente a pele, deixando-a macia e radiante ao longo do dia, com ativos naturais que respeitam o equilíbrio da pele.", image="img6.png"),
            Lumina(name="Serum Rejuvenescedor Lumina Vita", year=2020, description="Fórmula concentrada que reduz linhas finas e revitaliza a pele, promovendo firmeza e luminosidade desde as primeiras aplicações.", image="img7.jpg"),
            Lumina(name="Ácido Esfoliante Lumina Clear", year=2023, description="Ajuda a renovar a pele, desobstruindo poros e uniformizando o tom, deixando a pele mais suave e radiante.", image="img8.jpg")
        ]
        db.session.bulk_save_objects(produtos_iniciais)
        db.session.commit()
        print("✓ Produtos iniciais cadastrados com sucesso!")

# Inicializa as rotas
routes.init_app(app)

if __name__ == '__main__':
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',  # Adicione sua senha aqui, se houver
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"✓ O banco de dados '{DB_NAME}' está criado!")
    except Exception as e:
        print(f"✗ Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
    
    # Inicializa a aplicação Flask
    db.init_app(app=app)
    with app.app_context():
        # Cria as tabelas
        db.create_all()
        print("✓ Tabelas criadas com sucesso!")
        # Popula o banco de dados se estiver vazio
        populate_db()
        
    # Inicia o aplicativo na porta 4000
    app.run(host='localhost', port=4000, debug=True)