from datetime import datetime

class Pagamento:
    """
    A representação de um pagamento de compras.

    Essa classe recebe o pagamento do pedido de compra e gera uma nota fiscal para comprovar sua veracidade.

    Atributos:
        data (str): A data em que o pagamento da compra ocorreu.
        forma (str): O meios de pagamento (PIX, CREDITO, DEBITO, BOLETO).
        valor (float): O valor total da compra.
    """

    forma_pagamento = ["PIX", "CREDITO", "DEBITO", "BOLETO"]

    def __init__(self, forma_pag: str, valor_pago: float):
        self._data = datetime.now()
        self.forma_pag = forma_pag
        self.valor_pago = valor_pago


    @property
    def data(self):
        return self._data


    @property
    def forma_pag(self):
        return self._forma_pag

    @forma_pag.setter
    def forma_pag(self, nova_forma: str):
        if isinstance(nova_forma, str):
            if nova_forma in self.forma_pagamento:
                self._forma_pag = nova_forma
            else:
                raise ValueError("Erro! Forma de pagamento inexistente")
        else:
            raise TypeError("Erro! O valor deve ser um texto")


    @property
    def valor_pago(self):
        return self._valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor: float | int):
        if isinstance(novo_valor, (float, int)):
            novo_valor = float(novo_valor)
            if novo_valor >= 0:
                self._valor_pago = novo_valor 
            else:
                raise ValueError("Erro! O valor não pode ser negativo")
        else:
            raise TypeError("Erro! O valor deve ser um número")


    def gerar_dict(self):
        return {
            "data": self.data.strftime("%d-%m-%Y %H:%M:%S"),
            "forma_pag": self.forma_pag,
            "valor_pago": self.valor_pago
        }


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