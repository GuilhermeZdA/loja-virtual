from fastapi import APIRouter, HTTPException
from typing import List
from src.schema.produto_schema import ProdutoCreate, ProdutoResponse
from src.models import Produto
from src.repositories import ProdutoJSON

router = APIRouter(prefix = "/produtos", tags = ["Produtos"])

@router.post("/", status_code = 201, response_model = ProdutoResponse)
def criar_produto(dados: ProdutoCreate):
    try:
        novo_produto = Produto(
            sku = dados.sku,
            nome = dados.nome,
            categoria = dados.categoria,
            qtd_estoque = dados.qtd_estoque,
            preco = dados.preco
        )

        ProdutoJSON.adicionar_produto(novo_produto)

        return novo_produto

    except ValueError as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

@router.get("/", response_model = List[ProdutoResponse])
def listar_produtos():
    
    produtos_salvos = ProdutoJSON.exibir_produtos()

    return produtos_salvos

@router.delete("/{sku}")
def remover_produto(sku: str):

    sucesso = ProdutoJSON.remover_produtos(sku)

    if not sucesso:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")

    return {"mensagem": f"Produto {sku} removido com sucesso!"}