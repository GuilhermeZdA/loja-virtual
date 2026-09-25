class ItemCarrinho:
    """
    A representação de um produto dentro de um carrinho.

    Essa classe é responsável por armazenar quais produtos o cliente deseja e a quantidade deles.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto que o cliente vai guardar no carrinho.
        qtd (int): A quantidade de produtos que o cliente vai guardar no carrinho.
    """
    pass


class Carrinho:
    """
    A representação de um carrinho de compras.

    Essa classe é responsável por armazenar os items do carrinho e de qual cliente ele pertence.

    Atributos:
        cliente (Cliente): O dono do carrinho.
        itens (list<ItemCarrinho>): Produtos que o cliente escolheu.
        preco_total (float): Soma total do preço de todos os produtos do carrinho.
        peso_total (float): Soma total da massa de todos os produtos físicos do carrinho.
    """
    pass