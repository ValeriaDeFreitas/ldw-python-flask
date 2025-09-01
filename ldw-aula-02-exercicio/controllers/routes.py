import os
from flask import render_template, request, redirect, url_for

def init_app(app):
    # Lista de jogadores
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    
    # Lista de jogos (como dicionários)
    games_list = [{'Nome': 'CS 1.6', 'Ano': 1996, 'Descricao': 'FPS Online'}]

    # Rota principal
    @app.route('/')
    def home():
        return render_template('index.html')

    # Rota de divulgação
    @app.route('/divulgacao', methods=['GET', 'POST'])
    def divulgacao():
        # Pasta de imagens
        image_folder = os.path.join('static', 'images')
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

        # Dados fictícios para renderização
        name = 'Tarisland'
        year = 2022
        description = 'MMORPG'
        console = {
            'name': 'Playstation 5',
            'manufacturer': 'Sony',
            'year': 2020
        }

        # Se for requisição POST, adiciona jogador
        if request.method == 'POST':
            new_player = request.form.get('player')
            if new_player:
                players.append(new_player)
                return redirect(url_for('divulgacao'))

        # Renderiza a página
        return render_template('divulgacao.html',
                               name=name,
                               year=year,
                               description=description,
                               players=players,
                               console=console,
                               images=image_files)

    # Rota de cadastro de jogos
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            game_name = request.form.get('name')
            game_year = request.form.get('year')
            game_description = request.form.get('description')

            if game_name and game_year and game_description:
                games_list.append({
                    'Nome': game_name,
                    'Ano': game_year,
                    'Descricao': game_description
                })
                return redirect(url_for('cadastro'))

        return render_template('cadastro.html', list=games_list)
