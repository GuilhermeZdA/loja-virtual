import json
from src.caminhos import NOTAFISCAL

class NotaFiscalJSON:

    @staticmethod
    def emitir_nota(nova_nota):
        with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)

        dados[str(nova_nota.codigo_nota)] = nova_nota.gerar_dict()

        with open(NOTAFISCAL, 'w', encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii = False , indent = 4)

    @staticmethod
    def cancelar_nota_fiscal(id_pedido: str):
        with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
            notas = json.load(arquivo)

        encontrado = False

        for cod, dados in notas.items():
            if dados["id_pedido"] == id_pedido:
                dados["estado"] = "CANCELADO"
                encontrado = True
                break
            
        if encontrado:
            with open(NOTAFISCAL, 'w', encoding = "utf-8") as arquivo:
                json.dump(notas, arquivo, ensure_ascii = False, indent = 4)
        else:
            raise KeyError("Erro! Nota fiscal não encontrada")

    @staticmethod
    def gerar_codigo() -> int:
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
                
