from  flask_sqlalchemy import SQLAlchemy
db  = SQLAlchemy()

class Lumina (db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(150))
     year = db.Column(db.Integer)
     description = db.Column(db.String(300))
    
     
     def __init__(self, name, year, description):
         self.name = name
         self.year = year
         self.description = description
         