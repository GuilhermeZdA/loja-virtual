import json
from src.caminhos import CUPOM

class CupomJSON:

    @staticmethod
    def adicionar_cupom(novo_cupom) -> None:
        with open(CUPOM, 'r', encoding = "utf-8") as arquivo:
            cupons = json.load(arquivo)

        cupons[novo_cupom.codigo] = novo_cupom.gerar_dict()

        with open(CUPOM, 'w', encoding = "utf-8") as arquivo:
            json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)


    @staticmethod
    def exibir_cupom() -> None:
        with open(CUPOM, 'r', encoding = "utf-8") as arquivo:
            cupons = json.load(arquivo)

        lista_cupons = []

        if isinstance(cupons, dict):
            for codigo, dados in cupons.items():
                item = dados.copy()
                item["codigo"] = codigo
                lista_cupons.append(item)

        if isinstance(cupons, list):
            lista_cupons = cupons

        return lista_cupons

    @staticmethod
    def remover_cupom(codigo: str) -> None:
        with open(CUPOM, 'r', encoding = "utf-8") as arquivo:
            cupons = json.load(arquivo)
        encontrado = False

        if codigo in cupons:
            del cupons[codigo]
            encontrado = True

        if encontrado:
            with open(CUPOM, 'w', encoding = "utf-8") as arquivo:
                json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)

        return encontrado

    @staticmethod
    def buscar_cupom(cod: str) -> dict:
        with open(CUPOM, 'r', encoding = "utf-8") as arquivo:
            cupons = json.load(arquivo)

        if cod in cupons:
            return cupons[cod]

        return None

    @staticmethod
    def descontar_usos(codigo_cupom: str):
        with open(CUPOM, 'r', encoding = "utf-8") as arquivo:
            cupons = json.load(arquivo)

        if codigo_cupom in cupons:
            qtd_usos = cupons[codigo_cupom]["qtd_usos"]

            if qtd_usos > 0:
                nova_qtd = qtd_usos - 1
                cupons[codigo_cupom]["qtd_usos"] = nova_qtd

                if nova_qtd == 0:
                    cupons[codigo_cupom]["status"] = "INATIVO"

        with open(CUPOM, 'w', encoding = "utf-8") as arquivo:
            json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)