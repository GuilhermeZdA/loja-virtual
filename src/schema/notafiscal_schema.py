from pydantic import BaseModel
from enum import Enum
from .pedido_schema import ItemPedidoResponse

class EstadoNotaFiscal(str, Enum):
    EMITIDO = "EMITIDO"
    CANCELADO = "CANCELADO"

class NotaFiscalResponse(BaseModel):
    codigo_nota: str
    id_pedido: str
    cpf: str
    valor_pago: float
    produtos: list[ItemPedidoResponse]
    estado: EstadoNotaFiscal