from fastapi import APIRouter, HTTPException, Body
from src.schema import ProdutoDigitalCreate, ProdutoDigitalResponse, ProdutoFisicoCreate, ProdutoFisicoResponse
from src.models import ProdutoFisico, ProdutoDigital
from src.repositories import ProdutoJSON

router = APIRouter(prefix = "/produtos", tags = ["Produtos"])

@router.post("/fisico", status_code = 200, response_model = ProdutoFisicoResponse)
def criar_produto_fisico(dados: ProdutoFisicoCreate):

    try:
        novo_produto = ProdutoFisico(
            sku = dados.sku,
            nome = dados.nome,
            categoria = dados.categoria,
            qtd_estoque = dados.qtd_estoque,
            preco = dados.preco,
            peso = dados.peso
        )

        ProdutoJSON.adicionar_produto(novo_produto)

        return novo_produto.gerar_dict()

    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))


@router.post("/digital", status_code = 200, response_model = ProdutoDigitalResponse)
def criar_produto_digital(dados: ProdutoDigitalCreate):

    try:
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

    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))
    

@router.get("/", status_code = 200, response_model = list[ProdutoDigitalResponse | ProdutoFisicoResponse])
def listar_produtos():
    
    produtos_salvos = ProdutoJSON.exibir_produtos()

    return produtos_salvos


@router.delete("/{sku}", status_code = 200)
def remover_produto(sku: str):

    sucesso = ProdutoJSON.remover_produtos(sku)

    if not sucesso:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")

    return {"message": f"Produto de {sku} removido com sucesso!"}