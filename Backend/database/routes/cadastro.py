from flask import Blueprint, request, redirect
import psycopg2
import uuid
from datetime import date
from database.conexao import conecta_bd  # Importa a função de conexao.py

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.form

    # Coleta os dados do formulário (nomes devem bater com o HTML!)
    avatar = data.get('avatar')
    nome_completo = data.get('nome_completo')
    nascimento = data.get('nascimento')
    genero = data.get('genero')
    estado = data.get('estado')
    cidade = data.get('cidade')
    email = data.get('email')
    curso = data.get('course')
    senha = data.get('password')
    confirmPassword = data.get('confirmPassword')

    # Verifica se as senhas coincidem
    if senha != confirmPassword:
        return "As senhas não coincidem.", 400

    # Gera um UUID e data de cadastro
    usuario_id = str(uuid.uuid4())
    data_cadastro = date.today()

    conn = None
    cur = None
    try:
        conn = conecta_bd()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuario (
                Id, Username, Nome, DataNascimento, Genero, Estado, Cidade, Email, Curso, Senha, DataCadastro
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            usuario_id, avatar, nome_completo, nascimento, genero, estado, cidade, email, curso, senha, data_cadastro
        ))
        conn.commit()
    except Exception as e:
        return f"Ocorreu um erro ao cadastrar: {str(e)}", 500
    finally:
        if cur: cur.close()
        if conn: conn.close()
    return redirect('/')
