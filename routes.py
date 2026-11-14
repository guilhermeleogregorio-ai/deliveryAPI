from fastapi import APIRouter
from models import Usuario,db
from sqlalchemy.orm import sessionmaker


# AUTH (Autenticação)
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autentica ção do sistema
    """
    return{"mensagem":"Você acabou de acessar a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str, nome:str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem" : "Já existe um usuario com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem" : "usuario cadastrado com sucesso"}


#ORDER (Pedidos)

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota de pedidos"}