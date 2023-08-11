import mysql.connector
import psycopg2
import sqlite3
from abc import abstractmethod


class Connector:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or cls.__instance is None:
            cls.__instance = super(Connector, cls).__new__(cls)
        return cls.__instance

    def __init__(self, **kwargs):
        self.database = kwargs
        self.__connect = None
        self.__cursor = None

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def connection(self):
        """Implementar retorno de conexão com o banco de dados opcional."""
        ...

    def execute(self, query: str, data: tuple = None, /) -> list[tuple] | None:
        """Executa uma query no banco de dados conectado.

        :param query: Query sql para execução.
        :param data: Dados para inserções, consultas e afins.
        :return: list[tuple] | None
        """
        try:
            self.__connect = self.connection()
            self.__cursor = self.__connect.cursor()
            if not data:
                self.__cursor.execute(query)
            else:
                self.__cursor.execute(query, data)
            response = self.__cursor.fetchall() if 'SELECT' in query else None
            self.__connect.commit()
        except (mysql.connector.Error, sqlite3.Error, psycopg2.Error, RuntimeError) as err:
            print(f'{self}:: ERROR QUERY :: {query}\n{err}')
        else:
            return response
        finally:
            try:
                self.__cursor.close()
                self.__connect.close()
            except (AttributeError, mysql.connector.Error) as err:
                print(f'{self} :: ERROR QUERY :: {query}\n{err}\nVerifique dados de conexão.')
