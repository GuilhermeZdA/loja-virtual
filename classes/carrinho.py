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
        if isinstance(produto, (ProdutoDigital, ProdutoFisico)):
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
    def __init__(self, cliente: Cliente, itens: list):
        self.cliente = cliente
        self.itens = itens
        self.preco_total = None
        self.peso_total = None

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
        return self.__preco_total

    @property
    def peso_total(self):
        return self._peso_total
    
