from fastapi import APIRouter, Depends, HTTPException
from models import Usuario,db
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

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
    usuario = session.query(Usuario).filter(Usuario.email==UsuarioSchema.email).first()
    if usuario:
        return HTTPException(status_code=400, detail="Já existe um usuario com esse email")
    else:
        senha_criptografada = bcrypt_context.hash(UsuarioSchema.senha)
        novo_usuario = Usuario(UsuarioSchema.nome, UsuarioSchema.email, senha_criptografada, UsuarioSchema.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem" : f"usuario cadastrado com sucesso {UsuarioSchema.email}"}


#ORDER (Pedidos)

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota de pedidos"}