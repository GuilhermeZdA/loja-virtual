from fastapi import APIRouter
from src.schema import RelatorioFaturamentoResponse, RelatorioPedidoResponse, RelatorioRankProdutosResponse
from src.repositories import RelatorioJSON

router = APIRouter(prefix = "/relatorio", tags = ["Relatórios"])

@router.get("/pedidos", status_code = 200, response_model = list[RelatorioPedidoResponse])
def exibir_relatorio_pedidos():
    relatorio_pedidos = RelatorioJSON.gerar_relatorio_pedido()

    return relatorio_pedidos


@router.get("/faturamento", status_code = 200, response_model = RelatorioFaturamentoResponse)
def exibir_faturamento():
    relatorio_faturamento = RelatorioJSON.gerar_faturamento()

    return relatorio_faturamento


@router.get("/ranking", status_code = 200, response_model = list[RelatorioRankProdutosResponse])
def exibir_ranking_produtos():
    relatorio_ranking = RelatorioJSON.gerar_ranking_produtos()

    return relatorio_ranking