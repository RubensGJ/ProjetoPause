from flask import Flask, request, redirect, send_file
import psycopg2

app = Flask(__name__)

# Função para conectar ao banco de dados
def conecta_bd():
    return psycopg2.connect(
        host='localhost',
        database='projeto',
        user='postgres',
        password='123456'
    )

# Define o encoding das respostas HTTP
@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

# Rota inicial
@app.route('/')
def index():
    return send_file('templates/Telacadastro.html')  # Certifique-se de que o arquivo está na pasta "templates"

# Rota de cadastro
@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.form

    # Coleta os dados do formulário
    avatar = data.get('Avatar')
    nome_completo = data.get('Nome')
    nascimento = data.get('DataNascimento')
    genero = data.get('Genero')
    estado = data.get('Estado')
    cidade = data.get('Cidade')
    email = data.get('email')
    curso = data.get('Curso')
    senha = data.get('password')
    confirmPassword = data.get('confirmPassword')

    # Verifica se as senhas coincidem
    if senha != confirmPassword:
        return "As senhas não coincidem.", 400

    # Conexão e inserção no banco
    conn = None
    cur = None
    try:
        conn = conecta_bd()
        cur = conn.cursor()

        # Executa a inserção no banco
        cur.execute("""
            INSERT INTO usuarios (
                avatar, nome_completo, nascimento, genero, estado, cidade, email, curso, senha
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            avatar, nome_completo, nascimento, genero,
            estado, cidade, email, curso, senha
        ))

        conn.commit()

    except Exception as e:
        return f"Ocorreu um erro ao cadastrar: {str(e)}", 500

    finally:
        if cur: cur.close()
        if conn: conn.close()

    return redirect('/')

# Inicialização
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
