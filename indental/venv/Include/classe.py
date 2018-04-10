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
        cursor.execute("insert into indentalbd.telefone (numero,tipo,ddd,idPessoa) "+
                       "values('"+str(telefone)+"',"+str(tipo)+",'"+str(ddd)+"',"+str(idPessoa)+")")
        #data = cursor.fetchone()
        return # retorno;

    def atualiza(self, telefone, tipo, ddd, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("update indentalbd.telefone set numero = '"+str(telefone)+"',tipo = '"+str(tipo)+"',"
                        "ddd = '"+str(ddd)+"'" +
                        "where id = '" + id + "'")
        #data = cursor.fetchone()
        return # retorno;


class UsuarioDAO:

    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.usuario")
        data = cursor.fetchall()
        return data

    def salvar(self, login, senha):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.usuario (dataCadastro, status, login, senha, nivelAcesso)"+
                       "values(CURDATE(), 1, '"+login+"', '"+senha+"', 'usuario')")
        id = cursor.lastrowid
        #print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, login, senha, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("update indentalbd.usuario set login = '"+login+"', senha = '"+senha+"'" +
                        "where id = '" + id + "'")
        return

class PessoaDAO:

    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.pessoa")
        data = cursor.fetchall()
        return data

    def salvar(self, nome, sobrenome, rg, cpf, sexo, dtnascimento, email):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.pessoa (dataCadastro, status, nome, sobrenome, dataNascimento, sexo, "+
                       "rg, cpf, email) values(CURDATE(), 1, '"+nome+"', '"+sobrenome+"', "+
                       "STR_TO_DATE('"+dtnascimento+"','%d/%m/%Y'), '"+sexo + "', '" +rg + "', '" + cpf + "', "+
                       "'"+email+"')")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, nome, sobrenome, rg, cpf, sexo, dtnascimento, email, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("update indentalbd.pessoa set nome = '"+nome+"', sobrenome = '"+sobrenome+"', " +
                        "dataNascimento = STR_TO_DATE('"+dtnascimento+"','%d/%m/%Y'), sexo = '"+sexo+"', " +
                        "rg = '" + rg + "', cpf = '" + cpf + "', email = '" + email + "'"
                        "where id = '" + id + "'")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)


class FuncionarioDAO:
        variavel = 'Daphne'
        usuario = 'admin'
        password = 'admin'

        def __init__(self):
            return

        def funcao(self):
            db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM indentalbd.funcionario as f " +
                            "inner join indentalbd.usuario u on (u.id = f.idUsuario)" +
                            "inner join indentalbd.pessoa p on (p.id = f.idPessoa)" +
                            "inner join indentalbd.endereco e on (e.idPessoa = f.idPessoa)" +
                            "inner join indentalbd.telefone t on (t.idPessoa = f.idPessoa)")
            data = cursor.fetchall()
            return data

        def busca(self, id):
            db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM indentalbd.funcionario as f " +
                            "inner join indentalbd.usuario u on (u.id = f.idUsuario)" +
                            "inner join indentalbd.pessoa p on (p.id = f.idPessoa)" +
                            "inner join indentalbd.endereco e on (e.idPessoa = f.idPessoa)" +
                            "inner join indentalbd.telefone t on (t.idPessoa = f.idPessoa)"
                            "where f.id = "+id)
            data = cursor.fetchall()
            return data

        def salvar(self, cargo, salario, idUsuario, idPessoa):
            db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
            cursor = db.cursor()
            cursor.execute("insert into indentalbd.funcionario (idPessoa, salario, cargo, idUsuario)" +
                           "values(" + str(idPessoa) + ", " + salario + ", " + cargo + ", " + str(idUsuario)+")")
            return

        def atualiza(self, cargo, salario, id):
            db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
            cursor = db.cursor()
            cursor.execute("update indentalbd.funcionario set salario = " + salario + ", cargo = " + cargo +
                           " where id = '" + id + "'")
            return


class EnderecoDAO:

    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.endereco")
        data = cursor.fetchall()
        return data

    def salvar(self, rua, numero, bairro, cidade, estado, cep, IdPessoa):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.endereco (cep, numero, rua, bairro, cidade, estado, idPessoa)"+
                       "values('"+cep+"', '"+numero+"', '"+rua+"', '"+bairro+"','"+cidade+"','"+estado+"',"+
                       str(IdPessoa)+")")
        return

    def atualiza(self, rua, numero, bairro, cidade, estado, cep, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password , db='indentalbd')
        cursor = db.cursor()
        cursor.execute("update indentalbd.endereco set cep = '"+cep+"', numero = '"+numero+"', rua = '"+rua+"', " +
                        "bairro = '"+bairro+"',cidade = '"+cidade+"',estado = '"+estado+"'" +
                        "where id = '"+id+"'")
        return


class DentistaDAO:
    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.dentista as d " +
                "inner join indentalbd.especialidade esp on (esp.id = d.idEspecialidade)" +
                "inner join indentalbd.usuario u on (u.id = d.idUsuario)" +
                "inner join indentalbd.pessoa p on (p.id = d.idPessoa)" +
                "inner join indentalbd.endereco e on (e.idPessoa = d.idPessoa)" +
                "inner join indentalbd.telefone t on (t.idPessoa = d.idPessoa)")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.dentista as d " +
                "inner join indentalbd.especialidade esp on (esp.id = d.idEspecialidade)" +
                "inner join indentalbd.usuario u on (u.id = d.idUsuario)" +
                "inner join indentalbd.pessoa p on (p.id = d.idPessoa)" +
                "inner join indentalbd.endereco e on (e.idPessoa = d.idPessoa)" +
                "inner join indentalbd.telefone t on (t.idPessoa = d.idPessoa)" +
                "where d.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, cro, idPessoa, idUsuario, idEspecialidade):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.dentista (cro, idPessoa, idUsuario, idEspecialidade)" +
                       "values('" + cro + "', " + idPessoa + ", " + idUsuario + ", " + idEspecialidade + ")")
        return

    def atualiza(self, cro, idEspecialidade, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute(
            "update indentalbd.dentista set cro = '" + cro + "', idEspecialidade = " + idEspecialidade +
            " where id = " + id)
        return


class EspecialidadeDAO:
    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.especialidade")
        data = cursor.fetchall()
        return data

    def salvar(self, nome, valor):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.especialidade (nome, valor, status)" +
                       "values('" + nome + "', " + valor + ", 1)")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, nome, valor, status, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute(
            "update indentalbd.especialidade set nome = '" + nome + "', valor = " + valor + ", status = '"+status+"'," +
            "where id = '" + id + "'")
        return


class PacienteDAO:
    variavel = 'Daphne'
    usuario = 'admin'
    password = 'admin'

    def __init__(self):
        return

    def funcao(self):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.paciente as pa " +
                "inner join indentalbd.pessoa p on (p.id = pa.idPessoa)" +
                "inner join indentalbd.endereco e on (e.idPessoa = pa.idPessoa)" +
                "inner join indentalbd.telefone t on (t.idPessoa = pa.idPessoa)")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indentalbd.paciente as pa " +
                       "inner join indentalbd.pessoa p on (p.id = pa.idPessoa)" +
                       "inner join indentalbd.endereco e on (e.idPessoa = pa.idPessoa)" +
                       "inner join indentalbd.telefone t on (t.idPessoa = pa.idPessoa)" +
                       "where pa.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, idResponsavel, idPessoa):
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute("insert into indentalbd.paciente (idResponsavel, idPessoa)" +
                       "values(" + idResponsavel + ", " + idPessoa  + ")")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, idResponsavel, id):
        #vai atualizar?
        db = MySQLdb.connect(host='localhost', user=self.usuario, password=self.password, db='indentalbd')
        cursor = db.cursor()
        cursor.execute(
            "update indentalbd.paciente set idResponsavel = " + idResponsavel +
            " where id = '" + id + "'")
        return
