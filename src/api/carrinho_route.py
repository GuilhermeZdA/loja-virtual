from fastapi import APIRouter, HTTPException
from src.repositories import ProdutoJSON
from src.models import Carrinho, ProdutoDigital, ProdutoFisico
from src.schema.carrinho_schema import ItemCarrinhoCreate, CarrinhoResponse

router = APIRouter(prefix = "/carrinho", tags = ["Carrinho"])

carrinhos_ativos = {}


@router.post("/{cpf}/adicionar", status_code = 201, response_model = CarrinhoResponse)
def adicionar_item_ao_carrinho(cpf: str, dados: ItemCarrinhoCreate):
    if cpf not in carrinhos_ativos:
        novo_carrinho = Carrinho(cpf)
        carrinhos_ativos[cpf] = novo_carrinho

    carrinho = carrinhos_ativos[cpf]

    dict_produto = ProdutoJSON.buscar_produto(dados.sku)

    if dict_produto == None:
        raise HTTPException(status_code = 404, detail = "Dados do produto não encontrado")

    if dict_produto["tipo"] == "FISICO":
        produto = ProdutoFisico(
            sku = dict_produto["sku"],
            nome = dict_produto["nome"],
            categoria = dict_produto["categoria"],
            qtd_estoque = dict_produto["qtd_estoque"],
            preco = dict_produto["preco"],
            peso = dict_produto["peso"]
        )
    else:
        produto = ProdutoDigital(
            sku = dict_produto["sku"],
            nome = dict_produto["nome"],
            categoria = dict_produto["categoria"],
            qtd_estoque = dict_produto["qtd_estoque"],
            preco = dict_produto["preco"],
            codigo_uso = dict_produto["codigo_uso"]
        )

    carrinho.adicionar_item(produto, dados.qtd)

    return carrinho.gerar_dict()


@router.get("/{cpf}", status_code = 200, response_model = CarrinhoResponse)
def exibir_carrinho(cpf: str):

    if cpf in carrinhos_ativos:
        carrinho = carrinhos_ativos[cpf]
        return carrinho.gerar_dict()

    raise HTTPException(status_code = 404, detail = "Dados não encontrados")


@router.delete("/{cpf}/remover/{sku}", status_code = 200)
def remover_item(cpf: str, sku: str):
    if cpf in carrinhos_ativos:
        carrinho_atual = carrinhos_ativos[cpf]

        carrinho_atual.remover_item(sku)        

        return {"message" : f"Produto de SKU {sku} removido com sucesso de carrinho de CPF {cpf}"}
    
    else:
        raise HTTPException(status_code = 404, detail = "Não existe carrinho ativo com esse CPF")


@router.delete("/{cpf}", status_code = 200)
def cancelar_carrinho(cpf: str):

    if cpf in carrinhos_ativos:
        del carrinhos_ativos[cpf]
        return {"message" : f"O carrinho de CPF {cpf} foi removido com sucesso"}

    raise HTTPException(status_code = 404, detail = "Não existe carrinho ativo com esse CPF")