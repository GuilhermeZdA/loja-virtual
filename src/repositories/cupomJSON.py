import json
from models.pedido import Cupom

class CupomJSON:
    def __init__(self, caminho):
        self.caminho = caminho


    @property
    def caminho(self):
        return self._caminho

    @caminho.setter
    def caminho(self, novo_caminho):
        self._caminho = novo_caminho


    def carregar_cupom(self) -> dict:
        with open(self.caminho, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

    def adicionar_cupom(self, novo_cupom: Cupom) -> None:
        cupons = self.carregar_cupom()
        cupons.update(novo_cupom.gerar_dict())

        with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)

    def exibir_cupom(self) -> None:
        cupons = self.carregar_cupom()

        print("=" * 90)
        print(f'{"CÓDIGO":^10}{"TIPO":^10}{"VALOR":^15}{"VALIDADE":^20}{"QUANTIDADE DE USOS":^25}')
        print("=" * 90)

        for key, value in cupons.items():
            print(f'{key:^10}{value["tipo"]:^10}{value["valor"]:^15}{value["validade"]:^20}{value["usos"]:^25}')
            print("-" * 90)

    def remover_cupom(self, cupom: Cupom) -> None:
        cupons = self.carregar_cupom()
        encontrado = False

        if cupom.codigo in cupons:
            del cupons[cupom.codigo]
            encontrado = True

        if encontrado:
            with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
                json.dump(cupons, arquivo, ensure_ascii = False, indent = 4)

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