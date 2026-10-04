from classes.frete import Endereco

class Cliente:
    """
    A representação de um cliente da loja.

    Essa classe armazena todos os dados pessoais do cliente.

    Atributos:
        id (str): Número de identificação do cliente.
        nome (str): Nome do cliente.
        email (str): Email do cliente.
        cpf (str): CPF do cliente.
        endereco (Endereco): Dados do endereço do cliente (CEP, UF, Cidade).
    """
    def __init__(self, id: str, nome: str, email: str, cpf: str, endereco: Endereco):
        pass
