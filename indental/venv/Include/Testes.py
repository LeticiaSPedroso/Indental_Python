
import Entidade

class Teste:

    listaDAO = {
        Entidade.Usuario().__class__.__name__: "DAO User",
        Entidade.Telefone().__class__.__name__: "DAO Telefone"
    }

    def __init__(self):
        return

    def processa(self):
        print(Teste.listaDAO[Entidade.Usuario().__class__.__name__])
        print(Teste.listaDAO[self.__class__.__name__])

user = Entidade.Usuario()
telefone = Entidade.Telefone()

Teste.processa(user.__class__.__name__)
Teste.processa(telefone.__class__.__name__)
