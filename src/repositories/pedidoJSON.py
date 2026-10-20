import json
from random import choice
from src.models import Pedido
from src.caminhos import PEDIDOS

class PedidoJSON:


    @staticmethod
    def adicionar_pedidos(novo_pedido: Pedido):
        with open(PEDIDOS, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        dados.update(novo_pedido.gerar_dict())

        with open(PEDIDOS, 'w', encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii = False , indent = 4)
        
    @staticmethod
    def gerar_id() -> str:
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        try:
            with open(PEDIDOS, 'r', encoding = "utf-8") as arquivo:
                dados = json.load(arquivo)
        except(FileNotFoundError, json.JSONDecodeError):
            dados = {}

        while True:
            novo_id = ""

            while len(novo_id) < 5:
                novo_id += choice(list(caracteres))

            if novo_id not in dados:
                return novo_id