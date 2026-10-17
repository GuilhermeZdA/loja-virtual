from fastapi import FastAPI
from src.api.produto_route import router as rotas_produto
from src.api.cliente_route import router as rotas_cliente
from src.api.cupom_routes import router as rotas_cupom

app = FastAPI(title = "Sistema de loja virtual", description = "Projeto da faculdade")

@app.get("/", tags = ["Geral"])
def teste():
    return {"mensagem" : "A API esta viva e rodando"}

app.include_router(rotas_produto)
app.include_router(rotas_cliente)
app.include_router(rotas_cupom)