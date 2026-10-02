import re

class Produto:
    """
    A representação de um produto genérico dentro do catálogo da loja.

    Esta classe é uma superclasse para produtos mais especificos (ProdutoDigital e ProdutoFisico).

    Atributos:
        sku (str): Código que identifica o produto.
        nome (str): Nome do produto.
        categoria (str): Representa qual é o tipo do produto(Vestuário, Eletrônicos, etc).
        preco (float): Preço do produto em real (BRL).
        qtd_estoque (int): Quantidade de produtos disponiveis no estoque.
        status (string): Informa a disponibilidade do produto para venda (ATIVO/INATIVO).
    """
    def __init__(self, sku: str, nome: str, categoria: str, preco: float):
        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, valor: str):
        padrao =  r"^[A-Z]{3}-\d{3,5}$"
        if isinstance(valor, str):
            if re.match(padrao, valor):
                self._sku = valor
            else:
                raise ValueError("Erro! Padrão incorreto de SKU")
        else:
            raise TypeError("Erro! O valor digitado deve ser uma string")
    


class ProdutoDigital(Produto):
    """
    A representação de um produto digital dentro do catálogo da loja.

    Esta classe é uma subclasse de Pessoa e apresenta a caracteristica única do código de uso, que libera o acesso para seu uso para o cliente.

    Atributos:
        codigo_uso (str): Código que libera o uso do produto.
    """
    pass


class ProdutoFisico(Produto):
    """
    A representação de um produto físico dentro do catálogo da loja.

    Esta classe é uma subclasse de Pessoa e apresenta a caracteristica única do peso, que é utilizado no cálculo do frete.

    Atributos:
        peso (float): massa do produto em kg.
    """
    pass