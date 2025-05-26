from flask import Flask, request, redirect, send_file
from database.routes.cadastro import cadastro_bp
import psycopg2

app = Flask(__name__)
app.register_blueprint(cadastro_bp)

# Função para conectar ao banco de dados
def conecta_bd():
    return psycopg2.connect(
        host='localhost',
        database='projeto',
        user='postgres',
        password='Rubinho091123'
    )

# Define o encoding das respostas HTTP
@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

# Rota inicial
@app.route('/')
def index():
    return send_file('../frontend/templates/Telacadastro.html')  # Certifique-se de que o arquivo está na pasta "templates"

# Inicialização
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
