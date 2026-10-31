from pydantic import BaseModel

class RelatorioPedidoResponse(BaseModel):
    estado: str
    quantidade: float
    percentual: str


class RelatorioFaturamentoResponse(BaseModel):
    faturamento: float
    quantidade_vendas: int
    ticket_medio: float


class RelatorioRankProdutosResponse(BaseModel):
    nome: str
    sku: str
    quantidade_vendido: float