import re


class Endereco:
    """
    A representação de um endereço de um cliente

    Essa classe representa um endereço com os dados do CEP, UF e cidade para localizar destino da entrega dos produtos.
    
    Atributos:
        cep (str): Conjunto númerico de 8 dígitos para identificar um local.
        uf (str): A Unidade Federativa que o cliente habita.
        cidade (str) O municipio que o cliente habita.
    """

    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

    def __init__(self, cep: str, uf: str, cidade: str):
        self.cep = cep
        self.uf = uf
        self.cidade = cidade


    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, valor):
        if isinstance(valor, str):
            padrao = r"^\d{8}$"
            if re.fullmatch(padrao, valor):
                self._cep = valor
            else:
                raise ValueError("Erro! O valor digitado não confere com o padrão CEP")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")


    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, unidade):
        if isinstance(unidade, str):
            unidade = unidade.strip().upper()
            if unidade in Endereco.estados:
                self._uf = unidade
            else:
                raise ValueError("Erro! O estado digitado é inexistente")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cid):
        if isinstance(cid, str):
            espaco = "  "
            if espaco in cid or len(cid) < 0:
                raise ValueError("Erro! Espaços vazios repetidos no nome da cidade!")
            else:
                self._cidade = cid
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")



class Frete:
    """
    A representação do frete de uma entrega.

    Essa classe representa o frete de uma entrega que causa um acréscimo no preço de compra dos produtos. Essa classe faz os cálculos do frete com base no dados recebidos.

    Atributos:
        endereco (Endereco): Os dados sobre onde os produtos serão entregues.
        peso_total (float): A soma das massas dos produtos físicos.
        valor (float): O preço do frete. 
    """
    def __init__(self, endereco: Endereco, peso_total: float):
        self.endereco = endereco
        self.peso_total = peso_total
        self.valor = 0


    @property # Atributo endereço
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, local: Endereco):
        if isinstance(local, Endereco):
            self.__endereco = local
        else:
            raise TypeError("Erro! O valor deve ser um objeto da classe Endereco")
