import re
from src.repositories import FreteJSON

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

    # Atributo CEP
    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, valor: str):
        if isinstance(valor, str):
            padrao = r"^\d{8}$"
            if re.fullmatch(padrao, valor):
                self._cep = valor
            else:
                raise ValueError("Erro! O valor digitado não confere com o padrão CEP")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")

    # Atributo UF
    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, unidade: str):
        if isinstance(unidade, str):
            unidade = unidade.strip().upper()
            if unidade in Endereco.estados:
                self._uf = unidade
            else:
                raise ValueError("Erro! O estado digitado é inexistente")
        else:
            raise TypeError("Erro! O valor digitado deve ser um texto")

    # Atributo Cidade
    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cid: str):
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
    """
    def __init__(self, uf: str, peso_total):
        self.uf = uf
        self.peso_total = peso_total


    @property 
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, nova_uf: str):
        if isinstance(nova_uf, str):
            nova_uf = nova_uf.upper().strip()
            espaco = " "
            if len(nova_uf) != 2 or espaco in nova_uf:
                raise ValueError("Erro! Formato incorreto de UF (xx)")
            self._uf = nova_uf
        else:
            raise TypeError("Erro! O valor deve ser um texto")


    @property
    def peso_total(self):
        return self._peso_total

    @peso_total.setter
    def peso_total(self, novo_peso: float | int):
        if isinstance(self.peso_total, (float ,int)):
            if novo_peso >= 0:
                self._peso_total = novo_peso
            else:
                raise ValueError("Erro! O peso não pode ser negativo")
        else:
            raise TypeError("Erro! O peso deve ser um número")


    def calcular_frete(self) -> float: 
        if self.peso_total == 0:
            return 0

        multiplicador = FreteJSON.buscar_multiplicador(self.uf)
        taxa_kg = FreteJSON.taxa_fixa()

        valor_frete = self.peso_total * taxa_kg * multiplicador

        return valor_frete