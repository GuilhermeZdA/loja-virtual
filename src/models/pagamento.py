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
    nota_estados = ["EMITIDO", "CANCELADO"]

    def __init__(self, codigo_nota: str, id_pedido: str, cpf: str, valor_pago: str, produtos: list):
        self.codigo_nota = codigo_nota
        self.id_pedido = id_pedido
        self.cpf = cpf
        self.valor_pago = valor_pago
        self.produtos = produtos

        self._data_emissao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.estado = "EMITIDO"


    @property
    def codigo_nota(self):
        return self._codigo_nota

    @codigo_nota.setter
    def codigo_nota(self, novo_codigo: int):
        if isinstance(novo_codigo, int):
            self._codigo_nota = novo_codigo
        else:
            raise TypeError("Erro! O valor deve ser um número inteiro")


    @property
    def id_(self):
        return self._id_

    @id_.setter
    def id_(self, novo_id: str):
        if isinstance(novo_id, str):
            if len(novo_id) == 5:
                self._id_ = novo_id
            else:
                raise ValueError("Erro! O ID deve ser composto por 5 caracteres")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str):
            self._cpf = novo_cpf
        else:
            raise TypeError("Erro! CPF inválido ou inexistente")


    @property
    def valor_pago(self):
        return self._valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor: float | int):
        if isinstance(novo_valor, (int, float)):
            novo_valor = float(novo_valor)
            if novo_valor >= 0:
                self._valor_pago = novo_valor
            else:
                raise ValueError("Erro! O valor pago não pode ser negativo")
        else:
            raise TypeError("Erro! O valor deve ser um número")


    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, nova_lista: list):
        if isinstance(nova_lista, list):
            self._produtos = nova_lista
        else:
            raise TypeError("Erro! O valor tem que ser uma lista")


    @property
    def data_emissao(self):
        return self._data_emissao


    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, novo_estado: str):
        if isinstance(novo_estado, str):
            if novo_estado in self.nota_estados:
                self._estado = novo_estado
            else:
                raise ValueError("Erro! Não existe esse tipo de estado")
        else:
            raise TypeError("Erro! O valor deve ser um texto")


    def gerar_dict(self):
        return {
                "codigo_nota" : self.codigo_nota,
                "id_pedido": self.id_pedido,
                "cpf" : self.cpf,
                "valor_pago": self.valor_pago,
                "produtos": self.produtos,
                "estado": self.estado
            }
        