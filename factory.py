from objects import DbSqliteConnector, DbPostgresConnector, DbMySqlConnector
from typing import Literal


class DbConnectors:

    def __init__(self, driver: Literal['sqlite', 'postgresql', 'mysql'], **kwargs):
        """Factory para as diferentes instâncias de conectores(DbMySqlConnect, DbPostgresConnect, DbSqliteConnect). A
        @property[connect] Estabelece a conexão com o banco de dados.

        :param driver: String com o nome do driver desejado.
        :param kwargs: Dados para conexão com o banco de dados(database, user, password, host, port).
        """
        if driver in 'sqlite':
            self.__object = DbSqliteConnector(**kwargs)
        elif driver in 'postgresql':
            self.__object = DbPostgresConnector(**kwargs)
        elif driver in 'mysql':
            self.__object = DbMySqlConnector(**kwargs)

    @property
    def connect(self) -> DbSqliteConnector | DbPostgresConnector | DbMySqlConnector:
        """Propriedade retorna uma instância de conector para banco de dados."""
        try:
            return self.__object
        except AttributeError as err:
            print(err)
