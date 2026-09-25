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
    pass


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