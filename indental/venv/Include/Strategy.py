import abc

#
#   Strategys devem retornar String com a mensagem de erro ou None caso passou na validação
#
class IStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def processar(self):
        return

########################################################

class ValidaCPF():

    def __init__(self):
        return

    def processar(self):
        return None

########################################################