from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    produtos = db.relationship('Lumina', backref='categoria', lazy=True)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Lumina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(300))
    image = db.Column(db.String(100), nullable=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=True)

    def __init__(self, name, year, description, image=None, categoria_id=None):
        self.name = name
        self.year = year
        self.description = description
        self.image = image
        self.categoria_id = categoria_id

# NOVO MODELO DE CLIENTE
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone