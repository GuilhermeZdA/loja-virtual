from enum import Enum
from pydantic import BaseModel, Field

class CategoriaProduto(str, Enum):
    ALIMENTO = "ALIMENTO"
    ELETRONICO = "ELETRONICO"
    VESTUARIO = "VESTUARIO"
    DECORACAO = "DECORACAO"
    HIGIENE = "HIGIENE"


class ProdutoCreate(BaseModel):
    sku: str = Field(..., description = "Código único do produto")
    nome: str = Field(..., description = "Nome do produto")
    categoria: CategoriaProduto = Field(..., description = "Categoria do produto")
    qtd_estoque: int = Field(..., ge = 0, description = "Quantidade de produto no estoque")
    preco: float = Field(..., gt = 0, description = "Preço do produto")


class ProdutoResponse(BaseModel):
    sku: str
    nome: str
    categoria: CategoriaProduto
    qtd_estoque: int
    preco: float
    status: str