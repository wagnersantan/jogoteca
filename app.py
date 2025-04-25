from flask import Flask, render_template, request, redirect,session,flash

# Definindo a classe do jogo
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# Instância do app Flask
app = Flask(__name__)
app.secret_key = 'alura'

# Lista de jogos (pode ser usada em várias rotas futuramente)
jogos = [
    Jogo('Tetris', 'Puzzle', 'Atari'),
    Jogo('God of War', 'Hack n Slash', 'PS2'),
    Jogo('Mortal Kombat', 'Luta', 'PS2')
]

# Rota principal e alternativa '/inicio'
@app.route('/')
@app.route('/inicio')
def index():
    return render_template("lista.html", titulo='Jogos', jogos=jogos)

# Rota para exibir o formulário de novo jogo
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

# Rota que recebe os dados do formulário e cria um novo jogo
@app.route('/criar', methods=['POST'])
def criar():
    # Coleta os dados enviados pelo formulário
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    # Cria o novo objeto jogo
    jogo = Jogo(nome, categoria, console)

    # Adiciona o novo jogo na lista
    jogos.append(jogo)

    # Redireciona para a página inicial após salvar
    return redirect('/inicio')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if senha == 'alohomora':
        session['usuario_logado'] = usuario
        flash(f'{usuario} logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')
    
# Execução do servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
