
from templates import *
from DAO import *
from datetime import datetime
from flask import Flask, render_template, request
from flask import Flask, flash, render_template, request, session
import numpy as np
import os

app = Flask(__name__)

time = ["08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00", "10:30:00", "11:00:00", "11:30:00", "12:00:00",
        "12:30:00", "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00", "15:30:00", "16:00:00", "16:30:00",
        "17:00:00", "17:30:00", "18:00:00", "18:30:00", "19:00:00", "19:30:00", "20:00:00"]


@app.route("/")
def hello_world():
    DAO = TelefoneDAO()
    retorno = DAO.listar()
    return render_template('hello.html', var = retorno)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/logar', methods=['POST'])
def logar():
    DAO = UsuarioDAO()

    login = request.form['user']
    senha = request.form['senha']

    retorno = DAO.logar(login, senha)
    if len(retorno) > 0:
        session['flagLogado'] = True
        session['user'] = login
        session['senha'] = senha
        return render_template('hello.html', var=retorno)
    else:
        flash('Usuario não cadastrado ou senha incorreta!')
        return render_template('login.html', var=retorno)

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


@app.route("/alteraFuncionario", methods=['POST'])
def alteraFuncionario():
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

    DAOusuario.altera(login, senha, idUser)
    DAOpessoa.altera(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOfuncionario.altera(cargo, salario, idFuncionario)
    DAOendereco.altera(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.altera(telefone, tipo, ddd, idTelefone)

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


@app.route("/alteraDentista", methods=['POST'])
def alteraDentista():
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

    DAOusuario.altera(login, senha, idUser)
    DAOpessoa.altera(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOdentista.altera(cro, idEspecialidade, idDentista)
    DAOendereco.altera(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.altera(telefone, tipo, ddd, idTelefone)

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


@app.route("/alteraPaciente", methods=['POST'])
def alteraPaciente():
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

    DAOpessoa.altera(nome, sobrenome, rg, cpf, sexo, dtnascimento, email, idPes)
    DAOpaciente.altera(idResponsavel, idPaciente)
    DAOendereco.altera(rua, numero, bairro, cidade, estado, cep, idEndereco)
    DAOtelefone.altera(telefone, tipo, ddd, idTelefone)

    retorno = DAOpaciente.listar()
    return render_template('listaPacientes.html', var=retorno)


@app.route("/calendario")
def calendario():
    return render_template('calendario.html')


@app.route("/agendaDentista", methods=['POST'])
def agenda():
    data = request.form['txtData']
    cadeira = request.form['txtCadeira']

    clsdentista = DentistaDAO()
    clshorario_dentista = HorarioDentistaDAO()

    retorno = clsdentista.listar()
    horarios = clshorario_dentista.lista(data, cadeira)

    w, h = 500, 500;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    inicio = 0
    houveMudanca = 0
    i = 0

    while i <= 24:
        houveMudanca = 0
        inicio = 1

        for h in horarios:
            #iniciou o algum com esse tempo?
            if (h[7] == time[i]):
                indexInicio = time.index(h[7])
                indexFim = time.index(h[9])
                horaInicio = datetime_object = datetime.strptime(h[7], '%H:%M:%S')
                horaFim = datetime_object = datetime.strptime(h[9], '%H:%M:%S')
                diferenca = (horaFim - horaInicio)
                houveMudanca = 1

                i = time.index(time[i])
                while h[9] != time[i]:
                    Matrix[i][0] = time[i]
                    Matrix[i][1] = h
                    #print(Matrix[i][0])
                    #print(Matrix[i][1])
                    i = i + 1

        if houveMudanca == 0:
            Matrix[i][0] = time[i]
            Matrix[i][1] = ''
            #print(Matrix[i][0])
            #print(Matrix[i][1])
            i = i + 1


    return render_template('agendaDentista.html', horarios=Matrix, var=retorno, cadeira=cadeira, data=data)


@app.route("/salvaHorarioDentista", methods=['POST'])
def salvaHorarioDentista():
    data = request.form['txtDataAgenda']
    cpfDentista = request.form['selectDentista']
    cadeira = request.form['txtCadeira']
    horario_inicio = data + ' ' + request.form['txtHorarioInicio']
    horario_fim = data + ' ' + request.form['txtHorarioFim']

    comando = request.form['btnComando']

    daohorario_dentista = HorarioDentistaDAO()
    daodentista = DentistaDAO()
    idDentista = daodentista.buscaCpf(cpfDentista)
    
    #já existe o mesmo alguem nesta cadeira neste horario?
    #horarioReservado = daohorario_dentista.busca('', horario_inicio, horario_fim, cadeira, '0')
    
    #if horarioReservado is not None:
        #return "<h2>Horário já reservado</h2>"

    daohorario_dentista.salvar(idDentista, horario_inicio, horario_fim, cadeira, '0')

    # lista os horarios de novo e retorna a agenda
    clsdentista = DentistaDAO()
    clshorario_dentista = HorarioDentistaDAO()
    retorno = clsdentista.listar()
    horarios = clshorario_dentista.lista(data, cadeira)

    w, h = 500, 500;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    inicio = 0
    houveMudanca = 0
    i = 0

    while i <= 24:
        houveMudanca = 0
        inicio = 1

        for h in horarios:
            # iniciou o algum com esse tempo?
            if (h[7] == time[i]):
                indexInicio = time.index(h[7])
                indexFim = time.index(h[9])
                horaInicio = datetime_object = datetime.strptime(h[7], '%H:%M:%S')
                horaFim = datetime_object = datetime.strptime(h[9], '%H:%M:%S')
                diferenca = (horaFim - horaInicio)
                houveMudanca = 1

                i = time.index(time[i])
                while h[9] != time[i]:
                    # time[i] = t
                    Matrix[i][0] = time[i]
                    Matrix[i][1] = h
                    i = i + 1
                    # time.index(i)
                    # time[index][1] = h

        if houveMudanca == 0:
            Matrix[i][0] = time[i]
            Matrix[i][1] = ''
            i = i + 1

    return render_template('calendario.html')


@app.route("/alteraHorarioDentista", methods=['POST'])
def alteraHorarioDentista():
    cpfDentista = request.form['selectDentistaEditar']
    cadeira = request.form['selectCadeira']
    horario_inicio = request.form['txtHorarioInicioEditar']
    horario_fim = request.form['txtHorarioFimEditar']
    status = request.form['txtStatus']
    id = request.form['txtId']

    comando = request.form['btnComando']

    daohorario_dentista = HorarioDentistaDAO()
    daodentista = DentistaDAO()
    idDentista = daodentista.buscaCpf(cpfDentista)
    daohorario_dentista.altera(idDentista, horario_inicio, horario_fim, cadeira, status, id)

    # lista os horários de novo e retorna a agenda
    clsdentista = DentistaDAO()
    clshorario_dentista = HorarioDentistaDAO()
    retorno = clsdentista.listar()
    horariosDentista  = clshorario_dentista.lista()
    return render_template('agendaDentista.html', horarios=horariosDentista, var=retorno)


@app.route("/deletaHorarioDentista", methods=['POST'])
def deletaHorarioDentista():
    id = request.form['txtId']

    comando = request.form['btnComando']

    daohorario_dentista = HorarioDentistaDAO()
    daohorario_dentista.deleta(id)

    # volta pro calendario
    return render_template('calendario.html')


@app.route("/calendarioConsulta")
def calendarioConsulta():
    return render_template('calendarioConsulta.html')


@app.route("/agendaConsulta", methods=['POST'])
def agendaConsulta():
    data = request.form['txtData']

    comando = request.form['btnComando']
    cadeira_num = 1
    Matrix = np.zeros((10, 500, 500), dtype=object)  # dtype='U25')

    while cadeira_num <= 5:
        daohorario_paciente = HorarioPacienteDAO()
        horarios = daohorario_paciente.lista(data, cadeira_num)
        #w, h, d = 500, 500, 500;
        #Matrix = [[0 for x in range(w)] for y in range(h) for y in range(d)]
        inicio = 0
        houveMudanca = 0
        i = 0

        while i <= 24:
            print("horario" + time[i])
            print("cadeira_num"+str(cadeira_num))
            houveMudanca = 0
            for h in horarios:
                #iniciou o algum com esse tempo?
                if (h[8] == time[i]):
                    houveMudanca = 1

                    i = time.index(time[i])
                    while h[10] != time[i]:
                        Matrix[cadeira_num, i, 0] = str(time[i])
                        Matrix[cadeira_num, i, 1] = h
                        print(Matrix[cadeira_num, i, 0])
                        print(Matrix[cadeira_num, i, 1])
                        i = i + 1

            if houveMudanca == 0:
                Matrix[cadeira_num, i, 0] = time[i]
                Matrix[cadeira_num, i, 1] = ''
                print(Matrix[cadeira_num, i, 0])
                print(Matrix[cadeira_num, i, 1])
                i = i + 1
        cadeira_num = cadeira_num + 1


    cadeira_num = 1
    MatrixDentista = np.zeros((10, 500, 500), dtype=object)  # dtype='U25')

    while cadeira_num <= 5:
        daohorario_dentista = HorarioDentistaDAO()
        horarios = daohorario_dentista.lista(data, cadeira_num)
        inicio = 0
        houveMudanca = 0
        i = 0

        while i <= 24:
            print("horario" + time[i])
            print("cadeira_num" + str(cadeira_num))
            houveMudanca = 0
            for h in horarios:
                # iniciou o algum com esse tempo?
                if (h[7] == time[i]):
                    houveMudanca = 1

                    i = time.index(time[i])
                    while h[9] != time[i]:
                        MatrixDentista[cadeira_num, i, 0] = str(time[i])
                        MatrixDentista[cadeira_num, i, 1] = h
                        print(MatrixDentista[cadeira_num, i, 0])
                        print(MatrixDentista[cadeira_num, i, 1])
                        i = i + 1

            if houveMudanca == 0:
                MatrixDentista[cadeira_num, i, 0] = time[i]
                MatrixDentista[cadeira_num, i, 1] = ''
                print(MatrixDentista[cadeira_num, i, 0])
                print(MatrixDentista[cadeira_num, i, 1])
                i = i + 1
        cadeira_num = cadeira_num + 1

    # volta pro calendario
    return render_template('agendaConsulta.html',  horariosDe=MatrixDentista, data=data, time=time, horarios=Matrix)


@app.route("/salvaHorarioConsulta", methods=['POST'])
def salvaHorarioConsulta():
    data = request.form['txtDataSalvar']
    valor = request.form['txtValor']
    idHorarioDentista = request.form['txtIdHorario']
    cpf_paciente = request.form['txtCpf']
    horario_inicio = data + ' ' + request.form['txtHorarioInicio']
    horario_fim = data + ' ' + request.form['txtHorarioFim']

    comando = request.form['btnComando']

    daohorario_paciente = HorarioPacienteDAO()
    daopaciente = PacienteDAO()
    idPaciente = daopaciente.buscaCpf(cpf_paciente)

    # eese paciente já esta no mesmo horario em outra cadeira?
    horario = daohorario_paciente.buscaHorarioPaciente(idPaciente, horario_inicio)
    print(horario)
    if horario == 0:
        daohorario_paciente.salvar(idPaciente, idHorarioDentista, horario_inicio, horario_fim, valor)
    else:
        return "paciente já possue uma consulta neste horario!"

    # volta pro calendario
    return "oi"
    #render_template('calendario.html', horariosDe=MatrixDentista, data=data, time=time, horarios=Matrix)


@app.route("/alteraHorarioConsulta", methods=['POST'])
def alteraHorarioConsulta():
    print('veio')
    valor = request.form['txtValorAltera']
    print('valor' + valor)
    id = request.form['txtIdHorarioConsulta']
    print('id ' + id)
    cpf_paciente = request.form['txtCpfAltera']
    print('cpf_paciente ' + cpf_paciente)
    data_horario = request.form['txtHorarioAlterar']
    print('data_horario ' + data_horario)

    comando = request.form['btnComando']

    daohorario_paciente = HorarioPacienteDAO()
    daopaciente = PacienteDAO()
    idPaciente = daopaciente.buscaCpf(cpf_paciente)
    '''
    # eese paciente já esta no mesmo horario em outra cadeira?
    horario = daohorario_paciente.buscaHorarioPaciente(idPaciente, data_horario)
    print(horario)
    if horario == 0:'''
    daohorario_paciente.altera(id, idPaciente, valor)
    '''else:
        return "paciente já possue uma consulta neste horario!"'''

    # volta pro calendario
    return "oi de novo"
    #render_template('calendario.html', horariosDe=MatrixDentista, data=data, time=time, horarios=Matrix)


app.secret_key = os.urandom(12)


app.run(port=4996)