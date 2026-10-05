from produto import Produto, ProdutoFisico, ProdutoDigital
from carrinho import Carrinho
from frete import Frete
from pedido import Cupom

class ItemPedido:
    """
    A representação dos produtos que seram comprados.

    Essa classe armazena os dados dos produtos da compra e impedem que possiveis mudanças nos preços do catálogo alterem dados de compras já efetuadas.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto e seus dados atuais no momento do pedido de compra.
        qtd (int): Armazena a quantidade de produtos no momento do pedido de compra.
        preco_unidade (float): O preço de uma unidade do produto no momento do pedido de compra.
    """
    def __init__(self):
        self.item = self.item
        self.qtd = self.qtd
        self.preco_unidade = self.preco_unidade


class Pedido:
    """
    A representação do pedido de compra.

    Essa classe é responsável por agrupar e organizar todos os dados da compra, gerenciar descontos de cupons e acréscimos do frete e controlar o estado do processo.

    Atributos:
        carrinho (Carrinho): O carrinho com os produtos do cliente.
        frete (float): O valor do frete para a entrega dos produtos (BRL).
        desconto (float): O valor do desconto do cupom (BRL).
        total (float): O preço total da compra após os acréscimos e descontos.
        estado (str): A situação atual do pedido (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO).

    """
    def __init__(self, carrinho: Carrinho):
        self.carrinho = carrinho
        self.frete = None
        self.desconto = None
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
    def frete(self):
        return self._frete

    @frete.setter
    def frete(self, novo_frete: Frete):
        if isinstance(novo_frete, Frete):
            self._frete = novo_frete # Preciso entender mais disso aqui
        else:
            raise TypeError("Erro! Só é aceito objetos da classe frete")


    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, novo_desc: Cupom):
        if isinstance(novo_desc, Cupom):
            self._desconto = novo_desc # Preciso entender mais disso aqui
        else:
            raise TypeError("Erro! Só é aceito objetos da classe cupom")


    @property
    def total(self):
        return self._total


    @property
    def estado(self):
        return self._estado

    def buscar_cupom(self, codigo: str) -> float: # Vai utilizar o código para localizar o cupom no banco de dados
        pass

    def buscar_frete(self) -> float: # Vai calcular o frete caso haja produtos fisicos
        pass

    def calcular_total(self) -> float: # Vai calcular o valor total após descontos e aumentos
        pass

    def cancelar_pedido(self) -> None: # Vai apagar o pedido do banco de dados?
        pass

    def altenar_estado(self) -> None: # Vai analisar o que está acontecendo com o pedido e alternar seu estado
        pass

    def gerar_itempedido(self, carrinho: Carrinho) -> ItemPedido:
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
        
    # Os atributos depois de definidos devem ser imutaveis

    @property
    def tipo(self):
        return self._tipo


    @property
    def valor(self):
        return self._valor


    @property
    def validade(self):
        return self._validade

    @property
    def qtd_usos(self):
        return self._qtd_usos