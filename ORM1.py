from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import ambient_variable

engine = create_engine(CONN, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine) # Criando uma sessão baseada no engine
session = Session()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))
    
Base.metadata.create_all(engine)