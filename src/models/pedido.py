from .frete import Endereco
from .produto import ProdutoFisico, ProdutoDigital
from .frete import Frete
from random import randint
from datetime import datetime

class ItemPedido:
    """
    A representação dos produtos que seram comprados.

    Essa classe armazena os dados dos produtos da compra e impedem que possiveis mudanças nos preços do catálogo alterem dados de compras já efetuadas.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto e seus dados atuais no momento do pedido de compra.
        qtd (int): Armazena a quantidade de produtos no momento do pedido de compra.
        preco_unit (float): O preço de uma unidade do produto no momento do pedido de compra.
        subtotal_preco (float): O preço total desse(s) item(ns) no carrinho.
        subtotal_peso (float): O peso total desse(s) item(ns) no carrinho.
    """

    def __init__(self, item: ProdutoDigital | ProdutoFisico, qtd: int):
        self.item = item
        self.qtd = qtd
        self._preco_unit = float(item.preco)


    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, produto: ProdutoFisico | ProdutoDigital):
        if isinstance(produto, (ProdutoDigital, ProdutoFisico)): 
            self._item = produto
        else:
            raise TypeError("Erro! O valor deve ser um produto")


    @property
    def qtd(self):
        return self._qtd

    @qtd.setter
    def qtd(self, valor: int):
        if isinstance(valor, int):
            if valor > 0:
                self._qtd = valor
            else:
                raise ValueError("Erro! O valor digitado deve ser positivo")
        else:
            raise TypeError("Erro! O valor deve ser um número inteiro")


    @property
    def preco_unit(self):
        return self._preco_unit


    @property
    def subtotal_preco(self):
        return self.preco_unit * self.qtd


    @property
    def subtotal_peso(self):
        if isinstance(self.item, ProdutoFisico):
            return self.item.peso * self.qtd
        else:
            return 0

    def gerar_dict(self) -> dict:
        return {
            "sku": self.item.sku,
            "nome": self.item.nome,
            "qtd": self.qtd,
            "preco_unit": self.preco_unit,
            "subtotal_preco": self.subtotal_preco,
            "subtotal_peso": self.subtotal_peso
        }


class Pedido:
    """
    A representação do pedido de compra.

    Essa classe é responsável por agrupar e organizar todos os dados da compra, gerenciar descontos de cupons e acréscimos do frete e controlar o estado do processo.

    Atributos:
        id_ (str): O identificador individual de cada pedido
        carrinho (Carrinho): O carrinho com os produtos do cliente.
        frete (float): O valor do frete para a entrega dos produtos (BRL).
        desconto (float): O valor do desconto do cupom (BRL).
        total (float): O preço total da compra após os acréscimos e descontos.
        estado (str): A situação atual do pedido (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO).

    """
    lista_estados = ["CRIADO", "PAGO", "ENVIADO", "ENTREGUE", "CANCELADO"]


    def __init__(self, id_:str, cpf: str, endereco: Endereco, itens: list, frete: Frete, cupom: 'Cupom' = None):
        self._id_ = id_
        self._data = datetime.now()
        self._estado = "CRIADO"
        self._itens = itens
        self._forma_pag = None

        self.cpf = cpf
        self.endereco = endereco
        self.cupom = cupom
        self.frete = frete

        self._desconto = self.calcular_desconto()
        self._total = self.calcular_total()

    
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
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, local: Endereco):
        if isinstance(local, Endereco):
            self.__endereco = local
        else:
            raise TypeError("Erro! O valor deve ser um objeto da classe Endereco")


    @property
    def cupom(self):
        return self._cupom

    @cupom.setter
    def cupom(self, novo_cupom: 'Cupom'):
        if isinstance(novo_cupom, Cupom):
            self._cupom = novo_cupom
        elif novo_cupom == None:
            self._cupom = None
        else:
            raise TypeError("Erro! Deve receber um objeto cupom")


    @property
    def frete(self):
        return self._frete

    @frete.setter
    def frete(self, novo_frete: Frete):
        if isinstance(novo_frete, Frete):
            self._frete = novo_frete
        else:
            raise TypeError("Erro! Não é um objeto da classe frete")


    @property
    def desconto(self):
        return self._desconto


    @property
    def total(self):
        return self._total


    @property
    def estado(self):
        return self._estado


    @property
    def data(self):
        return self._data


    @property
    def itens(self):
        return self._itens


    @property
    def forma_pag(self):
        return self._forma_pag


    @property
    def preco_inicial(self):
        return self.calcular_preco()


    def calcular_preco(self) -> float:
        preco = 0
        for item_prod in self._itens:
            preco += item_prod.subtotal_preco
        return preco

    def calcular_desconto(self) -> float:
        if self.cupom == None:
            return 0

        if self.cupom.tipo == "$":
            if self.cupom.valor >= self.preco_inicial:
                raise ValueError("Erro! O valor do cupom deve ser menor que a soma dos preços dos produtos")
            else:
                return self.cupom.valor
            
        elif self.cupom.tipo == "%":
            if self.cupom.valor >= 100:
                raise ValueError("Erro! O desconto do cupom não pode zerar o preço das compras")
            else:
                return self.preco_inicial * (self.cupom.valor/100)


    def calcular_total(self) -> float:
        return self.preco_inicial - self.desconto + self.frete.calcular_frete()

    def gerar_dict(self) -> dict:
        return {
            "id_" : self.id_,
            "cpf" : self.cpf,
            "itens": [item.gerar_dict() for item in self.itens],
            "data": self.data.strftime("%d-%m-%Y %H:%M:%S"),
            "valor_frete" : self.frete.calcular_frete(),
            "desconto" : self.desconto,
            "total" : self.total,
            "estado" : self.estado,
            "endereco": self.endereco.gerar_dict(),
            "forma_pag": self.forma_pag
        }


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
        status (str): O estado do cupom (ATIVO/INATIVO) 
    """
    def __init__(self, codigo: str, tipo: str, valor: float, validade: str, qtd_usos: int):
        self.codigo = codigo
        self.tipo = tipo
        self.valor = valor
        self.validade = validade
        self.qtd_usos = qtd_usos


    @property # Atributo código_uso
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, cod: str):
        if isinstance(cod, str):
            espaco = " " 
            cod = cod.strip().upper()
            if espaco in cod or len(espaco) < 0: # Não pode ter espaços
                raise ValueError("Erro! O código não pode ter espaços em branco")
            else:
                self.__codigo = cod
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")
        

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        if isinstance(novo_tipo, str):
            if novo_tipo == "$":
                self._tipo = novo_tipo
            elif novo_tipo == "%":
                self._tipo = novo_tipo
            else:
                raise ValueError("Erro! Existem apenas os tipos '$' e '%'")
        else:
            raise TypeError("Erro! O valor deve ser um texto")


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if isinstance(novo_valor, (int, float)):
            novo_valor = float(novo_valor)
            if novo_valor > 0:
                if self.tipo == "$":
                    self._valor = novo_valor
                elif self.tipo == "%":
                    if novo_valor > 30:
                        self._valor = 30
                    else:
                        self._valor = novo_valor
                else:
                    raise ValueError("Erro! Tipo de valor indefinido")
            else:
                raise ValueError("Erro! O valor deve ser maior que 0")
        else:
            raise TypeError("Erro! O valor deve ser um número")


    @property
    def validade(self):
        return self._validade

    @validade.setter
    def validade(self, data):
        try:
            datetime.strptime(data, "%d-%m-%Y")

            self._validade = data

        except ValueError:
            raise ValueError("Erro! A data deve ser no formato DD/MM/YYYY")

    @property
    def qtd_usos(self):
        return self._qtd_usos

    @qtd_usos.setter
    def qtd_usos(self, valor):
        if isinstance(valor, int):
            if valor > 0:
                self._qtd_usos = valor
            else:
                self._qtd_usos = 0
        else:
            raise TypeError("Erro! O valor deve ser um número inteiro")


    @property
    def status(self):
        return self.analisar_status()


    def analisar_status(self) -> str:
        if self.qtd_usos > 0:

            data_validade = datetime.strptime(self.validade, "%d-%m-%Y").date()
            data_atual = datetime.now().date()

            if data_validade > data_atual:
                return "ATIVO"
        
        return "INATIVO"

    def gerar_dict(self) -> dict:
        return {
                "codigo": self.codigo,
                "tipo" : self.tipo,
                "valor" : self.valor,
                "validade" : self.validade,
                "qtd_usos" : self.qtd_usos,
                "status" : self.status
        }