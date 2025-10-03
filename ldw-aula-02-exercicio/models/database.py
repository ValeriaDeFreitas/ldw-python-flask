from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Lumina (db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(150))
     year = db.Column(db.Integer)
     description = db.Column(db.String(300))

     def __init__(self, name, year, description):
         self.name = name
         self.year = year
         self.description = description


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    preco = db.Column(db.Float)
    descricao = db.Column(db.String(150))
    avaliacao = db.Column(db.Integer)
    tipo_produto = db.Column(db.String(150))
    criado_em = db.Column(db.Date)
    atualizado_em = db.Column(db.Date)
    
    # pegando fk da tabela console campo id
    # relacionando tabelas   nome do model|           tabela games|   melhora o desempenho 
    console = db.relationship('Console', backref=db.backref('game', lazy=True))
    def __init__(self, marca, nome, preco, descricao, avaliacao, tipo_produto, criado_em, atualizado_em):
        self.marca = marca
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.avaliacao = avaliacao
        self.tipo_produto = tipo_produto
        self.criado_em = criado_em
        self.atualizado_em = atualizado_em
        
         