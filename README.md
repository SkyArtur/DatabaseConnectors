# DatabaseConnectors
Projeto de auxílio pedagógico no estudo de banco de dados e liguagem SQL e Python. Pretende facilitar a conexão com 
diferentes tipos de banco de dados durante o estudo de integração das linguagens Python e SQL. Permite conexão com
banco de dados Postgres, Mysql, Sqlite.

## Requerimentos
Execute o código a seguir para instalar as bibliotecas necessárias.
```shell
pip install -r requirements.txt
```

## Exemplos:

### Sqlite3

```python
from DatabaseConnectors import DbConnectors

db_sqlite = DbConnectors('sqlite', database='./files/db.sqlite').connect

db_sqlite.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL 
);
''')

db_sqlite.execute('INSERT INTO alunos (nome) VALUES (?);', ('Aline',))
db_sqlite.execute('INSERT INTO alunos (nome) VALUES (?);', ('Pedro',))
db_sqlite.execute('INSERT INTO alunos (nome) VALUES (?);', ('Bianca',))
db_sqlite.execute('INSERT INTO alunos (nome) VALUES (?);', ('Charles',))

print(db_sqlite.execute('SELECT * FROM alunos;'))
```
Saída:
```shell
[(1, 'Aline'), (2, 'Pedro'), (3, 'Bianca'), (4, 'Charles')]
```


