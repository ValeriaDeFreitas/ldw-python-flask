#Importando a classe Resource do flask_restful
from flask_restful import Resource
#Importando pacotes do flask
from flask import make_response, jsonify
#Importando a variável api do pacote api
from api import api
#Importando os schemas
from ..schemas import movie_schema
#Importando o Model
from ..models import movie_model
#Importando o service
from ..services import movie_service

#Criando os recursos de Filmes
class MovieList(Resource):
    #Método GET: Listar 
    def get(self):
        movies = movie_service.get_movies()
        movieSchema = movie_service.MovieSchema(many=True)
        return make_response(jsonify(movies), 200)   
        

api.add_resource(MovieList, '/movies')