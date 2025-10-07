import os
from flask import render_template, request, redirect, url_for, flash
from models.database import Lumina, Categoria, Cliente, db

def init_app(app):
    
    app.config['SECRET_KEY'] = 'lumina-secret-key-2024'
    
    # Rota principal
    @app.route('/')
    def home():
        return render_template('index.html')

    # Rota de divulgação
    @app.route('/divulgacao', methods=['GET', 'POST'])
    def divulgacao():
        patrocinadores = ['Ana Clara', 'Lucas Silva', 'Mariana Costa', 'Rafael Souza']
        
        if request.method == 'POST':
            new_patrocinador = request.form.get('patrocinadores')
            if new_patrocinador:
                patrocinadores.append(new_patrocinador)
                return redirect(url_for('divulgacao'))
        
        produtos_destaque = Lumina.query.all()
        return render_template('divulgacao.html', patrocinadores=patrocinadores, produtos=produtos_destaque)

    # --- ROTAS DE PRODUTOS ---
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        if request.method == 'POST':
            name = request.form.get('name')
            year = request.form.get('year')
            description = request.form.get('description')
            categoria_id = request.form.get('categoria_id')

            if name and year and description:
                novo_produto = Lumina(
                    name=name, 
                    year=int(year), 
                    description=description,
                    categoria_id=int(categoria_id) if categoria_id else None
                )
                db.session.add(novo_produto)
                db.session.commit()
                flash('Produto cadastrado com sucesso!', 'success')
                return redirect(url_for('cadastro'))
        
        produtos_paginados = Lumina.query.paginate(page=page, per_page=per_page, error_out=False)
        categorias = Categoria.query.all()
        
        return render_template('cadastro.html', products=produtos_paginados, categorias=categorias)
    
    @app.route('/produto/editar/<int:id>', methods=['GET', 'POST'])
    def produto_editar(id):
        produto = Lumina.query.get_or_404(id)
        categorias = Categoria.query.all()
        
        if request.method == 'POST':
            produto.name = request.form.get('name')
            produto.year = int(request.form.get('year'))
            produto.description = request.form.get('description')
            categoria_id_form = request.form.get('categoria_id')
            produto.categoria_id = int(categoria_id_form) if categoria_id_form else None
            
            db.session.commit()
            flash('Produto atualizado com sucesso!', 'success')
            return redirect(url_for('cadastro'))
        
        return render_template('produto_editar.html', produto=produto, categorias=categorias)

    @app.route('/produto/excluir/<int:id>')
    def produto_excluir(id):
        produto = Lumina.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        flash('Produto excluído com sucesso!', 'success')
        return redirect(url_for('cadastro'))
        
    # --- ROTAS DE CATEGORIAS ---
    @app.route('/categorias', methods=['GET', 'POST'])
    def categorias():
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        if request.method == 'POST':
            nome = request.form.get('nome')
            descricao = request.form.get('descricao')
            
            if nome:
                nova_categoria = Categoria(nome=nome, descricao=descricao)
                db.session.add(nova_categoria)
                db.session.commit()
                flash('Categoria cadastrada com sucesso!', 'success')
                return redirect(url_for('categorias'))
        
        categorias_paginadas = Categoria.query.paginate(page=page, per_page=per_page, error_out=False)
        return render_template('categorias.html', categorias=categorias_paginadas)

    @app.route('/categoria/editar/<int:id>', methods=['GET', 'POST'])
    def categoria_editar(id):
        categoria = Categoria.query.get_or_404(id)
        
        if request.method == 'POST':
            categoria.nome = request.form.get('nome')
            categoria.descricao = request.form.get('descricao')
            db.session.commit()
            flash('Categoria atualizada com sucesso!', 'success')
            return redirect(url_for('categorias'))
        
        return render_template('categoria_editar.html', categoria=categoria)

    @app.route('/categoria/excluir/<int:id>')
    def categoria_excluir(id):
        categoria = Categoria.query.get_or_404(id)
        if categoria.produtos:
            flash('Não é possível excluir uma categoria com produtos associados!', 'danger')
        else:
            db.session.delete(categoria)
            db.session.commit()
            flash('Categoria excluída com sucesso!', 'success')
        return redirect(url_for('categorias'))

    # --- ROTAS PARA O CRUD DE CLIENTES ---
    @app.route('/clientes', methods=['GET', 'POST'])
    def clientes():
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            telefone = request.form.get('telefone')
            
            if nome and email:
                if Cliente.query.filter_by(email=email).first():
                    flash('Este email já está cadastrado!', 'danger')
                else:
                    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
                    db.session.add(novo_cliente)
                    db.session.commit()
                    flash('Cliente cadastrado com sucesso!', 'success')
                return redirect(url_for('clientes'))

        clientes_paginados = Cliente.query.paginate(page=page, per_page=per_page, error_out=False)
        return render_template('clientes.html', clientes=clientes_paginados)

    @app.route('/cliente/editar/<int:id>', methods=['GET', 'POST'])
    def cliente_editar(id):
        cliente = Cliente.query.get_or_404(id)
        
        if request.method == 'POST':
            cliente.nome = request.form.get('nome')
            cliente.email = request.form.get('email')
            cliente.telefone = request.form.get('telefone')
            
            db.session.commit()
            flash('Cliente atualizado com sucesso!', 'success')
            return redirect(url_for('clientes'))
            
        return render_template('cliente_editar.html', cliente=cliente)

    @app.route('/cliente/excluir/<int:id>')
    def cliente_excluir(id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        flash('Cliente excluído com sucesso!', 'success')
        return redirect(url_for('clientes'))