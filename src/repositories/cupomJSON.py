import json
from src.models import Cupom
from src.caminhos import CUPOM

class CupomJSON:

    @staticmethod
    def adicionar_cupom(novo_cupom: Cupom) -> None:
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


    def atualizar_banco(self) -> None:
        dados = self.carregar_cupom()
        dados.update(self.gerar_dict())

        with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii = False, indent = 4)

    # FAZER A VALIDAÇÃO DO TEMPO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def buscar_cupom(self, cod: str) -> tuple: # Vai utilizar o código para localizar o cupom no banco de dados
        if isinstance(cod, str):
            
            cupons = self.carregar_cupom()
            valor = 0

            for codigo, value in cupons.items():
                if codigo == cod:
                    valor = int(value["usos"])
                    if valor == 0:
                        return 0
                    valor -= 1
                    value["usos"] = str(valor)

                    with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
                        json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)
                    return float(value["valor"]), value["tipo"]
            return 0
        else:
            raise TypeError("Erro! O valor deve ser um texto")