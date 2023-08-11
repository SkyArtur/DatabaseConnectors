from tests import *
from objects.connectors import DbSqliteConnector
from db_connector import DbConnector


class TestCaseSqliteConnector(TestCase):

    def setUp(self) -> None:
        self.sqlite_db = DbSqliteConnector(database=SQLITE_DB)
        self.fab = DbConnector('sqlite', database=SQLITE_DB)

    def test_conexao_e_leitura_de_dados(self):
        dados = self.sqlite_db.execute('SELECT * FROM alunos;')
        self.assertIsInstance(dados, list)
        self.assertIsInstance(dados[0], tuple)
        # print(dados)

    def test_conexao_usando_a_factory(self):
        dados = self.sqlite_db.execute('SELECT * FROM alunos;')
        self.assertIsInstance(dados, list)
        self.assertIsInstance(dados[0], tuple)
        # print([dict(id=i[0], nome=i[1]) for i in dados])
