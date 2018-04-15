import MySQLdb
import abc


class AbstractDAO(metaclass=abc.ABCMeta):

    def __init__(self):
        return

    def getConexao(self):
        self.url = 'localhost'
        self.usuario = 'root'
        self.password = 'admin'
        self.base = 'indentalbd'

        return MySQLdb.connect(host=self.url, user=self.usuario, password=self.password, db=self.base)

class TelefoneDAO(AbstractDAO):

    def __init__(self):
        self.tabela = "telefone"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela)
        data = cursor.fetchall()

        return data

    def salvar(self, telefone, tipo, ddd, idPessoa):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (numero,tipo,ddd,idPessoa) "+
                       "values('"+str(telefone)+"',"+str(tipo)+",'"+str(ddd)+"',"+str(idPessoa)+")")
        #data = cursor.fetchone()
        return # retorno;

    def atualiza(self, telefone, tipo, ddd, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + "." + self.tabela + " set "
                       "numero = '"+str(telefone)+"', "
                       "tipo = '"+str(tipo)+"', "
                       "ddd = '"+str(ddd)+"' " +
                       "where id = '" + id + "'")
        #data = cursor.fetchone()
        return # retorno;


class UsuarioDAO:

    def __init__(self):
        self.tabela = "usuario"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela)
        data = cursor.fetchall()
        return data

    def salvar(self, login, senha):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (dataCadastro, status, login, senha, nivelAcesso)"+
                       "values(CURDATE(), 1, '"+login+"', '"+senha+"', 'usuario')")
        id = cursor.lastrowid
        #print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, login, senha, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + "." + self.tabela + " set login = '"+login+"', senha = '"+senha+"'" +
                        "where id = '" + id + "'")
        return

class PessoaDAO:

    def __init__(self):
        self.tabela = "pessoa"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela)
        data = cursor.fetchall()
        return data

    def salvar(self, nome, sobrenome, rg, cpf, sexo, dtnascimento, email):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (dataCadastro, status, nome, sobrenome, dataNascimento, sexo, "+
                       "rg, cpf, email) values(CURDATE(), 1, '"+nome+"', '"+sobrenome+"', "+
                       "STR_TO_DATE('"+dtnascimento+"','%d/%m/%Y'), '"+sexo + "', '" +rg + "', '" + cpf + "', "+
                       "'"+email+"')")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, nome, sobrenome, rg, cpf, sexo, dtnascimento, email, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + "." + self.tabela + " set nome = '"+nome+"', sobrenome = '"+sobrenome+"', " +
                        "dataNascimento = STR_TO_DATE('"+dtnascimento+"','%d/%m/%Y'), sexo = '"+sexo+"', " +
                        "rg = '" + rg + "', cpf = '" + cpf + "', email = '" + email + "'"
                        "where id = '" + id + "'")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)


class FuncionarioDAO:

        def __init__(self):
            self.tabela = "funcionario"
            return

        def listar(self):
            db = AbstractDAO.getConexao(self)
            cursor = db.cursor()
            cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as f " +
                            "inner join " + self.base + ".usuario u on (u.id = f.idUsuario)" +
                            "inner join " + self.base + ".pessoa p on (p.id = f.idPessoa)" +
                            "inner join " + self.base + ".endereco e on (e.idPessoa = f.idPessoa)" +
                            "inner join " + self.base + ".telefone t on (t.idPessoa = f.idPessoa)")
            data = cursor.fetchall()
            return data

        def busca(self, id):
            db = AbstractDAO.getConexao(self)
            cursor = db.cursor()
            cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as f " +
                            "inner join " + self.base + ".usuario u on (u.id = f.idUsuario)" +
                            "inner join " + self.base + ".pessoa p on (p.id = f.idPessoa)" +
                            "inner join " + self.base + ".endereco e on (e.idPessoa = f.idPessoa)" +
                            "inner join " + self.base + ".telefone t on (t.idPessoa = f.idPessoa)"
                            "where f.id = "+id)
            data = cursor.fetchall()
            return data

        def salvar(self, cargo, salario, idUsuario, idPessoa):
            db = AbstractDAO.getConexao(self)
            cursor = db.cursor()
            cursor.execute("insert into " + self.base + "." + self.tabela + " (idPessoa, salario, cargo, idUsuario)" +
                           "values(" + idPessoa + ", " + salario + ", '" + cargo + "', " + idUsuario +")")
            return

        def atualiza(self, cargo, salario, id):
            db = AbstractDAO.getConexao(self)
            cursor = db.cursor()
            cursor.execute("update " + self.base + "." + self.tabela + " set salario = " + salario + ", cargo = '" + cargo +
                           "' where id = '" + id + "'")
            return


class EnderecoDAO:

    def __init__(self):
        self.tabela = "endereco"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela)
        data = cursor.fetchall()
        return data

    def salvar(self, rua, numero, bairro, cidade, estado, cep, IdPessoa):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (cep, numero, rua, bairro, cidade, estado, idPessoa)"+
                       "values('"+cep+"', '"+numero+"', '"+rua+"', '"+bairro+"','"+cidade+"','"+estado+"',"+
                       str(IdPessoa)+")")
        return

    def atualiza(self, rua, numero, bairro, cidade, estado, cep, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + "." + self.tabela + " set cep = '"+cep+"', numero = '"+numero+"', rua = '"+rua+"', " +
                        "bairro = '"+bairro+"',cidade = '"+cidade+"',estado = '"+estado+"'" +
                        "where id = '"+id+"'")
        return


class DentistaDAO:

    def __init__(self):
        self.tabela = "dentista"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as d " +
                "inner join " + self.base + ".especialidade esp on (esp.id = d.idEspecialidade)" +
                "inner join " + self.base + ".usuario u on (u.id = d.idUsuario)" +
                "inner join " + self.base + ".pessoa p on (p.id = d.idPessoa)" +
                "inner join " + self.base + ".endereco e on (e.idPessoa = d.idPessoa)" +
                "inner join " + self.base + ".telefone t on (t.idPessoa = d.idPessoa)")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as d " +
                "inner join " + self.base + ".especialidade esp on (esp.id = d.idEspecialidade)" +
                "inner join " + self.base + ".usuario u on (u.id = d.idUsuario)" +
                "inner join " + self.base + ".pessoa p on (p.id = d.idPessoa)" +
                "inner join " + self.base + ".endereco e on (e.idPessoa = d.idPessoa)" +
                "inner join " + self.base + ".telefone t on (t.idPessoa = d.idPessoa)" +
                "where d.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, cro, idPessoa, idUsuario, idEspecialidade):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (cro, idPessoa, idUsuario, idEspecialidade)" +
                       "values('" + cro + "', " + idPessoa + ", " + idUsuario + ", " + idEspecialidade + ")")
        return

    def atualiza(self, cro, idEspecialidade, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + "." + self.tabela + " set cro = '" + cro + "', idEspecialidade = " + idEspecialidade +
            " where id = " + id)
        return


class EspecialidadeDAO:

    def __init__(self):
        self.tabela = "especialidade"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela)
        data = cursor.fetchall()
        return data

    def salvar(self, nome, valor):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (nome, valor, status)" +
                       "values('" + nome + "', " + valor + ", 1)")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, nome, valor, status, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + "." + self.tabela + " set nome = '" + nome + "', valor = " + valor + ", status = '"+status+"'," +
            "where id = '" + id + "'")
        return


class PacienteDAO:

    def __init__(self):
        self.tabela = "paciente"
        return

    def listar(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as pa " +
                "inner join " + self.base + ".pessoa p on (p.id = pa.idPessoa)" +
                "inner join " + self.base + ".endereco e on (e.idPessoa = pa.idPessoa)" +
                "inner join " + self.base + ".telefone t on (t.idPessoa = pa.idPessoa)")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " as pa " +
                       "inner join " + self.base + ".pessoa p on (p.id = pa.idPessoa)" +
                       "inner join " + self.base + ".endereco e on (e.idPessoa = pa.idPessoa)" +
                       "inner join " + self.base + ".telefone t on (t.idPessoa = pa.idPessoa)" +
                       "where pa.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, idResponsavel, idPessoa):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (idResponsavel, idPessoa)" +
                       "values(" + idResponsavel + ", " + idPessoa  + ")")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def atualiza(self, idResponsavel, id):
        #vai atualizar?
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + "." + self.tabela + " set idResponsavel = " + idResponsavel +
            " where id = '" + id + "'")
        return
