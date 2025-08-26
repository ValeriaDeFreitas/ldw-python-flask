from flask import render_template, request, redirect, url_for

def init_app(app):
    #Lista de jogadores
    players =['Yan', 'Ferrari', 'Valéria', 'Amanda']
    #Array de objetos - Lista de jogos
    gamelist =[{'Titulo' : 'CS 1.6', 'Ano' : 1996, 'Categoria' : 'FPS Online'}]
    
    #Definindo a rota principal da aplicação '/'
    @app.route('/')
    def home(): #Função que será executada ao acessar a rota
        return render_template('index.html')


    @app.route('/games', methods = ['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        #Dicionário em Python (objeto)
        console = {'name' : 'Playstation 5',
                'manufacturer' : 'Sony',
                'year' : 2020
                }
        #Tratando uma requisição post com request
        if request.method == 'POST':
            # Coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))
                
        return render_template('games.html', 
                            title = title,
                            year = year,
                            category = category,
                            players = players,
                            console = console
                            )
        
    @app.route('/newgame', methods=['GET','POST'])
    def newgame():
            #Tratando a requisição POST
            if request.method == 'POST':
                
                if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                    gamelist.append({'Titulo' : request.form.get('title'), 'Ano' : request.form.get('year'),
                    'Categoria' : request.form.get('category')})
                    return redirect(url_for('newgame'))
                    
            return render_template('newGame.html', gamelist=gamelist)