#importando o Flask
from flask import Flask, render_template

#Criando uma instância do Flask
app = Flask (__name__, template_folder='views') # __name__ representa o nome da aplicação


#Definindo a rota principal da aplicação '/'
@app.route('/')
def home(): #Função que será executada ao acessar a rota
    return render_template('index.html')


@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    players =['Yan', 'Ferrari', 'Valéria', 'Amanda']
    #Dicionário em Python (objeto)
    console = {'name' : 'Playstation 5',
               'manufacturer' : 'Sony',
               'year' : 2020
               }
        
    return render_template('games.html', 
                           title = title,
                           year = year,
                           category = category,
                           players = players,
                           console = console
                           )
    



# Se for executado diretamente pelo interpretador
if __name__ == '__main__':
#Iniciando um servidor
    app.run(host='localhost', port=5000, debug=True) #iniciando o servidor
    


