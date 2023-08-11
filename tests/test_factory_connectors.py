import datetime

from tests import *
from db_connector import DbConnector


class TestCaseFactoryDbConnectors(TestCase):

    def setUp(self) -> None:
        self.MYSQL_DB = {
            "database": "estudos",
            "user": "estudante",
            "password": "212223",
            "host": "192.168.1.35"
        }

        self.alunos = [
            ('Aline', 'Dantas', datetime.date(day=5, month=5, year=1998)),
            ('Sandra', 'Machado', datetime.date(day=21, month=10, year=2005)),
            ('Pedro', 'Silva', datetime.date(day=11, month=1, year=2000)),
            ('Marcio', 'Chagas', datetime.date(day=29, month=12, year=1999)),
        ]

    def test_execucao_simple_de_consultas(self):
        self.mysql_db = DbConnector('mysql', **self.MYSQL_DB)
        self.mysql_db.execute('DROP TABLE alunos;')
        self.mysql_db.execute("""
            CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(150) NOT NULL,
                sobrenome VARCHAR(150),
                nascimento DATE 
            );
        """)
        for aluno in self.alunos:
            self.mysql_db.execute("INSERT INTO alunos(nome, sobrenome, nascimento)VALUES (%s, %s, %s)", aluno)
        dados = self.mysql_db.execute('SELECT * FROM alunos;')
        print(dados)
        self.assertEqual(len(dados), 4)
        sandra = self.mysql_db.execute('SELECT nome, sobrenome, nascimento FROM alunos WHERE id = %s;', (2,))
        print(sandra)
        self.assertEqual(sandra[0][0], self.alunos[1][0])

    def test_instancia_sem_parametros(self):
        try:
            self.mysql_db = DbConnector()
        except Exception as err:
            self.assertRaises(TypeError, err)

    def test_instancia_com_parametros_errados(self):
        try:
            self.mysql_db = DbConnector('asdfasfdsa')
        except Exception as err:
            self.assertRaises(TypeError, err)

    def test_passando_parametro_correto_mas_sem_argumentos_nomeados(self):
        self.mysql_db = DbConnector('mysql')
        self.mysql_db.execute('SELECT * FROM alunos;')
