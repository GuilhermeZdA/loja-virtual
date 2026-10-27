from pydantic import BaseModel, Field
from enum import Enum

class FormaPagamento(str, Enum):
    PIX = "PIX"
    CREDITO = "CREDITO"
    DEBITO = "DEBITO"
    BOLETO = "BOLETO"


class PagamentoCreate(BaseModel):
    forma_pag: FormaPagamento = Field(..., description = "Forma de pagamento do pedido (PIX, CREDITO, DEBITO, BOLETO)")
    valor_pag: float = Field(..., description = "Valor pago pelo cliente")


class PagamentoResponse(BaseModel):
    data: str
    forma_pag: FormaPagamento
    valor_pago: float