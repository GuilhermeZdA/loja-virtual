from pydantic import Field, BaseModel
from typing import Literal

class CupomCreate(BaseModel):
    codigo: str = Field(..., description = "Código de identificação do cupom")
    tipo: Literal["$", "%"] = Field(..., description = "Qual o tipo de desconto do cupom ($/%)")
    valor: float = Field(..., description = "Valor do desconto do cupom")
    validade: str = Field(..., description = "Data limite para o uso do cupom. Formato: DD-MM-YYYY (Ex: 12-11-2027) ")
    qtd_usos: int = Field(..., ge = 0, description = "Limite de usos do cupom")


class CupomResponse(BaseModel):
    codigo: str
    tipo: Literal["$", "%"]
    valor: float
    validade: str
    qtd_usos: int
    status: str