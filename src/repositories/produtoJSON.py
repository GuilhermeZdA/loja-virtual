import json
from src.models.produto import Produto
from src.caminhos import PRODUTOS

class ProdutoJSON:

    @staticmethod
    def adicionar_produto(novo_produto: Produto) -> None:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)
            
        produtos[novo_produto.sku] = novo_produto.gerar_dict()

        with open(PRODUTOS, 'w', encoding = "utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii = False, indent = 4)


    @staticmethod
    def exibir_produtos() -> list:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)

        lista_produtos = []

        if isinstance(produtos, dict):
            for sku, dados in produtos.items():
                if isinstance(dados, dict):
                    item = dados.copy()
                    item["sku"] = sku  
                    lista_produtos.append(item)

        elif isinstance(produtos, list):
            lista_produtos = produtos

        return lista_produtos

    @staticmethod
    def buscar_produto(sku: str) -> dict:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)
        return produtos.get(sku)

    @staticmethod
    def remover_produtos(sku: str) -> bool:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)
        encontrado = False

        if sku in produtos:
            del produtos[sku]
            encontrado = True

        if encontrado:
            with open(PRODUTOS, 'w', encoding = "utf-8") as arquivo:
                json.dump(produtos, arquivo, ensure_ascii = False, indent = 4)

        return encontrado

    @staticmethod
    def retirar_estoque(itens_pedido: list):
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            estoque = json.load(arquivo)

        for prod in itens_pedido:
            sku = prod.item.sku
            qtd = prod.qtd

            if sku in estoque:
                nova_qtd = estoque[sku]["qtd_estoque"] - qtd
                estoque[sku]["qtd_estoque"] = nova_qtd

            if nova_qtd <= 0:
                estoque[sku]["qtd_estoque"] = 0
                estoque[sku]["status"] = "INATIVO"

        with open(PRODUTOS, 'w', encoding = "utf-8") as arquivo:
            json.dump(estoque, arquivo, ensure_ascii = False, indent = 4)

    @staticmethod
    def devolver_estoque(itens_pedido: list):
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            estoque = json.load(arquivo)

        for prod in itens_pedido:
            sku = prod["sku"]
            qtd = prod["qtd"]

            if sku in estoque:
                estoque[sku]["qtd_estoque"] += qtd

        with open(PRODUTOS, 'w', encoding = "utf-8") as arquivo:
            json.dump(estoque, arquivo, ensure_ascii = False, indent = 4)