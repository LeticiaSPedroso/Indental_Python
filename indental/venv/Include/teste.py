#variavel = 'Daphneeee'
#print('Hello World ' + variavel)
from templates import *
from classe import NomeClasse
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    cls = NomeClasse()
    retorno = cls.funcao()
    return render_template('hello.html', var = retorno)

@app.route("/lista")
def lista():
    cls = NomeClasse()
    retorno = cls.funcao()
    return render_template('lista.html', var = retorno)

@app.route("/cadastro", methods=['POST'])
def cadastro():

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']
    idPessoa = request.form['txtIdPessoa']
    comando = request.form['btnComando']

    print('Botao Comando: ' + comando)

    cls = NomeClasse()
    retorno = cls.salvar(telefone, tipo, ddd, idPessoa)
    return 'oi'#render_template('hello.html', var = retorno)

app.run()