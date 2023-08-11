from unittest import TestCase
import datetime
import json
from pathlib import Path

PATH_FILES = Path(__file__).resolve().parent.parent.joinpath('files')

with open(PATH_FILES.joinpath('json/db.json'), encoding='utf8') as file:
    MYSQL_DB = json.load(file)['MYSQL']

SQLITE_DB = PATH_FILES.joinpath('db.sqlite')



