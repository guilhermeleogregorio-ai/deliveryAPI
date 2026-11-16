from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os 

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from routes import auth_router, order_router

app.include_router(auth_router)
app.include_router(order_router)

# para rodar o nosso código, executar no terminal: uvicorn main:app --reload