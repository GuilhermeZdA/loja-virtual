from cliente import Cliente
from produto import Produto, ProdutoDigital, ProdutoFisico

class ItemCarrinho:
    """
    A representação de um produto dentro de um carrinho.

    Essa classe é responsável por armazenar quais produtos o cliente deseja e a quantidade deles.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto que o cliente vai guardar no carrinho.
        qtd (int): A quantidade de produtos que o cliente vai guardar no carrinho.
    """
    def __init__(self, item: ProdutoFisico | ProdutoDigital, qtd: int):
        self.item = item
        self.qtd = qtd

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, produto: ProdutoFisico | ProdutoDigital):
        if isinstance(produto, (ProdutoDigital, ProdutoFisico)): # Depois fazer a validação com o banco de dados
            self._item = produto
        else:
            raise TypeError("Erro! O valor deve ser um produto")
        

    @property
    def qtd(self):
        return self._qtd

    @item.setter
    def qtd(self, valor: int):
        if isinstance(valor, int):
            if valor > 0:
                self._qtd = valor
            else:
                raise ValueError("Erro! O valor digitado deve ser positivo")
        else:
            raise TypeError("Erro! O valor deve ser um número inteiro")


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
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self._itens: list[ItemCarrinho] = [] # Type hint para a vscode entender que a lista só manipulara ItemCarrinho
        self.preco_total = 0
        self.peso_total = 0

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, novo_cliente):
        if isinstance(novo_cliente, Cliente):
            self.__cliente = novo_cliente
        else:
            raise TypeError("Erro! Cliente inválido ou inexistente")


    @property
    def itens(self):
        return self._itens


    @property
    def preco_total(self):
        return self.calcular_preco()


    @property
    def peso_total(self):
        return self.calcular_peso()


    def adicionar_item(self, item: ItemCarrinho) -> None:
        if isinstance(item, ItemCarrinho):
            if item in self._itens:
                posicao = self._itens.index(item)
                self._itens[posicao].qtd += item.qtd # Teoricamente soma a quantidade a mais de items que eu coloquei
            else:
                self._itens.append(item)
        else:
            raise TypeError("Erro! O valor digitado deve ser um item de carrinho")

    def remover_item(self, item: ItemCarrinho) -> None: # Não tenho certeza se devo usar ItemCarrinho ou Produto
        if isinstance(item, ItemCarrinho):
            posicao = self._itens.index(item)
            if item in self._itens:
                if self._itens[posicao].qtd - item.qtd <= 0: # Analisa se após a remoção de uma quantidade de itens, o valor continua positivo
                    self._itens.remove(item)
                else:
                    self._itens[posicao] -= item.qtd
            else:
                raise ValueError("Erro! Item não encontrado")
        else:
            raise TypeError("Erro! O valor digitado deve ser um item de carrinho")

    def calcular_preco(self) -> float:
        preco = 0
        for produto in self._itens:
            preco += produto.item.preco * produto.qtd
        return preco

    def calcular_peso(self) -> float:
        peso = 0
        for produto in self._itens:
            if isinstance(produto.item, ProdutoFisico):
                peso += produto.item.peso
        return peso