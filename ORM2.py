from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import or_
from ORM1 import Pessoa
from ambient_variable import CONN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM1 import Pessoa
from ambient_variable import CONN


def ReturnSession():
    USUARIO = "root"
    PASSWORD = "sousa123"
    HOST = "localhost"
    PORT = "3306"
    BANCO = "AulaPython"
    CONN = f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=False)
    Base = declarative_base()
    Session = sessionmaker(bind=engine) # Criando uma sessão baseada no engine
    return Session()

session = ReturnSession()

x = session.query(Pessoa).filter(Pessoa.nome == "Lucas").delete()
print(x)