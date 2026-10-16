from .produto import Produto, ProdutoFisico, ProdutoDigital
from .carrinho import Carrinho
from random import randint
import json

class ItemPedido:
    """
    A representação dos produtos que seram comprados.

    Essa classe armazena os dados dos produtos da compra e impedem que possiveis mudanças nos preços do catálogo alterem dados de compras já efetuadas.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto e seus dados atuais no momento do pedido de compra.
        qtd (int): Armazena a quantidade de produtos no momento do pedido de compra.
        preco_unidade (float): O preço de uma unidade do produto no momento do pedido de compra.
    """
    def __init__(self, item: ProdutoDigital | ProdutoFisico, qtd: int, preco_unidade: float):
        self._item = item
        self._qtd = qtd
        self._preco_unidade = preco_unidade

    @property
    def item(self):
        return self._item


    @property
    def qtd(self):
        return self._qtd


    @property
    def preco_unidade(self):
        return self._preco_unidade


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


    def __init__(self, carrinho: Carrinho):
        self.carrinho = carrinho
        self._id_ = self.gerar_id() #TESTAR
        self.frete = 0
        self.desconto = 0
        self.total = 0
        self.estado = ""

    @property
    def carrinho(self):
        return self._carrinho

    @carrinho.setter
    def carrinho(self, novo_carrinho: Carrinho):
        if isinstance(novo_carrinho, Carrinho):
            self._carrinho = novo_carrinho
        else:
            raise TypeError("Erro! Só é aceito objetos da classe carrinho")

    @property
    def id_(self):
        return self._id_

    # MUDAR O RACIOCINIO DO FRETE E DESCONTO
    @property
    def frete(self):
        return self._frete

    @frete.setter
    def frete(self, novo_frete: float):
        if isinstance(novo_frete, float):
            self._frete = novo_frete # Preciso entender mais disso aqui
        else:
            raise TypeError("Erro! Só é aceito objetos da classe frete")


    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, novo_desc: float):
        if isinstance(novo_desc, float):
            self._desconto = novo_desc # Preciso entender mais disso aqui
        else:
            raise TypeError("Erro! Só é aceito objetos da classe cupom")


    @property
    def total(self):
        return self.calcular_total()


    @property
    def estado(self):
        return self.altenar_estado()


    def usar_cupom(self, cod: str): # PRECISO DO CALCULAR TOTAL
        pass

    def buscar_frete(self) -> float: # Vai calcular o frete caso haja produtos fisicos
        pass

    def calcular_total(self) -> float: # Vai calcular o valor total após descontos e aumentos
        pass

    def cancelar_pedido(self) -> None: # Vai apagar o pedido do banco de dados?
        pass

    def confirmar_pedido(self):
        pass
    
    def altenar_estado(self) -> str: # Vai analisar o que está acontecendo com o pedido e alternar seu estado
        pass

    def gerar_itempedido(self, carrinho: Carrinho) -> ItemPedido:
        pass

    def gerar_dict(self) -> dict:
        return {
            self.id_ : {
                "carrinho" : {},
                "frete" : self.frete,
                "desconto" : self.desconto,
                "total" : self.total,
                "estado" : self.estado
            }
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
        if isinstance(data, str):
            self._validade = data
        else:
            raise TypeError("Erro! O valor deve ser um texto")


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


    def gerar_dict(self) -> dict:
        return {
            self.codigo : {
                "tipo" : self.tipo,
                "valor" : self.valor,
                "validade" : self.validade,
                "usos" : self.qtd_usos
            }
        }