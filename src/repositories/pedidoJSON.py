import json
from models.pedido import Pedido

class PedidoJSON:
    def __init__(self, caminho):
        self.caminho = caminho


    @property
    def caminho(self):
        return self._caminho

    @caminho.setter
    def caminho(self, novo_caminho):
        self._caminho = novo_caminho


    def carregar_pedidos(caminho) -> dict:
        with open(caminho, 'r', encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados

    def adicionar_pedidos(self, novo_pedido: Pedido) -> None:
        pedidos = self.carregar_pedidos()
        pedidos.update(novo_pedido.gerar_dict())

        with open(self.caminho, 'w', encoding = "utf-8") as arquivo:
            json.dump(pedidos, arquivo, ensure_ascii = False , indent = 4)

    def gerar_id(self) -> str: #TESTAR
        dados = self.carregar_pedidos()
        novo_id = 0

        if not dados: # JSON vazio
            novo_id = "1"
            return novo_id

        for ids in dados.keys():
            ids = int(ids)
            if ids - novo_id >= 2:
                novo_id += 1
                break
            if novo_id < ids:
                novo_id = ids

        return str(novo_id)