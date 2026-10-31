from pydantic import Field, BaseModel
from enum import Enum

class TipoCupom(str, Enum):
    VALOR_PERCENTUAL = "%"
    VALOR_FIXO = "$"

class CupomCreate(BaseModel):
    codigo: str = Field(..., description = "Código de identificação do cupom (CUPOM20)")
    tipo: TipoCupom = Field(..., description = "Tipo de desconto do cupom")
    valor: float = Field(..., description = "Valor ou porcentagem do desconto do cupom")
    validade: str = Field(..., description = "Data limite para o uso do cupom. Formato: DD-MM-YYYY (25-09-2027) ")
    qtd_usos: int = Field(..., ge = 0, description = "Quantidade de usos do cupom")


class CupomResponse(BaseModel):
    codigo: str
    tipo: TipoCupom
    valor: float
    validade: str
    qtd_usos: int
    status: str