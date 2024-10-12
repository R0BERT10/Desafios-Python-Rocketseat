from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def create_database():
    '''Cria uma nova base de dado com todas as tabelas caso ainda não exista.'''
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        db.create_all()