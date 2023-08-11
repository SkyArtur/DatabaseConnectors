from objects import DbSqliteConnector, DbPostgresConnector, DbMySqlConnector
from typing import Literal


class DbConnector:
    __instance = None

    def __new__(cls, __driver: Literal['sqlite', 'postgresql', 'mysql'], **kwargs):
        """Factory para as diferentes instâncias de conectores(DbMySqlConnect, DbPostgresConnect, DbSqliteConnect). A
        @property[connect] Estabelece a conexão com o banco de dados.

        :param __driver: String com o nome do driver desejado.
        :param kwargs: Dados para conexão com o banco de dados(database, user, password, host, port).
        """
        try:
            if __driver in 'sqlite':
                cls.__instance = DbSqliteConnector(**kwargs)
            elif __driver in 'postgresql':
                cls.__instance = DbPostgresConnector(**kwargs)
            elif __driver in 'mysql':
                cls.__instance = DbMySqlConnector(**kwargs)
        except AttributeError:
            print(f'{cls.__name__}:: ERROR DRIVER :: {__driver}\nBanco de dados não reconhecido.')
        return cls.__instance

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__str__()
