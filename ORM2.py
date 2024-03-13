from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM1 import Pessoa
import ambient_variable



def ReturnSession():
    USUARIO = "root"
    PASSWORD = "sousa123"
    HOST = "localhost"
    PORT = "3306"
    BANCO = "AulaPython"
    CONN = f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine) # Criando uma sessão baseada no engine
    return Session()

session = ReturnSession()

x = Pessoa(nome="Allison", 
           usuario="allison", 
           senha="1234")

session.add(x)
session.commit()