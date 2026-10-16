import re

class Produto:
    """
    A representação de um produto genérico dentro do catálogo da loja.

    Esta classe é uma superclasse para produtos mais especificos (ProdutoDigital e ProdutoFisico).

    Atributos:
        sku (str): Código que identifica o produto.
        nome (str): Nome do produto.
        categoria (str): Representa qual é o tipo do produto(Vestuário, Eletrônicos, etc).
        preco (float): Preço do produto em real (BRL).
        qtd_estoque (int): Quantidade de produtos disponiveis no estoque.
        status (string): Informa a disponibilidade do produto para venda (ATIVO/INATIVO).
    """
    categorias = ["ELETRONICO", "VESTUARIO", "DECORACAO", "ALIMENTO", "HIGIENE"]

    def __init__(self,
                sku: str,
                nome: str,
                categoria: str,
                qtd_estoque: str,
                preco: float):
        
        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self.qtd_estoque = qtd_estoque
        self.preco = preco


    @property # Atributo SKU
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, valor: str):
        padrao =  r"^[A-Z]{3}\d{3,5}$" # Padrão: até 3 letras e entre 3 a 5 dígitos
        if isinstance(valor, str) and len(valor) > 0:
            if re.match(padrao, valor):
                self._sku = valor
            else:
                raise ValueError("Erro! Padrão incorreto de SKU")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    @property # Atributo nome
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            novo_nome = novo_nome.strip() # Retirar os espaços sobrando
            espaco = "  " # Evitar espaços repetidos
            if not espaco in novo_nome and len(novo_nome) > 0:
                self._nome = novo_nome
            else:
                raise ValueError("Erro! Espaços vazios repetidos no nome do produto!")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    @property # Atributo categoria
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categ: str):
        if isinstance(categ, str) and len(categ) > 0:
            categ = categ.strip().upper()
            if categ in Produto.categorias: # Analisa se a categoria existe
                self._categoria = categ
            else:
                raise ValueError("Erro! Categoria inexistente")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    @property # Atributo qtd_estoque
    def qtd_estoque(self):
        return self._qtd_estoque

    @qtd_estoque.setter
    def qtd_estoque(self, valor: int):
        if isinstance(valor, int):
            if valor >= 0:
                self._qtd_estoque = valor
            else:
                self._qtd_estoque = 0
        else:
            raise TypeError("Erro! O valor deve ser um número inteiro")


    @property # Atributo preço
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor: float):
        if isinstance(valor, (int, float)):
            valor = float(valor)
            if valor > 0: # Analisa se o valor do preço é positivo
                self._preco = valor
            else:
                raise TypeError("Erro! O preço do produto deve ser positivo")
        else:
            raise ValueError("Erro! O valor digitado deve ser um inteiro ou um número de ponto flutuante")


    @property # Atributo status
    def status(self):
        return self.analisar_status()


    def analisar_status(self) -> str:
        if self.qtd_estoque > 0:
            return "ATIVO"
        elif self.qtd_estoque == 0:
            return "INATIVO"

    def __iadd__(self, valor: int):
        if isinstance(valor, int):
            self.qtd_estoque += valor
            return self
        else:
            return NotImplemented

    def __isub__(self, valor: int):
        if isinstance(valor, int):
            self.qtd_estoque -= valor
            return self
        else:
            return NotImplemented

    def gerar_dict(self) -> dict:
        return {
            "sku" : self.sku,
            "nome" : self.nome,
            "categoria" : self.categoria,
            "qtd_estoque" : self.qtd_estoque,
            "preco" : self.preco,
            "status" : self.status
        }

class ProdutoDigital(Produto):
    """
    A representação de um produto digital dentro do catálogo da loja.

    Esta classe é uma subclasse de Pessoa e apresenta a caracteristica única do código de uso, que libera o acesso para seu uso para o cliente.

    Atributos:
        codigo_uso (str): Código que libera o uso do produto.
    """

    def __init__(self, sku, nome, categoria, qtd_estoque, preco, codigo_uso):
        super().__init__(sku, nome, categoria, qtd_estoque, preco)
        self.codigo_uso = codigo_uso


    @property # Atributo código_uso
    def codigo_uso(self):
        return self.__codigo_uso

    @codigo_uso.setter
    def codigo_uso(self, cod: str):
        if isinstance(cod, str):
            espaco = " "
            cod = cod.strip().upper()
            if espaco in cod or len(espaco) < 0:
                raise ValueError("Erro! O código não pode ter espaços em branco")
            else:
                self.__codigo_uso = cod
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    def gerar_dict(self) -> dict:
        dicionario = super().gerar_dict()
        dicionario["tipo"] = "DIGITAL"
        dicionario["codigo_uso"] = self.codigo_uso

        return dicionario

class ProdutoFisico(Produto):
    """
    A representação de um produto físico dentro do catálogo da loja.

    Esta classe é uma subclasse de Pessoa e apresenta a caracteristica única do peso, que é utilizado no cálculo do frete.

    Atributos:
        peso (float): massa do produto em kg.
    """
    def __init__(self, sku, nome, categoria, qtd_estoque, preco, peso):
        super().__init__(sku, nome, categoria, qtd_estoque, preco)
        self.peso = peso


    @property # Atributo peso
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor: float):
        if isinstance(valor, (int, float)):
            valor = float(valor)
            if valor > 0: # Analisa se o valor do peso é positivo
                self._peso = valor
            else:
                raise TypeError("Erro! O peso do produto deve ser positivo")
        else:
            raise ValueError("Erro! O valor digitado deve ser um inteiro ou um número de ponto flutuante")


    def gerar_dict(self) -> dict:
        dicionario = super().gerar_dict()
        dicionario["tipo"] = "FISICO"
        dicionario["peso"] = self.peso

        return dicionario