from pydantic import BaseModel, Field
from enum import Enum
from src.schema.cliente_schema import EnderecoResponse

class EstadoPedido(str, Enum):
    CRIADO = "CRIADO"
    PAGO = "PAGO"
    ENVIADO = "ENVIADO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"


class PedidoCreate(BaseModel):
    cpf: str = Field(..., description = "Cadastro de Pessoa Física (CPF) do Cliente")
    cod_cupom: str | None = Field(default = None, description = "Código de identificação do cupom")


class ItemPedidoResponse(BaseModel):
    sku: str
    nome: str
    qtd: int
    preco_unit: float
    subtotal_preco: float
    subtotal_peso: float


class PedidoResponse(BaseModel):
    id_: str
    cpf: str
    itens: list[ItemPedidoResponse]
    data: str
    frete: float
    desconto: float
    total: float
    estado: EstadoPedido
    endereco: EnderecoResponse
    forma_pag: str | None = None