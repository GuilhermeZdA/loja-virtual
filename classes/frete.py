class Endereco:
    """
    A representação de um endereço de um cliente

    Essa classe representa um endereço com os dados do CEP, UF e cidade para localizar destino da entrega dos produtos.
    
    Atributos:
        cep (str): Conjunto númerico de 8 dígitos para identificar um local.
        uf (str): A Unidade Federativa que o cliente habita.
        cidade (str) O municipio que o cliente habita.
    """
    pass


class Frete:
    """
    A representação do frete de uma entrega.

    Essa classe representa o frete de uma entrega que causa um acréscimo no preço de compra dos produtos. Essa classe faz os cálculos do frete com base no dados recebidos.

    Atributos:
        endereco (Endereco): Os dados sobre onde os produtos serão entregues.
        peso_total (float): A soma das massas dos produtos físicos.
        valor (float): O preço do frete. 
    """
    pass