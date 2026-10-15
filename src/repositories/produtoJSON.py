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

    # @staticmethod
    # def exibir_produtos(self) -> None:
    #     with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
    #         produtos = json.load(arquivo)

    #     print("=" * 110)
    #     print(f'{"SKU":^9}{"NOME":^40}{"CATEGORIA":^15}{"PREÇO":^15}{"QUANTIDADE":^15}{"STATUS":^11}')
    #     print("=" * 110)

    #     for key, item in produtos.items():
    #         print(f'{key:^9}{item["nome"]:^40}{item["categoria"]:^15}{item["preco"]:^15}{item["qtd_estoque"]:^15}{item["status"]:^11}')
    #         print("-" * 110)

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
    def remover_produtos(produto: Produto) -> None:
        with open(PRODUTOS, 'r', encoding = "utf-8") as arquivo:
            produtos = json.load(arquivo)
        encontrado = False

        if produto.sku in produtos:
            del produtos[produto.sku]
            encontrado = True

        if encontrado:
            with open(PRODUTOS, 'w', encoding = "utf-8") as arquivo:
                json.dump(produtos, arquivo, ensure_ascii = False, indent = 4)