# DatabaseConnectors
Projeto de auxílio pedagógico no estudo de banco de dados e linguagem SQL e Python. Pretende facilitar a conexão com 
diferentes tipos de banco de dados durante o estudo de integração das linguagens Python e SQL. Permite conexão com
banco de dados Postgres, Mysql, Sqlite. 

#### Alguns tópicos Python trabalhados neste projeto:
- Python Básico: type hinting, estruturas lógicas condicionais, tratamento de exceções, coleções, args & kwargs;
- OOP: herança simples, polimorfismo, atribuição;
- Patterns: Singleton - SingletonDatabase(), Simple Factory - DbConnectors();

## Requerimentos
O módulo é pensado para ser adicionado a um projeto logo, execute o código a seguir para instalar as bibliotecas 
necessárias, a partir da raiz do projeto.
```shell
pip install -r ./DatabaseConnectors/requirements.txt
```

## Exemplos básicos de utilização:

### Sqlite / PostgreSQL / MySQL

```python
from DatabaseConnectors import DbConnectors

# Dados para conexão, preferencialmente em um tipo dict().
database = {
    "database": "estudos",
    "user": "skyartur",
    "password": "259101",
    "host": "192.168.1.25"
}
file_sqlite = dict(database='./files/db.sqlite')

# Definindo bancos de dados diferentes.
db_sqlite = DbConnectors('sqlite', **file_sqlite).connect
db_postgres = DbConnectors('postgresql', **database).connect
db_mysql = DbConnectors('mysql', **database).connect

# Criando tabelas com as diferentes sintaxes.
db_sqlite.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL 
);
''')

db_postgres.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL 
);
''')

db_mysql.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL 
);
''')

# Inserindo dados com as diferentes sintaxes.
alunos = ['Aline', 'Pedro', 'Bianca', 'Charles']

for nome in alunos:
    db_sqlite.execute('INSERT INTO alunos (nome) VALUES (?)', (nome,))
    db_postgres.execute('INSERT INTO alunos (nome) VALUES (%s);', (nome,))
    db_mysql.execute('INSERT INTO alunos (nome) VALUES (%s);', (nome,))

# Verificando dados dos bancos
mensagem = 'Dados fornecidos pelo conector {}:\n{}'
print(mensagem.format(db_sqlite, db_sqlite.execute('SELECT * FROM alunos;')))
print(mensagem.format(db_postgres, db_postgres.execute('SELECT * FROM alunos;')))
print(mensagem.format(db_mysql, db_mysql.execute('SELECT * FROM alunos;')))
```
Saída:
```shell
Dados fornecidos pelo conector DbSqliteConnector:
[(1, 'Aline'), (2, 'Pedro'), (3, 'Bianca'), (4, 'Charles')]
Dados fornecidos pelo conector DbPostgresConnector:
[(1, 'Aline'), (2, 'Pedro'), (3, 'Bianca'), (4, 'Charles')]
Dados fornecidos pelo conector DbMySqlConnector:
[(1, 'Aline'), (2, 'Pedro'), (3, 'Bianca'), (4, 'Charles')]
```
