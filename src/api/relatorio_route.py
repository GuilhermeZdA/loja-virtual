from fastapi import APIRouter, HTTPException
from src.schema import RelatorioFaturamentoResponse, RelatorioPedidoResponse, RelatorioRankProdutosResponse
from src.repositories import RelatorioJSON

router = APIRouter(prefix = "/relatorio", tags = ["Relatórios"])


@router.get("/pedidos", status_code = 200, response_model = list[RelatorioPedidoResponse])
def exibir_relatorio_pedidos():
    try:
        relatorio_pedidos = RelatorioJSON.gerar_relatorio_pedido()
    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

    return relatorio_pedidos


@router.get("/faturamento", status_code = 200, response_model = RelatorioFaturamentoResponse)
def exibir_faturamento():
    try:
        relatorio_faturamento = RelatorioJSON.gerar_faturamento()
    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))
    
    return relatorio_faturamento


@router.get("/ranking", status_code = 200, response_model = list[RelatorioRankProdutosResponse])
def exibir_ranking_produtos():
    try:
        relatorio_ranking = RelatorioJSON.gerar_ranking_produtos()
    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))
    
    return relatorio_ranking