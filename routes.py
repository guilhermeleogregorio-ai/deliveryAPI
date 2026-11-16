from fastapi import APIRouter, Depends, HTTPException
from models import Usuario,db
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido
# AUTH (Autenticação)
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autentica ção do sistema
    """
    return{"mensagem":"Você acabou de acessar a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(Usuario_schema: UsuarioSchema , session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==Usuario_schema.email).first()
    if usuario:
        return HTTPException(status_code=400, detail="Já existe um usuario com esse email")
    else:
        senha_criptografada = bcrypt_context.hash(Usuario_schema.senha)
        novo_usuario = Usuario(Usuario_schema.nome, Usuario_schema.email, senha_criptografada, Usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem" : f"usuario cadastrado com sucesso {Usuario_schema.email}"}


#ORDER (Pedidos)

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=PedidoSchema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return{"mensagem" : f"Pedido criado com sucesso. ID do pedido {novo_pedido.id}"}