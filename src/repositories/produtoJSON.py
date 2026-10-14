import json
from models.produto import Produto

class ProdutoJSON:

    def __init__(self, caminho):
        self.caminho = caminho


    @property
    def caminho(self):
        return self._caminho

    @caminho.setter
    def caminho(self, novo_caminho):
        self._caminho = novo_caminho


    def carregar_produtos(self) -> dict:
        with open(self.caminho, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

    def adicionar_produto(self, novo_produto: Produto) -> None:
        produtos = self.carregar_produtos()
        produtos.update(novo_produto.gerar_dict())

        with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii = False, indent = 4)

    def exibir_produtos(self) -> None:
        produtos = self.carregar_produtos()

        print("=" * 110)
        print(f'{"SKU":^9}{"NOME":^40}{"CATEGORIA":^15}{"PREÇO":^15}{"QUANTIDADE":^15}{"STATUS":^11}')
        print("=" * 110)

        for key, item in produtos.items():
            print(f'{key:^9}{item["nome"]:^40}{item["categoria"]:^15}{item["preco"]:^15}{item["qtd_estoque"]:^15}{item["status"]:^11}')
            print("-" * 110)

    def remover_produtos(self, produto: Produto) -> None:
        produtos = self.carregar_produtos()
        encontrado = False

        if produto.sku in produtos:
            del produtos[produto.sku]
            encontrado = True

        if encontrado:
            with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
                json.dump(produtos, arquivo, ensure_ascii = False, indent = 4)