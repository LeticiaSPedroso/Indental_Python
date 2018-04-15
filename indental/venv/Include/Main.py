

from templates import *
from DAO import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    DAO = TelefoneDAO()
    retorno = DAO.listar()
    return render_template('hello.html', var = retorno)

@app.route("/listaTelefone")
def lista():
    DAO = TelefoneDAO()
    retorno = DAO.listar()
    return render_template('lista.html', var = retorno)


@app.route("/cadastro", methods=['POST'])
def cadastro():

    telefone = request.form['txtTelefone']
    tipo = request.form['txtTipo']
    ddd = request.form['txtDdd']
    idPessoa = request.form['txtIdPessoa']
    comando = request.form['btnComando']

    print('Botao Comando: ' + comando)

    DAO = TelefoneDAO()
    retorno = DAO.salvar(telefone, tipo, ddd, idPessoa)
    return render_template('hello.html', var = retorno)


@app.route("/listaFuncionario")
def listaFuncionario():
    DAO = FuncionarioDAO()
    retorno = DAO.listar()
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

    DAOusuario = UsuarioDAO()
    DAOpessoa = PessoaDAO()
    DAOfuncionario = FuncionarioDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    idUsuario = DAOusuario.salvar(login, senha)
    idPessoa = DAOpessoa.salvar(nome, sobrenome, rg, cpf, sexo, dtnascimento, email)
    DAOfuncionario.salvar(cargo, salario, idUsuario, idPessoa)
    DAOendereco.salvar(rua, numero, bairro, cidade, estado, cep, idPessoa)
    DAOtelefone.salvar(telefone, tipo, ddd, idPessoa)

    retorno = DAOfuncionario.listar()
    return render_template('listaFuncionario.html', var = retorno)


@app.route("/insertFuncionario")
def hello_world2():
    return render_template('cadastroFuncionario.html')


@app.route("/visualizaFuncionario", methods=['POST'])
def visualizaFuncionario():
    DAOfuncionario = FuncionarioDAO()
    id = request.form['txtIdFuncionario']
    retorno = DAOfuncionario.busca(id)
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

    DAOusuario = UsuarioDAO()
    DAOpessoa = PessoaDAO()
    DAOfuncionario = FuncionarioDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    DAOusuario.atualiza(login, senha, idUser)
    DAOpessoa.atualiza(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOfuncionario.atualiza(cargo, salario, idFuncionario)
    DAOendereco.atualiza(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.atualiza(telefone, tipo, ddd, idTelefone)

    retorno = DAOfuncionario.listar()
    return render_template('listaFuncionario.html', var=retorno)



@app.route("/listaDentistas")
def lista_dentista():
    DAOdentista = DentistaDAO()
    retorno = DAOdentista.listar()
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

    DAOusuario = UsuarioDAO()
    DAOpessoa = PessoaDAO()
    DAOdentista = DentistaDAO()
    DAOespecialidade = EspecialidadeDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    idUsuario = DAOusuario.salvar(login, senha)
    idPessoa = DAOpessoa.salvar(nome, sobrenome, rg, cpf, sexo, dtnascimento, email)
    idEspecialidade = DAOespecialidade.salvar(especialidade, valor_especialidade)
    DAOdentista.salvar(cro, idPessoa, idUsuario, idEspecialidade)
    DAOendereco.salvar(rua, numero, bairro, cidade, estado, cep, idPessoa)
    DAOtelefone.salvar(telefone, tipo, ddd, idPessoa)

    retorno = DAOdentista.listar()
    return render_template('listaDentistas.html', var=retorno)



@app.route("/visualizaDentista", methods=['POST'])
def visualizaDentista():
    DAOdentista= DentistaDAO()
    id = request.form['txtIdDentista']
    print(id)
    retorno = DAOdentista.busca(id)
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

    DAOusuario = UsuarioDAO()
    DAOpessoa = PessoaDAO()
    DAOdentista = DentistaDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    DAOusuario.atualiza(login, senha, idUser)
    DAOpessoa.atualiza(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOdentista.atualiza(cro, idEspecialidade, idDentista)
    DAOendereco.atualiza(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.atualiza(telefone, tipo, ddd, idTelefone)

    retorno = DAOdentista.listar()
    return render_template('listaDentistas.html', var=retorno)



@app.route("/listaPacientes")
def listaPacientes():
    DAOpaciente = PacienteDAO()
    retorno = DAOpaciente.listar()
    return render_template('listaPacientes.html', var=retorno)


@app.route("/cadastroPaciente")
def cadastroPaciente():
    return render_template('cadastroPaciente.html')


@app.route("/insertPaciente", methods=['POST'])
def insertPaciente():

    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

    idResponsavel = request.form['txtIdReponsavel']

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

    DAOpessoa = PessoaDAO()
    DAOpaciente = PacienteDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    idPessoa = DAOpessoa.salvar(nome, sobrenome, rg, cpf, sexo, dtnascimento, email)
    DAOpaciente.salvar(idResponsavel, idPessoa)
    DAOendereco.salvar(rua, numero, bairro, cidade, estado, cep, idPessoa)
    DAOtelefone.salvar(telefone, tipo, ddd, idPessoa)

    retorno = DAOpaciente.listar()
    return render_template('listaPacientes.html', var=retorno)



@app.route("/visualizaPaciente", methods=['POST'])
def visualizaPaciente():
    DAOpaciente = PacienteDAO()
    id = request.form['txtIdPaciente']
    retorno = DAOpaciente.busca(id)
    return render_template('visualizaPaciente.html', var = retorno)


@app.route("/atualizaPaciente", methods=['POST'])
def atualizaPaciente():
    idPes = request.form['txtIdPessoa']
    idResponsavel = request.form['txtIdResponsavel']
    idPaciente = request.form['txtIdPaciente']
    idEndereco = request.form['txtIdEndereco']
    idTelefone= request.form['txtIdTelefone']

    nome = request.form['txtNome']
    sobrenome = request.form['txtSobrenome']
    rg = request.form['txtRg']
    cpf = request.form['txtCpf']
    sexo = request.form['txtSexo']
    dtnascimento = request.form['txtDataNascimento']
    email = request.form['txtEmail']

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

    DAOpessoa = PessoaDAO()
    DAOpaciente = PacienteDAO()
    DAOendereco = EnderecoDAO()
    DAOtelefone = TelefoneDAO()

    DAOpessoa.atualiza(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOpaciente.atualiza(idResponsavel, idPaciente)
    DAOendereco.atualiza(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.atualiza(telefone, tipo, ddd, idTelefone)

    retorno = DAOpaciente.listar()
    return render_template('listaPacientes.html', var=retorno)


app.run(port=4996)