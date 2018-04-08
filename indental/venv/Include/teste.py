

from templates import *
from classe import *#NomeClasse,FuncionarioDAO
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    cls = NomeClasse()
    retorno = cls.funcao()
    return render_template('hello.html', var = retorno)


@app.route("/listaTelefone")
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


@app.route("/listaFuncionario")
def listaFuncionario():
    cls = FuncionarioDAO()
    retorno = cls.funcao()
    return render_template('listaFuncionario.html', var = retorno)


@app.route("/cadastroFuncionario", methods=['POST'])
def cadastroFuncionario():
    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

    cargo = request.form['txtCargo']
    salario = request.form['txtSalario']

    login = request.form['txtLogin']
    senha = request.form['txtSenha']

    rua = request.form['txtRua']
    numero = request.form['txtNumero']
    bairro = request.form['txtBairro']
    cidade = request.form['txtCidade']
    estado = request.form['txtEstado']
    cep = request.form['txtCep']

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']
    comando = request.form['btnComando']

    clsusuario = UsuarioDAO()
    clspessoa = PessoaDAO()
    clsfuncionario = FuncionarioDAO()
    clsendereco = EnderecoDAO()
    clstelefone = NomeClasse()

    idUsuario = clsusuario.salvar(login, senha)
    idPessoa = clspessoa.salvar(nome, sobrenome, rg, cpf, sexo, dtnascimento, email)
    clsfuncionario.salvar(cargo, salario, idUsuario, idPessoa)
    clsendereco.salvar(rua, numero, bairro, cidade, estado, cep, idPessoa)
    clstelefone.salvar(telefone, tipo, ddd, idPessoa)

    retorno = clsfuncionario.funcao()
    return render_template('listaFuncionario.html', var = retorno)


@app.route("/insertFuncionario")
def hello_world2():
    return render_template('cadastroFuncionario.html')


@app.route("/visualizaFuncionario", methods=['POST'])
def visualizaFuncionario():
    clsfuncionario = FuncionarioDAO()
    id = request.form['txtIdFuncionario']
    retorno = clsfuncionario.busca(id)
    return render_template('visualizaFuncionario.html', var = retorno)


@app.route("/atualizaFuncionario", methods=['POST'])
def atualizaFuncionario():
    idUser = request.form['txtIdUsuario']
    idPes = request.form['txtIdPessoa']
    idFuncionario = request.form['txtIdFuncionario']
    idEndereco = request.form['txtIdEndereco']
    idTelefone= request.form['txtIdTelefone']

    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

    cargo = request.form['txtCargo']
    salario = request.form['txtSalario']

    login = request.form['txtLogin']
    senha = request.form['txtSenha']

    rua = request.form['txtRua']
    numero = request.form['txtNumero']
    bairro = request.form['txtBairro']
    cidade = request.form['txtCidade']
    estado = request.form['txtEstado']
    cep = request.form['txtCep']

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']

    comando = request.form['btnComando']

    clsusuario = UsuarioDAO()
    clspessoa = PessoaDAO()
    clsfuncionario = FuncionarioDAO()
    clsendereco = EnderecoDAO()
    clstelefone = NomeClasse()

    clsusuario.atualiza(login, senha, idUser)
    clspessoa.atualiza(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    clsfuncionario.atualiza(cargo, salario, idFuncionario)
    clsendereco.atualiza(rua, numero, bairro, cidade, estado, cep, idEndereco)
    clstelefone.atualiza(telefone, tipo, ddd, idTelefone)

    retorno = clsfuncionario.funcao()
    return render_template('listaFuncionario.html', var=retorno)



@app.route("/listaDentistas")
def lista_dentista():
    clsdentista = DentistaDAO()
    retorno = clsdentista.funcao()
    return render_template('listaDentistas.html', var=retorno)


@app.route("/cadastroDentista")
def cadastro_dentista():
    return render_template('cadastroDentista.html')


@app.route("/insertDentista", methods=['POST'])
def cadastraDentista():
    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

    especialidade = request.form['txtEspecialidade']
    valor_especialidade = request.form['txtValorEspecialidade']

    cro = request.form['txtCro']

    login = request.form['txtLogin']
    senha = request.form['txtSenha']

    rua = request.form['txtRua']
    numero = request.form['txtNumero']
    bairro = request.form['txtBairro']
    cidade = request.form['txtCidade']
    estado = request.form['txtEstado']
    cep = request.form['txtCep']

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']

    comando = request.form['btnComando']

    clsusuario = UsuarioDAO()
    clspessoa = PessoaDAO()
    clsdentista = DentistaDAO()
    clsespecialidade = EspecialidadeDAO()
    clsendereco = EnderecoDAO()
    clstelefone = NomeClasse()

    idUsuario = clsusuario.salvar(login, senha)
    idPessoa = clspessoa.salvar(nome, sobrenome, rg, cpf, sexo, dtnascimento, email)
    idEspecialidade = clsespecialidade.salvar(especialidade, valor_especialidade)
    clsdentista.salvar(cro, idPessoa, idUsuario, idEspecialidade)
    clsendereco.salvar(rua, numero, bairro, cidade, estado, cep, idPessoa)
    clstelefone.salvar(telefone, tipo, ddd, idPessoa)

    retorno = clsdentista.funcao()
    return render_template('listaDentistas.html', var=retorno)



@app.route("/visualizaDentista", methods=['POST'])
def visualizaDentista():
    clsdentista= DentistaDAO()
    id = request.form['txtIdDentista']
    print(id)
    retorno = clsdentista.busca(id)
    return render_template('visualizaDentista.html', var = retorno)


@app.route("/atualizaDentista", methods=['POST'])
def atualizaDentista():
    idUser = request.form['txtIdUsuario']
    idPes = request.form['txtIdPessoa']
    idDentista = request.form['txtIdDentista']
    idEspecialidade = request.form['txtIdEspecialidade']
    idEndereco = request.form['txtIdEndereco']
    idTelefone= request.form['txtIdTelefone']

    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

    cro = request.form['txtCro']

    login = request.form['txtLogin']
    senha = request.form['txtSenha']

    rua = request.form['txtRua']
    numero = request.form['txtNumero']
    bairro = request.form['txtBairro']
    cidade = request.form['txtCidade']
    estado = request.form['txtEstado']
    cep = request.form['txtCep']

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']
    comando = request.form['btnComando']

    print('Botao Comando: ' + comando)

    clsusuario = UsuarioDAO()
    clspessoa = PessoaDAO()
    clsdentista = DentistaDAO()
    clsendereco = EnderecoDAO()
    clstelefone = NomeClasse()

    clsusuario.atualiza(login, senha, idUser)
    clspessoa.atualiza(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    clsdentista.atualiza(cro, idEspecialidade, idDentista)
    clsendereco.atualiza(rua, numero, bairro, cidade, estado, cep, idEndereco)
    clstelefone.atualiza(telefone, tipo, ddd, idTelefone)

    retorno = clsdentista.funcao()
    return render_template('listaDentistas.html', var=retorno)


app.run()
