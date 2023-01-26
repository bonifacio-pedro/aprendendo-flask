from flask import Flask,render_template, url_for, request
# Url for é para adicionar os Statics de forma simples.

app = Flask(__name__) # Iniciando app fazendo referencia ao nome do arquivo "app"


# Rotas são passadas com esse simbolo "@", essa é uma rota Index
@app.route('/')
def index(): # O que a rota faz
    return render_template('index.html') # Se o nome da pasta estiver certo, basta passar o arquivo.

@app.route('/nome', methods=['POST'])
def nome():
    if request.method == 'POST':
        name = request.form['nome']
        return render_template('index.html', user=name)

@app.route('/<string:any>')
def erro(any):
    return "<h1>404 {} não existe</h1>".format(any)

if __name__ == "__main__": # Se for o arquivo principal
    app.run(debug=True) # Para caso erro, mostrar na tela