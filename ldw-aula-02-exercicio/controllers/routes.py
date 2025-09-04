import os
from flask import render_template, request, redirect, url_for

def init_app(app):
    # Lista de jogadores
    colaboradores = ['Ana Clara', 'Lucas Silva', 'Mariana Costa', 'Rafael Souza']
    
    # Lista de jogos (como dicionários)
    list = [{'Nome': 'CS 1.6', 'Ano': 1996, 'Descricao': 'FPS Online'}]

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

        # Lista de jogos para cards (cada um com nome, ano e descrição)
        produtos = [
            {"name": "Creme Hidratante Lumina Glow", "year": 2022, "description": "Hidrata profundamente a pele, deixando-a macia e radiante ao longo do dia, com ativos naturais que respeitam o equilíbrio da pele.", "image":"img6.png"},
            {"name": "Serum Rejuvenescedor Lumina Vita", "year": 2020, "description": "Fórmula concentrada que reduz linhas finas e revitaliza a pele, promovendo firmeza e luminosidade desde as primeiras aplicações.", "image":"img7.jpg"},
            {"name": "Ácido Esfoliante Lumina Clear", "year": 2023, "description": "Ajuda a renovar a pele, desobstruindo poros e uniformizando o tom, deixando a pele mais suave e radiante.", "image":"img8.jpg"}
        ]

        # Lista de consoles (se quiser exibir também)
        consoles = [
            {"name": "Playstation 5", "manufacturer": "Sony", "year": 2020},
            {"name": "Xbox Series X", "manufacturer": "Microsoft", "year": 2020},
            {"name": "Nintendo Switch", "manufacturer": "Nintendo", "year": 2017}
        ]

        # Se for requisição POST, adiciona jogador
        if request.method == 'POST':
            new_player = request.form.get('player')
            if new_player:
                colaboradores.append(new_player)
                return redirect(url_for('divulgacao'))

        # Renderiza a página
        return render_template(
            'divulgacao.html',
            colaboradores=colaboradores,
            produtos=produtos,       # passa lista de jogos
            consoles=consoles, # passa lista de consoles
            images=image_files,
            list=list
        )

    # Rota de cadastro de jogos
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            name = request.form.get('name')
            year = request.form.get('year')
            description = request.form.get('description')

            if name and year and description:
                list.append({
                    'Nome': name,
                    'Ano': int(year),
                    'Descricao': description
                })
                return redirect(url_for('cadastro'))

        return render_template('cadastro.html', list=list)
