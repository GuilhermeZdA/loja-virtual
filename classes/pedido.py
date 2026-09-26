class ItemPedido:
    """
    A representação dos produtos que seram comprados.

    Essa classe armazena os dados dos produtos da compra e impedem que possiveis mudanças nos preços do catálogo alterem dados de compras já efetuadas.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto e seus dados atuais no momento do pedido de compra.
        qtd (int): Armazena a quantidade de produtos no momento do pedido de compra.
        preco_unidade (float): O preço de uma unidade do produto no momento do pedido de compra.
    """
    pass


class Pedido:
    """
    A representação do pedido de compra.

    Essa classe é responsável por agrupar e organizar todos os dados da compra, gerenciar descontos de cupons e acréscimos do frete e controlar o estado do processo.

    Atributos:
        carrinho (Carrinho): O carrinho com os produtos do cliente.
        frete (float): O valor do frete para a entrega dos produtos (BRL).
        desconto (float): O valor do desconto do cupom (BRL).
        total (float): O preço total da compra após os acréscimos e desconotos.
        estado (str): A situação atual do pedido (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO).

    """
    pass


class Cupom:
    """
    A representação de um cupom de desconto.

    Essa classe representa cupons que podem ser utilizados antes do pagamento para diminuir o preço do produto. O cupom pode ter um desconto percentual (%) ou um desconto em valor fixo (BRL).

    Atributos:
        codigo (str): O código de identificação do cupom.
        tipo (str): O tipo de desconto do cupom (VALOR/PERCENTUAL).
        valor (float): A quantidade de desconto que o cupom fornece.
        validade (str): Data máxima até a inativação do cupom.
        qtd_usos (int): Quantidade de usos restantes até que o cupom se torne inativo. 
    """
    pass