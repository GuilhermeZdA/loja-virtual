from fastapi import FastAPI
from src.api.produto_route import router as rotas_produto

app = FastAPI(title = "Sistema de loja virtual", description = "Projeto da faculdade")

@app.get("/")
def teste():
    return {"mensagem" : "A API esta viva e rodando"}

app.include_router(rotas_produto)