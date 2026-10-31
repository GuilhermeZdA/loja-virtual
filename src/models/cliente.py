from .frete import Endereco

class Cliente:
    """
    A representação de um cliente da loja.

    Essa classe armazena todos os dados pessoais do cliente.

    Atributos:
        nome (str): Nome do cliente.
        email (str): Email do cliente.
        cpf (str): CPF do cliente.
        endereco (Endereco): Dados do endereço do cliente (CEP, UF, Cidade).
    """
    def __init__(self, nome: str, email: str, cpf: str, endereco: Endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.endereco = endereco

    @property
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
                raise ValueError("Erro! Há muitos espaços vazios entre seu nome")
        else:
            raise TypeError("Erro! O tipo requisitado é str")


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email: str):
        if isinstance(novo_email, str):
            if "@" in novo_email: # Impede emails sem '@'
                self._email = novo_email
            else:
                raise ValueError("O email digitado deve conter '@'")
        else:
            raise TypeError("Erro! Erro! O tipo requisitado é str")


    @property 
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor: str):
        if isinstance(valor, str):
            if self.validar_cpf(valor):
                self.__cpf = valor
            else:
                raise ValueError("Erro! Padrão de CPF impossível de existir")
        else:
            raise TypeError("Erro! Erro! O tipo requisitado é str")


    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, local: Endereco):
        if isinstance(local, Endereco): 
            self.__endereco = local
        else:
            raise TypeError("Erro! Erro! O tipo requisitado é Endereco")

    @staticmethod
    def validar_cpf(cpf: str) -> bool:

        cpf = "".join(filter(str.isdigit, cpf)) # Permite caracteres entre os números do cpf

        if not cpf or len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        decimo_digito = sum(int(x) * y for x, y in zip(cpf[:9], range(10, 1, -1)))
        decimo_digito = 0 if (decimo_digito % 11) < 2 else 11 - (decimo_digito % 11)
        
        undecimo_digito = sum(int(x) * y for x, y  in zip(cpf[:10], range(11, 1, -1)))
        undecimo_digito = 0 if (undecimo_digito % 11) < 2 else 11 - (undecimo_digito % 11)

        if str(decimo_digito) == cpf[9] and str(undecimo_digito) == cpf[10]:
            return True
        return False

    def gerar_dict(self) -> dict:
        return {
            self.cpf : {
            "nome" : self.nome,
            "email" : self.email,
            "endereco": {
                "cep": self.endereco.cep,
                "uf" : self.endereco.uf,
                "cidade" : self.endereco.cidade
                }
            }
        }