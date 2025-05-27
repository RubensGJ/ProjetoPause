from flask import Flask, request, redirect, send_file, Blueprint, render_template, url_for, session
import psycopg2
from database.conexao import conecta_bd

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        try:
            conn = conecta_bd()
            cur = conn.cursor()
            cur.execute('SELECT id, username, email FROM usuario WHERE email = %s AND senha = %s', (email, senha))
            usuario = cur.fetchone()
            cur.close()
            conn.close()
            if usuario:
                session['usuario_id'] = usuario[0]
                session['username'] = usuario[1]
                session['email'] = usuario[2]
                return redirect(url_for('usuario'))
            else:
                return render_template('Telalogin.html', error='Email ou senha incorretos')
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return render_template('Telalogin.html', error='Erro ao fazer login')
    return render_template('Telalogin.html')

@app.route('/')
def index():
    return send_file('../frontend/templates/Telalogin.html')

@app.route('/telausuario')
def tela_usuario():
    return send_file('../frontend/templates/Telausuario.html')

if __name__ == '__main__':
    app.run(debug=True)