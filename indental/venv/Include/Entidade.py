class EntidadeDominio(object):
    id = None

    def __init__(self):
        return


class Usuario(EntidadeDominio):
    dataCadastro = None
    status = None
    login = None
    senha = None
    nivelAcesso = None

    def __init__(self):
        super().__init__()
        return


class Pessoa(EntidadeDominio):
    dataCadastro = None
    status = None
    nome = None
    sobrenome = None
    dataNascimento = None
    sexo = None
    rg = None
    cpf = None
    email = None

    def __init__(self):
        super().__init__()
        return


class Funcionario(EntidadeDominio):
    pessoa = Pessoa()
    salario = None
    cargo = None
    usuario = Usuario()

    def __init__(self):
        super().__init__()
        return


class Paciente(EntidadeDominio):
    responsavel = Pessoa()

    def __init__(self):
        super().__init__()
        return


class Endereco(EntidadeDominio):
    cep = None
    numero = None
    rua = None
    bairro = None
    cidade = None
    estado = None

    def __init__(self):
        super().__init__()
        return


class Telefone(EntidadeDominio):
    numero = None
    tipo = None
    ddd = None
    essoa = None

    def __init__(self):
        super().__init__()
        return


class Dentista(EntidadeDominio):
    cro = None
    pessoa = Pessoa()
    usuario = Usuario()

    def __init__(self):
        super().__init__()
        return


class Tratamento(EntidadeDominio):
    descricao = None

    def __init__(self):
        super().__init__()
        return


class Procedimento(EntidadeDominio):
    descricao = None
    tratamento = Tratamento()

    def __init__(self):
        super().__init__()
        return


class Consulta(EntidadeDominio):
    dataHora = None
    dentista = Dentista()
    paciente = Paciente()
    tratamento = Tratamento()

    def __init__(self):
        super().__init__()
        return


class Especialidade(EntidadeDominio):
    nome = None
    valor = None
    status = None

    def __init__(self):
        super().__init__()
        return
