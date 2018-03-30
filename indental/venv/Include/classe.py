import MySQLdb

class NomeClasse:
    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.telefone")
        data = cursor.fetchall()

        # print(data)
        # print(data[1])
        # PYTHON É A MELHO LINGUAGEM DO MUNDO!!!
        return data

    def salvar(self, telefone, tipo, ddd, idPessoa):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.telefone "+
                       "values(2,'"+telefone+"',"+tipo+",'"+ddd+"',"+idPessoa+")")
        #data = cursor.fetchone()
        #print(data)
        #print(data[1])
        # PYTHON É A MELHO LINGUAGEM DO MUNDO!!!
        return