from .produto import Produto, ProdutoDigital, ProdutoFisico

class ItemCarrinho:
    """
    A representação de um produto dentro de um carrinho.

    Essa classe é responsável por armazenar quais produtos o cliente deseja e a quantidade deles.

    Atributos:
        item (ProdutoFisico/ProdutoDigital): O produto que o cliente vai guardar no carrinho.
        qtd (int): A quantidade de produtos que o cliente vai guardar no carrinho.
        subtotal_preco (float): O preço total desse(s) item(ns) no carrinho.
        subtotal_peso (float): O peso total desse(s) item(ns) no carrinho.
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
    def subtotal_preco(self):
        return self.item.preco * self.qtd


    @property
    def subtotal_peso(self):
        if isinstance(self.item, ProdutoFisico):
            return self.item.peso * self.qtd
        else:
            return 0
        
    def gerar_dict(self):
        return {
            "sku": self.item.sku,
            "nome": self.item.nome,
            "qtd": self.qtd,
            "subtotal_preco": self.subtotal_preco,
            "subtotal_peso": self.subtotal_peso
        }
    

class Carrinho:
    """
    A representação de um carrinho de compras.

    Essa classe é responsável por armazenar os items do carrinho e de qual cliente ele pertence.

    Atributos:
        cpf (str): O código de identificação do dono do carrinho.
        itens (list<ItemCarrinho>): Produtos que o cliente escolheu.
        preco_total (float): Soma total do preço de todos os produtos do carrinho.
        peso_total (float): Soma total da massa de todos os produtos físicos do carrinho.
    """
    def __init__(self, cpf: str):
        self.cpf = cpf
        self._itens: list[ItemCarrinho] = [] # Type hint para a vscode entender que a lista só manipulara ItemCarrinho


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
    def itens(self):
        return self._itens


    @property
    def preco_total(self):
        return self.calcular_preco()


    @property
    def peso_total(self):
        return self.calcular_peso()

 
    def adicionar_item(self, produto: Produto, qtd: int) -> None:
        if qtd > produto.qtd_estoque:
            qtd = produto.qtd_estoque

        for item_existente in self._itens:
            if produto.sku == item_existente.item.sku:
                nova_qtd = qtd + item_existente.qtd

                if nova_qtd > produto.qtd_estoque:
                    nova_qtd = produto.qtd_estoque
                else:
                    item_existente.qtd = nova_qtd
                return

        novo_item = ItemCarrinho(item = produto, qtd = qtd)
        self._itens.append(novo_item)

    def remover_item(self, sku: str):
        for prod_atual in self.itens:
            if prod_atual.item.sku == sku:
                self.itens.remove(prod_atual)
                return

        raise ValueError(f"Não existe produto com SKU {sku} nesse carrinho")


    def calcular_preco(self) -> float:
        preco = 0
        for produto in self._itens:
            preco += produto.subtotal_preco
        return preco

    def calcular_peso(self) -> float:
        peso = 0
        for produto in self._itens:
            peso += produto.subtotal_peso
        return peso

    def gerar_dict(self):
        return {
            "cpf": self.cpf,
            "itens": [item.gerar_dict() for item in self.itens],
            "preco_total": self.preco_total,
            "peso_total": self.peso_total
        }