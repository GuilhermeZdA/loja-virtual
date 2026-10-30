from fastapi import APIRouter, HTTPException
from src.models import Pagamento, NotaFiscal
from src.repositories import PedidoJSON, NotaFiscalJSON
from src.schema import NotaFiscalResponse, PagamentoCreate, PagamentoResponse

router = APIRouter(prefix = "/pagamento", tags = ["Pagamento"])

@router.get("/", status_code = 200, response_model = list[NotaFiscalResponse])
def listar_notas_fiscais():

    notas_salvas = NotaFiscalJSON.exibir_notas()

    return notas_salvas

@router.post("/{id_}/pagar", response_model = PagamentoResponse)
def processar_pagamento(id_: str, dados: PagamentoCreate):

    try:
        pedido_atual = PedidoJSON.buscar_pedido(id_)

        if pedido_atual["estado"] != "CRIADO":
            raise HTTPException(status_code = 400, detail = "O pagamento já foi realizado")

        if pedido_atual["estado"] == "CANCELADO":
            raise HTTPException(status_code = 400, detail = "O pedido foi cancelado")

        pagamento_obj = Pagamento(
            forma_pag = dados.forma_pag,
            valor_pago = dados.valor_pag
        )

        if pagamento_obj.valor_pago == pedido_atual["total"]:

            PedidoJSON.atualizar_estado(id_, "PAGO")
            PedidoJSON.atualizar_data_pag(id_, pagamento_obj.data.strftime("%d-%m-%Y %H:%M:%S"))
            PedidoJSON.atualizar_forma_pag(id_, pagamento_obj.forma_pag)

            novo_codigo_nota = NotaFiscalJSON.gerar_codigo()

            nota_obj = NotaFiscal(
                codigo_nota = novo_codigo_nota,
                id_pedido = id_,
                cpf = pedido_atual["cpf"],
                valor_pago = dados.valor_pag,
                produtos = pedido_atual["itens"]
            )

            NotaFiscalJSON.emitir_nota(nota_obj)

            return pagamento_obj.gerar_dict()
            
        else:
            raise HTTPException(status_code = 400, detail = "O pagamento é maior que o valor do pedido")
        
    except KeyError:
        raise HTTPException(status_code = 404, detail = "Pedido não encontrado")