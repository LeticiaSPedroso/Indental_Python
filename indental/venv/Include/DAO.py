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

    def altera(self, telefone, tipo, ddd, id):
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

    def altera(self, login, senha, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + "." + self.tabela + " set login = '"+login+"', senha = '"+senha+"'" +
                        "where id = '" + id + "'")
        return

    def logar(self, user, senha):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + "." + self.tabela + " WHERE login = '"+user+"' AND senha = '"+senha+"'")
        return cursor.fetchall()

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

    def altera(self, nome, sobrenome, rg, cpf, sexo, dtnascimento, email, id):
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

        def altera(self, cargo, salario, id):
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

    def altera(self, rua, numero, bairro, cidade, estado, cep, id):
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

    def buscaCpf(self, cpfDentista):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT d.id FROM " + self.base + ".dentista as d " +
                        "inner join " + self.base + ".pessoa p on (p.id = d.idPessoa)" +
                        "where p.cpf = " + cpfDentista)
        data = cursor.fetchone()
        return data[0]

    def salvar(self, cro, idPessoa, idUsuario, idEspecialidade):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + "." + self.tabela + " (cro, idPessoa, idUsuario, idEspecialidade)" +
                       "values('" + cro + "', " + idPessoa + ", " + idUsuario + ", " + idEspecialidade + ")")
        return

    def altera(self, cro, idEspecialidade, id):
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

    def altera(self, nome, valor, status, id):
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

    def buscaCpf(self, cpfPaciente):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT pac.id FROM " + self.base + ".paciente as pac " +
                       "inner join " + self.base + ".pessoa p on (p.id = pac.idPessoa)" +
                       "where p.cpf = '" + cpfPaciente + "'")
        data = cursor.fetchone()
        return data[0]

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

    def altera(self, idResponsavel, id):
        #vai alterar?
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + "." + self.tabela + " set idResponsavel = " + idResponsavel +
            " where id = '" + id + "'")
        return

class ProcedimentoDAO:

    def __init__(self):
        return

    def funcao(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + ".procedimento as p ")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + ".procedimento as p " +
                       "where p.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, descricao, idTratamento):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + ".procedimento (descricao, idTratamento)" +
                       "values('" + descricao + "', " + idTratamento  + ")")
        #id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return

    def altera(self, descricao, idTratamento, id):
        #vai alterar?
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + ".procedimento set descricao = '" + descricao + "', idTratamento = " + idTratamento +
            " where id = '" + id + "'")
        return


class TratamentoDAO:

    def __init__(self):
        return

    def funcao(self):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + ".tratamento as t" +
                    "inner join " + self.base + ".procedimento p on (t.id = p.idTratamento)")
        data = cursor.fetchall()
        return data

    def busca(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + self.base + ".tratamento as t " +
                        "inner join " + self.base + ".procedimento p on (t.id = p.idTratamento)"
                       "where t.id = " + id)
        data = cursor.fetchall()
        return data

    def salvar(self, descricao):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + ".tratamento (descricao)" +
                       "values('" + descricao + "')")
        id = cursor.lastrowid
        # print('id gerado: '+str(id))
        cursor.close()
        return str(id)

    def altera(self, descricao, idTratamento, id):
        #vai alterar?
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + ".tratamento set descricao = '" + descricao + "', idTratamento = " + idTratamento +
            " where id = '" + id + "'")
        return


class HorarioPacienteDAO:

    def __init__(self):
        return

    def lista(self, data, cadeira, id_paciente):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        sql = "SELECT hp.*, DATE_FORMAT(hp.dataHorarioInicio, '%d/%m/%Y') as dtInicio, "
        sql = sql + "DATE_FORMAT(hp.dataHorarioInicio, '%H:%i:%s') as horarioInicio, DATE_FORMAT(hp.dataHorarioTermino,"
        sql = sql + " '%d/%m/%Y') as dtFim, DATE_FORMAT(hp.dataHorarioTermino, '%H:%i:%s') as horarioFim, p.nome, "
        sql = sql + " p.sobrenome, pe.* FROM " + self.base + ".horario_paciente as hp "
        sql = sql + "inner join " + self.base + ".horario_dentista hd "
        sql = sql + "on hd.id = hp.idHorarioDentista left join " + self.base + ".dentista d on d.id = hd.idDentista "
        sql = sql + "left join " + self.base + ".pessoa p on p.id = d.idPessoa "
        sql = sql + "left join " + self.base + ".paciente pac on pac.id = hp.idPaciente "
        sql = sql + "left join " + self.base + ".pessoa pe on pe.id = pac.idPessoa "
        sql = sql + "WHERE hp.status = 0 "

        if data != '':
            sql = sql + "and CAST(hp.dataHorarioInicio as Date) = STR_TO_DATE('" + data + "', '%d/%m/%Y') "
            sql = sql + "and CAST(hp.dataHorarioTermino as Date) = STR_TO_DATE('" + data + "', '%d/%m/%Y') "
        if cadeira != '':
            sql = sql + "and hd.cadeira = " + str(cadeira)
        if id_paciente != '':
            sql = sql + "and pac.id = " + str(id_paciente)

        sql = sql + " order by hp.dataHorarioInicio"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def busca(self, idPaciente, horarioInicio, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        sql = "SELECT hp.*, pd.nome,pd.sobrenome,pp.nome,pp.sobrenome, hd.cadeira, "
        sql = sql + "DATE_FORMAT(hp.dataHorarioInicio, '%d/%m/%Y') as dtInicio, "
        sql = sql + "DATE_FORMAT(hp.dataHorarioInicio, '%H:%i:%s') as horarioInicio "
        sql = sql + "FROM " + self.base + ".horario_paciente as hp "
        sql = sql + "inner join " + self.base + ".horario_dentista hd on hd.id = hp.idHorarioDentista "
        sql = sql + "inner join " + self.base + ".paciente p on p.id = hp.idPaciente "
        sql = sql + "left  join " + self.base + ".pessoa pp on pp.id = p.idPessoa "
        sql = sql + "inner join " + self.base + ".dentista d on d.id = hd.idDentista "
        sql = sql + "left  join " + self.base + ".pessoa pd on pd.id = d.idPessoa where "
        data = ""
        if idPaciente != "" and horarioInicio != "":
            sql = sql + " idPaciente = " + str(idPaciente) + " and "
            sql = sql + "hp.dataHorarioInicio = STR_TO_DATE('" + str(horarioInicio) + "', '%d/%m/%Y %H:%i:%s')"
            cursor.execute(sql)
            data = cursor.rowcount
        elif id != "":
            sql = sql + " hp.id = " + str(id)
            cursor.execute(sql)
            data = cursor.fetchone()
        return data

    def salvar(self, idPaciente, idHorarioDentista, dataHorarioInicio, dataHorarioFim, valor):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("insert into " + self.base + ".horario_paciente (id, idPaciente, idHorarioDentista, " +
                       "dataHorarioInicio, dataHorarioTermino, valor, status, compareceu) " +
                       "values (null, " + str(idPaciente) + ", " + str(idHorarioDentista) + ", " +
                       "STR_TO_DATE('" + str(dataHorarioInicio) + "', '%d/%m/%Y %H:%i:%s'), " +
                       "STR_TO_DATE('" + str(dataHorarioFim) + "', '%d/%m/%Y %H:%i:%s'), " + str(valor) + ", 0, 0)")
        cursor.close()
        return

    def altera(self, id, idPaciente, valor, compareceu, pagou):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        sql = "update " + self.base + ".horario_paciente set "

        if compareceu != '':
            sql = sql + " compareceu = '" + str(compareceu) + "'"
        elif idPaciente != '' and valor != '':
            sql = sql + " idPaciente = '" + str(idPaciente) + "', valor = " + str(valor)
        elif pagou != '':
            sql = sql + " pagou = " + str(pagou)

        sql = sql + " where id = '" + str(id) + "'"

        cursor.execute(sql)
        cursor.close()
        return

    def atualizar_presenca(self, id, compareceu):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("update " + self.base + ".horario_paciente set compareceu = " + str(compareceu) +
                       " where id = '" + str(id) + "'")
        cursor.close()

    def deleta(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("delete from " + self.base + ".horario_paciente where id = " + id)
        return


class HorarioDentistaDAO:

    def __init__(self):
        return

    def lista(self, data, cadeira):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        sql = "SELECT hd.*, DATE_FORMAT(hd.dataHorarioInicio, '%d/%m/%Y') as dtInicio, "
        sql = sql + "DATE_FORMAT(hd.dataHorarioInicio,'%H:%i:%s') as horarioInicio, DATE_FORMAT(hd.dataHorarioTermino,"
        sql = sql + " '%d/%m/%Y') as dtFim, DATE_FORMAT(hd.dataHorarioTermino, '%H:%i:%s') as horarioFim, p.nome, "
        sql = sql + " p.sobrenome FROM " + self.base + ".horario_dentista as hd inner join " + self.base + ".dentista d on "
        sql = sql + "d.id = hd.idDentista inner join " + self.base + ".pessoa p on p.id = d.idPessoa "

        if data != '':
            sql = sql + "WHERE CAST(dataHorarioInicio as Date) = STR_TO_DATE('" + data + "', '%d/%m/%Y') "
            sql = sql + "and CAST(dataHorarioTermino as Date) = STR_TO_DATE('" + data + "', '%d/%m/%Y') "
        if cadeira != '':
            sql = sql + "and cadeira = " + str(cadeira)

        sql = sql + " and hd.status = 0"
        sql = sql + " order by dataHorarioInicio"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def busca(self, idDentista, dataHorarioInicio, dataHorarioTermino, cadeira, status):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        if idDentista == '':
            cursor.execute("SELECT * FROM " + self.base + ".horario_dentista" +
                        " where cadeira = " + str(cadeira) + " and status = " + status +
                        " and (dataHorarioInicio = STR_TO_DATE('" + str(dataHorarioInicio) +
                        "','%d/%m/%Y %H:%i:%s') or " + " dataHorarioTermino = STR_TO_DATE('" + str(dataHorarioTermino) +
                        "','%d/%m/%Y %H:%i:%s'))")
        else:
            cursor.execute("SELECT * FROM " + self.base + ".horario_dentista" +
                        " where idDentista = " + str(idDentista) + " and cadeira = " + str(cadeira) + 
                        " and status = " + status + " and (dataHorarioInicio = STR_TO_DATE('" + str(dataHorarioInicio) +
                        "','%d/%m/%Y %H:%i:%s') or " + " dataHorarioTermino = STR_TO_DATE('" + str(dataHorarioTermino) +
                        "','%d/%m/%Y %H:%i:%s'))")
        
        data = cursor.fetchone()
        return data

    def salvar(self, idDentista, dataHorarioInicio, dataHorarioTermino, cadeira, status):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "insert into " + self.base + ".horario_dentista (idDentista, dataHorarioInicio, dataHorarioTermino, cadeira, " +
            "status) " +
            "values(" + str(idDentista) + ", STR_TO_DATE('" + str(dataHorarioInicio) + "','%d/%m/%Y %H:%i:%s'), " +
            "STR_TO_DATE('" + str(dataHorarioTermino) + "','%d/%m/%Y %H:%i:%s'), " + str(cadeira) + ", " + str(status) +
            ")")

        return

    def altera(self, idDentista, dataHorarioInicio, dataHorarioFim, cadeira, status, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + ".horario_dentista set idDentista = " + str(idDentista) + ", dataHorarioInicio = " +
            " STR_TO_DATE('" + str(dataHorarioInicio) + "','%d/%m/%Y %H:%i:%s'), dataHorarioTermino = " +
            "STR_TO_DATE('" + str(dataHorarioFim) + "','%d/%m/%Y %H:%i:%s'), cadeira = " + str(cadeira) + ", status = "+
            status + " where id = " + id)
        return

    def deleta(self, id):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("delete from " + self.base + ".horario_dentista where id = " + id)
        return

class PagamentoDAO:

    def __init__(self):
        self.tabela = "pagamento_consulta"
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

    def buscaCpf(self, cpfPaciente):
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute("SELECT pac.id FROM " + self.base + ".paciente as pac " +
                       "inner join " + self.base + ".pessoa p on (p.id = pac.idPessoa)" +
                       "where p.cpf = '" + cpfPaciente + "'")
        data = cursor.fetchone()
        return data[0]

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

    def altera(self, idResponsavel, id):
        #vai alterar?
        db = AbstractDAO.getConexao(self)
        cursor = db.cursor()
        cursor.execute(
            "update " + self.base + "." + self.tabela + " set idResponsavel = " + idResponsavel +
            " where id = '" + id + "'")
        return