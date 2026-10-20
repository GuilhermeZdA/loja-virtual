from src.models import Pedido
from src.caminhos import PEDIDOS
import json

class Relatorio:
    """
    A representação de um relatório sobres as compras.

    Essa classe armazena os dados sobre o fluxo de vendas dentro da loja, o que ajuda o dono a gerenciar as próximas vendas.
    
    Atributos:
        faturamento (float): A soma de todo o dinheiro arrecadado da loja.
        top_vendidos (Dict): Ranking dos produtos mais vendidos.
    """
    def __init__(self):

        @property
        def faturamento(self):
            return calcular_faturamento()

        @staticmethod
        def calcular_faturamento() -> float:
            faturamento = 0
            with open(PEDIDOS, 'r', encoding = "utf-8") as arquivo:
                pedidos = json.load(arquivo)

            for values in pedidos.value():
                if values["estado"] == "ENTREGUE" or "PAGO" or "ENVIADO":
                    faturamento += values["total"]

            return faturamento

        @staticmethod
        def calcular_ranking(): # Precisa do banco de dados
            pass