# Pause: Pausa para a Saúde Mental

Este projeto é uma plataforma web desenvolvida para oferecer apoio psicológico a estudantes universitários, conectando-os com voluntários de psicologia. O objetivo é promover saúde mental, acolhimento e suporte emocional de forma acessível e segura.

## Funcionalidades

- Cadastro de usuários (estudantes e voluntários)
- Login seguro
- Chat para conversas entre estudantes e voluntários
- Edição de perfil do usuário
- Recuperação de senha
- Interface responsiva e acessível

## Tecnologias Utilizadas

- **Backend:** Python, Flask, psycopg2
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Banco de Dados:** PostgreSQL

## Estrutura do Projeto

```
Backend/
  app.py                # Arquivo principal do backend Flask
  requirements.txt      # Dependências do projeto
  database/
    conexao.py          # Conexão com o banco de dados
    routes/             # Rotas Flask (login, cadastro, etc)
    templates/          # Templates HTML do backend
frontend/
  assets/               # CSS, JS e imagens
  templatesPages/       # Páginas HTML do frontend
```

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r Backend/requirements.txt
   ```
3. **Configure o banco de dados:**
   - Crie um banco PostgreSQL chamado `projeto`.
   - Execute o script `Backend/database/templateSql.sql` para criar as tabelas.
   - Ajuste as credenciais em `Backend/database/conexao.py` se necessário.
4. **Inicie o servidor Flask:**
   ```bash
   cd Backend
   python app.py
   ```
5. **Acesse o sistema:**
   - Abra o navegador e acesse `http://localhost:5000`

## Observações

- O projeto está em desenvolvimento e pode conter áreas a serem aprimoradas.
- Para contribuir, faça um fork e envie um pull request.

## Licença

Este projeto é open-source e está sob a licença MIT.
