from fastapi import FastAPI
from src.api.produto_route import router as rotas_produto
from src.api.cliente_route import router as rotas_cliente
from src.api.cupom_routes import router as rotas_cupom
from src.api.carrinho_route import router as rotas_carrinho
from src.api.pedido_route import router as rotas_pedido
from src.api.pagamento_routes import router as rotas_pagamento
from src.api.relatorio_route import router as rotas_relatorio

descricao = """**Bem-vindo a documentação oficial da Loja Virtual API!**
              \nEssa API dispoem das principais funcionalidades de uma comércio virtual como:
              \n - Cadastro de clientes, produtos, cupons.
              \n - Criação de um carrinho de compra e toda a lógica para efetuar o pedido de compra e pagamento.
              \n - Relatórios para analisar a evolução da loja."""


app = FastAPI(title = "Sistema de Loja Virtual", description = descricao, version = "1.0.0")

app.include_router(rotas_produto)
app.include_router(rotas_cliente)
app.include_router(rotas_cupom)
app.include_router(rotas_carrinho)
app.include_router(rotas_pedido)
app.include_router(rotas_pagamento)
app.include_router(rotas_relatorio)