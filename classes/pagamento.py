class Pagamento:
    """
    A representação de um pagamento de compras.

    Essa classe recebe o pagamento do pedido de compra e gera uma nota fiscal para comprovar sua veracidade.

    Atributos:
        data (str): A data em que o pagamento da compra ocorreu.
        forma (str): O meios de pagamento (PIX, CREDITO, DEBITO, BOLETO).
        valor (float): O valor total da compra.
    """
    pass


class NotaFiscal:
    """
    A representação de uma nota fiscal da compra.

    Essa classe armazena dados da compra para registrar que a transação comercial ocorreu.

    Atributos:
        valor_pago (float): O valor total pago pelo cliente na compra.
        produtos (list<ItemCarrinho>): Os produtos que foram comprados.
        data (str): A data que ocorreu a compra.
    """
    pass