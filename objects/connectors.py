"""
Driver para conexões com banco de dados MySQL, Sqlite3, PostgreSQL.
"""
from .singleton import *


class DbMySqlConnector(SingletonDatabase):
    def __init__(self, **kwargs):
        """
        :param kwargs: {database: str, user: str, password: str, host: str, port: str}
        """
        super().__init__(**kwargs)

    def connection(self) -> mysql.connector.MySQLConnection:
        """Estabelece uma conexão com um banco de dados MySQL."""
        return mysql.connector.connect(**self.database)


class DbPostgresConnector(SingletonDatabase):
    def __init__(self, **kwargs):
        """
        :param kwargs: {database: str, user: str, password: str, host: str, port: str}
        """
        super().__init__(**kwargs)

    def connection(self) -> psycopg2.connect:
        """Estabelece uma conexão com um banco de dados PostgreSQL."""
        return psycopg2.connect(**self.database)


class DbSqliteConnector(SingletonDatabase):
    def __init__(self, **kwargs):
        """
        :param kwargs: {database: nome_arquivo.sqlite}
        """
        super().__init__(**kwargs)

    def connection(self) -> sqlite3.Connection:
        """Estabelece uma conexão com um banco de dados Sqlite3."""
        return sqlite3.connect(**self.database)
