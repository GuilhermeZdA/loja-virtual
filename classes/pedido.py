from produto import Produto, ProdutoFisico, ProdutoDigital
from carrinho import Carrinho
from frete import Frete
from pedido import Cupom
from pagamento import Pagamento
from caminhos import PEDIDOS, CUPOM
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
        return self.calcular_total()


    @property
    def estado(self):
        return self.altenar_estado()

    def buscar_cupom(self, codigo: str) -> float: # Vai utilizar o código para localizar o cupom no banco de dados
        pass

    def buscar_frete(self) -> float: # Vai calcular o frete caso haja produtos fisicos
        pass

    def calcular_total(self) -> float: # Vai calcular o valor total após descontos e aumentos
        pass

    def cancelar_pedido(self) -> None: # Vai apagar o pedido do banco de dados?
        pass

    def confirmar_pedido(self) -> Pagamento:
        pass
    
    def altenar_estado(self) -> str: # Vai analisar o que está acontecendo com o pedido e alternar seu estado
        pass

    def gerar_itempedido(self, carrinho: Carrinho) -> ItemPedido:
        pass

    # BANCO DE DADOS
    def gerar_id(self) -> str: #TESTAR
        caminho = PEDIDOS
        dados = self.carregar_pedidos(caminho)
        novo_id = 0

        if not dados: # JSON vazio
            novo_id = "1"
            return novo_id

        for ids in dados.keys():
            ids = int(ids)
            if ids - novo_id >= 2:
                novo_id += 1
                break
            if novo_id < ids:
                novo_id = ids

        return str(novo_id)

    @staticmethod
    def carregar_pedidos(caminho) -> dict:
        with open(caminho, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

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

    def adicionar_pedidos(self):
        caminho = PEDIDOS
        pedidos = self.carregar_pedidos(caminho)
        pedidos.update(self.gerar_dict())

        with open(caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(pedidos, arquivo, ensure_ascii = False , indent = 4)
        print("deu certo")


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


    @staticmethod
    def carregar_cupom(caminho) -> dict:
        with open(caminho, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

    def gerar_dict(self) -> dict:
        return {
            self.codigo : {
                "tipo" : self.tipo,
                "valor" : self.valor,
                "validade" : self.validade,
                "usos" : self.qtd_usos
            }
        }

    def adicionar_cupom(self) -> None:
        caminho = CUPOM
        cupons = self.carregar_cupom(caminho)
        cupons.update(self.gerar_dict())

        with open(caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)
        print("Deu certo")

    def exibir_cupom(self) -> None:
        caminho = CUPOM
        cupons = self.carregar_cupom(caminho)

        print("=" * 90)
        print(f'{"CÓDIGO":^10}{"TIPO":^10}{"VALOR":^15}{"VALIDADE":^20}{"QUANTIDADE DE USOS":^25}')
        print("=" * 90)

        for key, value in cupons.items():
            print(f'{key:^10}{value["tipo"]:^10}{value["valor"]:^15}{value["validade"]:^20}{value["usos"]:^25}')
            print("-" * 90)

    def remover_cupom(self) -> str:
        caminho = CUPOM
        cupons = self.carregar_cupom(caminho)
        encontrado = False

        if self.codigo in cupons:
            del cupons[self.codigo]
            encontrado = True

        if encontrado:
            with open(caminho, 'w', encoding = "utf-8") as arquivo:
                json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)
            return "dados apagados com sucesso"
        
        return "dados não encontrados"

    def atualizar_banco(self):
        caminho = CUPOM
        dados = self.carregar_cupom(caminho)
        dados.update(self.gerar_dict())

        with open(caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii = False, indent = 4)

        print("dados atualizados")