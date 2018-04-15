
import Entidade
import Strategy
import DAO

class Fachada(object):

    listaDAO = {
        Entidade.Usuario(): DAO.UsuarioDAO(),
        Entidade.Telefone(): DAO.Telefone(),
        Entidade.Funcionario(): DAO.Funcionario(),
        Entidade.Pessoa(): DAO.Pessoa(),
        Entidade.Paciente(): DAO.Paciente(),
        Entidade.Endereco(): DAO.Endereco(),
        Entidade.Dentista(): DAO.Dentista()
    }

    def __init__(self):
        return

    def salvar(entidade):

        return