from pedido import Pedido

class Pagamento:
    """
    A representação de um pagamento de compras.

    Essa classe recebe o pagamento do pedido de compra e gera uma nota fiscal para comprovar sua veracidade.

    Atributos:
        data (str): A data em que o pagamento da compra ocorreu.
        forma (str): O meios de pagamento (PIX, CREDITO, DEBITO, BOLETO).
        valor (float): O valor total da compra.
    """
    def __init__(self, pedido: Pedido, data: str, forma: str, valor: float):
        self.pedido = pedido
        self.data = data
        self.forma = forma
        self.valor = valor


    @property
    def pedido(self):
        return self._pedido

    @pedido.setter
    def pedido(self, novo_pedido: Pedido):
        if isinstance(novo_pedido, Pedido):
            self._pedido = novo_pedido 
        else:
            raise TypeError("Erro! Só é aceito objetos da classe pedido")

    @property
    def data(self):
        return self._data


    @property
    def forma(self):
        return self._forma


    @property
    def valor(self):
        return self._valor


class NotaFiscal:
    """
    A representação de uma nota fiscal da compra.

    Essa classe armazena dados da compra para registrar que a transação comercial ocorreu.

    Atributos:
        valor_pago (float): O valor total pago pelo cliente na compra.
        produtos (list<ItemCarrinho>): Os produtos que foram comprados.
        data (str): A data que ocorreu a compra.
    """
    def __init__(self, pagamento : Pagamento, valor_pago: float, produtos: list, data: str):
        self.pagamento = pagamento
        self.valor_pago = valor_pago
        self.produtos = produtos
        self.data = data


    @property
    def pagamento(self):
        return self._pagamento

    @pagamento.setter
    def pagamento(self, novo_pag: Pagamento):
        if isinstance(novo_pag, Pagamento):
            self._pagamento = novo_pag
        else:
            raise TypeError("Erro! Só é aceito objetos da classe pagamento")


    @property
    def valor_pago(self):
        return self.pagamento.valor

    @property
    def data(self):
        return self._data