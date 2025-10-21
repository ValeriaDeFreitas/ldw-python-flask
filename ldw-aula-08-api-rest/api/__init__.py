#importando o Flask do pacote API
from flask import Flask

#Importando o Flask-Restful
from flask_restful import Api

#Importando o pymongo
from flask_pymongo import PyMongo

#Importando o Flask-Marshmallow
from flask_marshmallow import Marshmallow

#Carregando o flask na variável app
app = Flask(__name__)

#Setando o endereço do banco MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/api-movies"

#Carregando o pacote api do Flask-Restful na variável api
api = Api()
#Carregando o PyMongo na variável mongo
mongo = PyMongo(app)
#Carregando o Marshmallow na variável ma
ma = Marshmallow(app)

from resources import movie_resources