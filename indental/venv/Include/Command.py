import abc

#
#   Strategys devem retornar String com a mensagem de erro ou None caso passou na validação
#
class ICommand(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self):
        return

########################################################

class Salvar(ICommand):

    def __init__(self):
        return

    def executar(self):
        return None

########################################################

class Alterar(ICommand):

    def __init__(self):
        return

    def executar(self):
        return None

########################################################

class Buscar(ICommand):

    def __init__(self):
        return

    def executar(self):
        return None

########################################################

class Listar(ICommand):

    def __init__(self):
        return

    def executar(self):
        return None

########################################################

class Excluir(ICommand):

    def __init__(self):
        return

    def executar(self):
        return None
