import os
from flask import render_template, request, redirect, url_for

def init_app(app):
    # Lista de jogadores
    patrocinadores = ['Ana Clara', 'Lucas Silva', 'Mariana Costa', 'Rafael Souza']

    products =[{'Nome' : 'HydraGlow Creme Facial', 'Ano' : 2023, 'Descricao' : 'Um creme hidratante leve de rápida absorção, desenvolvido com ácido hialurônico e extrato de camomila, que promove hidratação profunda e duradoura enquanto acalma a pele, deixando-a macia e luminosa.'}]
    
    

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

        # Se for requisição POST, adiciona jogador
        if request.method == 'POST':
            new_patrocinador = request.form.get('patrocinadores')
            if new_patrocinador:
                patrocinadores.append(new_patrocinador)
                return redirect(url_for('divulgacao'))

        # Renderiza a página
        return render_template(
            'divulgacao.html',
            patrocinadores=patrocinadores,
            produtos=produtos,       # passa lista de jogos
            images=image_files,
            products=products)

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':

            if request.form.get('name') and request.form.get('year') and request.form.get('description'):
                    products.append({'Nome' : request.form.get('name'), 'Ano' : request.form.get('year'),
                    'Descricao' : request.form.get('description')})
                    return redirect(url_for('cadastro'))
        return render_template('cadastro.html', products=products)
    


