from fastapi import APIRouter, HTTPException, Body
from typing import List
from src.schema.produto_schema import ProdutoCreate, ProdutoResponse
from src.models import ProdutoFisico, ProdutoDigital
from src.repositories import ProdutoJSON

router = APIRouter(prefix = "/produtos", tags = ["Produtos"]) # Produtos é o endpoint

@router.post("/", status_code = 201, response_model = ProdutoResponse)
def criar_produto(
    dados: ProdutoCreate = Body(
        ...,
        openapi_examples={
            "exemplo_fisico": {
                "summary": "Produto Físico",
                "value": {
                    "sku": "ABC1234",
                    "nome": "Teclado Mecânico",
                    "categoria": "ELETRONICO",
                    "qtd_estoque": 5,
                    "preco": 250.0,
                    "tipo": "FISICO",
                    "peso": 1.2
                }
            },
            "exemplo_digital": {
                "summary": "Produto Digital",
                "value": {
                    "sku": "AAA1111",
                    "nome": "Avast",
                    "categoria": "ELETRONICO",
                    "qtd_estoque": 20,
                    "preco": 80.0,
                    "tipo": "DIGITAL",
                    "codigo_uso": "ABCDE"
                }
            }
        }
    )
):
    try:
        if dados.tipo == "FISICO":       
            novo_produto = ProdutoFisico(
                sku = dados.sku,
                nome = dados.nome,
                categoria = dados.categoria,
                qtd_estoque = dados.qtd_estoque,
                preco = dados.preco,
                peso = dados.peso
            )

        elif dados.tipo == "DIGITAL":       
            novo_produto = ProdutoDigital(
                sku = dados.sku,
                nome = dados.nome,
                categoria = dados.categoria,
                qtd_estoque = dados.qtd_estoque,
                preco = dados.preco,
                codigo_uso = dados.codigo_uso
            )

        ProdutoJSON.adicionar_produto(novo_produto)

        return novo_produto.gerar_dict()

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