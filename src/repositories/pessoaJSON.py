import json
from src.models.cliente import Cliente

class PessoaJSON:
    def __init__(self, caminho):
        self.caminho = caminho


    @property
    def caminho(self):
        return self._caminho

    @caminho.setter
    def caminho(self, novo_caminho):
        self._caminho = novo_caminho


    def carregar_cliente(self) -> dict:
        with open(self.caminho, 'r', encoding= "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

    def adicionar_cliente(self, pessoa: Cliente) -> None:
        pessoas = self.carregar_cliente()
        pessoas.update(pessoa.gerar_dict())

        with open(self.caminho, "w", encoding = "utf-8") as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii = False, indent = 4) # indent = 4 deixa bonito
        print("deu certo")

    def exibir_cliente(self) -> None:
        pessoas = self.carregar_cliente()

        print("=" * 140)
        print(f'{"NOME":^50}{"EMAIL":^30}{"CPF":^13}{"UF":^5}{"CIDADE":^30}{"CEP":^15}')
        print("=" * 140)

        for key, value in pessoas.items():
            print(f'{value["nome"]:^50}{value["email"]:^30}{key:^13}{value["endereco"]["uf"]:^5}{value["endereco"]["cidade"]:^30}{value["endereco"]["cep"]:^15}')
            print("-" * 140)

    def remover_cliente(self, pessoa) -> str:
        pessoas = self.carregar_cliente()
        encontrado = False

        if pessoa.cpf in pessoas:
            del pessoas[pessoa.cpf]
            encontrado = True

        if encontrado:
            with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
                json.dump(pessoas, arquivo, ensure_ascii = False, indent = 4)
            return "deu certo"
        return "dados não encontrados"