from flask import Flask, request, redirect, send_file, render_template, url_for
from database.routes.cadastro import cadastro_bp
from database.routes.login import login_bp
import psycopg2
import os

app = Flask(__name__,
    template_folder='database/templates',
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/assets')),
    static_url_path='/static'
)

app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)

# Função para conectar ao banco de dados
def conecta_bd():
    return psycopg2.connect(
        host='localhost',
        database='projeto',
        user='postgres',
        password='Rubinho091123'
    )

# Rota inicial
@app.route('/')
def index():
    return render_template('Telainicial.html')

# Rotas para as outras páginas
@app.route('/login')
def login():
    return render_template('Telalogin.html')

@app.route('/cadastro')
def cadastro():
    return render_template('Telacadastro.html')

@app.route('/sobre-nos')
def sobre_nos():
    return render_template('Sobre_nos.html')

@app.route('/sobre-site')
def sobre_site():
    return render_template('Sobre_site.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/usuario')
def usuario():
    return render_template('Telausuario.html')

@app.route('/novaSenha')
def nova_senha():
    return render_template('Nova_Senha.html')

# Inicialização
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
