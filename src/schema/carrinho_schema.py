from pydantic import BaseModel, Field

class ItemCarrinhoCreate(BaseModel):
    sku: str = Field(..., description = "Código único do produto")
    qtd: int = Field(..., gt = 0, description = "Quantidade desse produto adicionado no carrinho")


class ItemCarrinhoResponse(BaseModel):
    sku: str
    nome: str
    qtd: int
    subtotal_preco: float
    subtotal_peso: float
    

class CarrinhoResponse(BaseModel):
    cpf: str
    itens: list[ItemCarrinhoResponse]
    preco_total: float
    peso_total: float