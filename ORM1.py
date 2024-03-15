from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ambient_variable import CONN


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
    
    def __repr__(self):
        return f"Nome: {self.nome}, Usuário: {self.usuario}, Senha: {self.senha}"
    
class Categoria(Base):
    __tablename__ = "Categoria"
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50))
    
    def __repr__(self):
        return f"categoria: {self.categoria}"
    
class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(50))
    id_categoria = Column(Integer, ForeignKey('Categoria.id'))
        
    def __repr__(self):
        return f"produto: {self.produto}"
    
    
Base.metadata.create_all(engine)