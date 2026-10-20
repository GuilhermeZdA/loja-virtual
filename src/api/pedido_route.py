from fastapi import APIRouter
from src.models import Pedido
from src.repositories import PedidoJSON, PessoaJSON
from src.schema.pedido_schema import PedidoCreate, PedidoResponse, ItemPedidoResponse

router = APIRouter(prefix = "/pedido", tags = ["PEDIDO"])

@router.post("/", status_code = 201, response_model = PedidoResponse)
def iniciar_pedido(dados: PedidoCreate):
    novo_pedido = Pedido(
        id_ = PedidoJSON.gerar_id(),
        cpf = dados.cpf,
        endereco = PessoaJSON.buscar_dados("endereco", dados.cpf),
        itens = [""],
        cod_cupom = dados.cod_cupom
    )