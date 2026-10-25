import json
from src.caminhos import CLIENTES

class PessoaJSON:

    @staticmethod
    def adicionar_cliente(nova_pessoa) -> None:
        with open(CLIENTES, 'r', encoding = "utf-8") as arquivo:
            pessoas = json.load(arquivo)

        pessoas.update(nova_pessoa.gerar_dict())

        with open(CLIENTES, "w", encoding = "utf-8") as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii = False, indent = 4) # indent = 4 deixa bonito

    @staticmethod
    def exibir_cliente() -> list:
        with open(CLIENTES, 'r', encoding = "utf-8") as arquivo:
            pessoas = json.load(arquivo)

        lista_clientes = []

        if isinstance(pessoas, dict):
            for cpf, dados in pessoas.items():
                if isinstance(dados, dict):
                    item = dados.copy()
                    item["cpf"] = cpf
                    lista_clientes.append(item)

        if isinstance(pessoas, list):
            lista_clientes = pessoas

        return lista_clientes

    @staticmethod
    def remover_cliente(cpf: str) -> bool:
        with open(CLIENTES, 'r', encoding = "utf-8") as arquivo:
            pessoas = json.load(arquivo)
        encontrado = False

        if cpf in pessoas:
            del pessoas[cpf]
            encontrado = True

        if encontrado:
            with open(CLIENTES, 'w', encoding = "utf-8") as arquivo:
                json.dump(pessoas, arquivo, ensure_ascii = False, indent = 4)
        
        return encontrado


    @staticmethod
    def buscar_dados(tipo, cpf):
        with open(CLIENTES, 'r', encoding = "utf-8") as arquivo:
            pessoas = json.load(arquivo)

        if cpf not in pessoas:
            raise ValueError("Erro! não existe cliente com esse CPF")

        try:
            dado = pessoas[cpf][tipo]
            return dado
        except KeyError:
            raise ValueError(f"Erro! O dado {tipo} não existe no cadastro deste cliente.")