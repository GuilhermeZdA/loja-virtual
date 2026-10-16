import json
from src.models.produto import Produto
from src.caminhos import PRODUTOS

class ProdutoJSON:

    @staticmethod
    def adicionar_produto(novo_produto: Produto) -> None:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)
            
        produtos.update(novo_produto.gerar_dict())

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