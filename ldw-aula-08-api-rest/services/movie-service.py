#Importando o PyMongo 
from api import mongo
#Importando o Model
from ..models import movie_model

#Função ára CADASTRAR
def add_movie(movie):
    mongo.db.movies.insert_one({
        'title': movie.title,
        'description': movie.description,
        'year': movie.year,
        'duration': movie.duration
    })
