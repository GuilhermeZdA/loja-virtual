import json
from src.caminhos import NOTAFISCAL

class NotaFiscalJSON:

    @staticmethod
    def adicionar_pedidos(nova_nota):
        with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)

        dados[nova_nota.codigo_nota] = nova_nota.gerar_dict()

        with open(NOTAFISCAL, 'w', encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii = False , indent = 4)

    @staticmethod
    def gerar_codigo():
        try:
            with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
                dados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {}

        if not dados:
            return 1

        numeros = []
        for key in dados.keys():
            numeros.append(int(key))

        return max(numeros) + 1
                
