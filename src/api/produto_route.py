from fastapi import APIRouter, HTTPException
from src.schema import ProdutoDigitalCreate, ProdutoDigitalResponse, ProdutoFisicoCreate, ProdutoFisicoResponse, ProdutoUpdate
from src.models import ProdutoFisico, ProdutoDigital, Produto
from src.repositories import ProdutoJSON

router = APIRouter(prefix = "/produtos", tags = ["Produtos"])

@router.post("/fisico", status_code = 200, response_model = ProdutoFisicoResponse)
def criar_produto_fisico(dados: ProdutoFisicoCreate):
    
    if ProdutoJSON.produto_existe(dados.sku):
        raise HTTPException(status_code = 400, detail = "Erro! Já existe um produto com esse SKU")
    
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
        
    if ProdutoJSON.produto_existe(dados.sku):
        raise HTTPException(status_code = 400, detail = "Erro! Já existe um produto com esse SKU")
    
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


@router.patch("/produto/{sku}/{atributo}", status_code = 200)
def atualizar_dados(sku: str, atributo: str, dados: ProdutoUpdate):
    atributos_permitidos = ["nome", "preco"]

    atributo = atributo.strip().lower()
    sku = sku.strip().upper()

    if atributo not in atributos_permitidos:
        raise HTTPException(status_code = 400, detail = f"Erro! É possivel modificar apenas os atributos {atributos_permitidos}")

    if not ProdutoJSON.produto_existe(sku):
        raise HTTPException(status_code = 400, detail = f"Erro! Não existe produto cadastrado com o SKU {sku}")

    produtos_ativos = ProdutoJSON.carregar_produtos()

    if not produtos_ativos:
        raise HTTPException(status_code = 400, detail = "Erro! Não há produtos cadastrados")

    produto_atual = produtos_ativos[sku]

    if not produto_atual:
        raise HTTPException(status_code = 400, detail = f"Erro! Não existe produto com SKU {sku}")

    produto_atual[atributo] = dados.novo_valor
    produto_atual.pop("status", None)

    try:
        if produto_atual["tipo"] == "FISICO":
            produto_atual.pop("tipo", None)

            validador = ProdutoFisico(**produto_atual)

        elif produto_atual["tipo"] == "DIGITAL":
            produto_atual.pop("tipo", None)

            validador = ProdutoDigital(**produto_atual)

    except (ValueError, TypeError) as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

    ProdutoJSON.atualizar_produto(sku, atributo, dados.novo_valor)

    return {"message": f"{atributo} atualizado com sucesso!"}


@router.delete("/{sku}", status_code = 200)
def remover_produto(sku: str):

    sucesso = ProdutoJSON.remover_produtos(sku)

    if not sucesso:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")

    return {"message": f"Produto de {sku} removido com sucesso!"}