from flask import Flask, request, redirect, send_file, Blueprint, render_template, url_for
import psycopg2
from database.conexao import conecta_bd

app = Flask(__name__)

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        try:
            conn = conecta_bd()
            cur = conn.cursor()
            # Verifica se o usuário existe
            cur.execute('SELECT * FROM usuario WHERE email = %s AND senha = %s', (email, senha))
            usuario = cur.fetchone()
            cur.close()
            conn.close()
            if usuario:
                # Login bem sucedido
                return redirect(url_for('usuario'))
            else:
                # Login falhou
                return render_template('Telalogin.html', error='Email ou senha incorretos')
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return render_template('Telalogin.html', error='Erro ao fazer login')
    # Se for GET, apenas renderiza a página de login
    return render_template('Telalogin.html')

@app.route('/')
def index():
    return send_file('../frontend/templates/Telalogin.html')

@app.route('/telausuario')
def tela_usuario():
    return send_file('../frontend/templates/Telausuario.html')

if __name__ == '__main__':
    app.run(debug=True)