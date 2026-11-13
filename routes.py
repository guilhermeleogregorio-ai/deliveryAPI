from fastapi import APIRouter

# AUTH (Autenticação)
auth_router = APIRouter(prefix="/auth", tags=["auth"])

#ORDER (Pedidos)

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}