from sqlalchemy import create_engine, Column,String,Integer,Boolean,Float,ForeignKey
from sqlalchemy.orm import declarative_base

#cria conexão
db = create_engine("sqlite:///banco.bd")

#cria a base do banco
Base = declarative_base()

#cria as classes/tabelas 
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id",Integer,primary_key= True, autoincrement= True)
    nome = Column("nome", String)
    email = Column("email",String,nullable=False)
    senha = Column("senha",String)
    ativo = Column("ativo",Boolean)
    admin = Column("admin",Boolean, default=False)

    def __init__(self,nome,email,senha,ativo,admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
#Pedido
#ItensPedido

#executa a criação dos metados do seu banco 

