from flask import Flask, request, redirect, send_file
import psycopg2

app = Flask(__name__)

def conecta_bd():
    return psycopg2.connect(
        host='localhost',
        database='projeto',
        user='postgre',
        password='92525601'
    )

@app.route('/')
def index():
    return send_file('../frontend/templates/Telalogin.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    try:
        conn = conecta_bd()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE avatar = %s AND senha = %s", (usuario, senha))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return send_file('../frontend/templates/Telausuario.html')
        else:
            return '''
                <script>
                    alert("Usuário ou senha inválidos.");
                    window.location.href = "/";
                </script>
            '''
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}", 500

@app.route('/telausuario')
def tela_usuario():
    return send_file('../frontend/templates/Telausuario.html')

if __name__ == '__main__':
    app.run(debug=True)