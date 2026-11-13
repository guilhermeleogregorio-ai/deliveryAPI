from fastapi import FastAPI

app = FastAPI()

from routes import auth_router, order_router
# para rodar o nosso código, executar no terminal: uvicorn main:app --reload