# Delivery Pizzaria API

API desenvolvida em Python com FastAPI para gerenciamento de autenticação e pedidos de uma pizzaria.

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd deliveryAPI
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Criar o ambiente
   python -m venv .venv

   # Ativar no Windows
   .venv\Scripts\activate

   # Ativar no Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor da API:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação:**
   Abra o navegador e acesse `http://127.0.0` para testar as rotas.
