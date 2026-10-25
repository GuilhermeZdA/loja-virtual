from src.caminhos import SETTINGS
import json

class FreteJSON:

    @staticmethod
    def buscar_multiplicador(uf: str) -> int:
        with open(SETTINGS, 'r', encoding = "utf-8") as arquivo:
            configs = json.load(arquivo)

        uf = uf.upper()

        if uf in configs["taxa_uf"]:
            multiplicador = configs["taxa_uf"][uf]
            return multiplicador
        else:
            raise KeyError("Erro! UF não encontrada!")

    @staticmethod
    def taxa_fixa():
        with open(SETTINGS, 'r', encoding = "utf-8") as arquivo:
            configs = json.load(arquivo)

        return configs["taxa_peso"]["taxa_kg"]