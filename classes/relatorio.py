from pagamento import Pagamento

class Relatorio:
    """
    A representação de um relatório sobres as compras.

    Essa classe armazena os dados sobre o fluxo de vendas dentro da loja, o que ajuda o dono a gerenciar as próximas vendas.
    
    Atributos:
        faturamento (float): A soma de todo o dinheiro arrecadado da loja.
        top_vendidos (Dict): Ranking dos produtos mais vendidos.
    """
    def __init__(self, pagamentos: list[Pagamento]):
        self._pagamentos = pagamentos # Usar o banco de dados para buscar os pagamento


    @property
    def pedidos(self):
        return self._pagamentos

    def calcular_faturamento(self) -> float:
        faturamento = 0
        for pagamento in self._pagamentos:
            faturamento += pagamento.valor
        return self._pagamentos

    def ranking(self): # Precisa do banco de dados
        pass