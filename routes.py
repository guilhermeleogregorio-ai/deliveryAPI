from fastapi import APIRouter

# AUTH (Autenticação)
auth_router = APIRouter(prefix="/auth", tags=["auth"])

#ORDER (Pedidos)

order_router = APIRouter(prefix="/order", tags=["order"])