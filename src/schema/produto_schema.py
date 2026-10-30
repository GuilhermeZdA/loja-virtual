from enum import Enum
from pydantic import BaseModel, Field
from typing import Literal, Union, Annotated


class CategoriaProduto(str, Enum):
    ALIMENTO = "ALIMENTO"
    ELETRONICO = "ELETRONICO"
    VESTUARIO = "VESTUARIO"
    DECORACAO = "DECORACAO"
    HIGIENE = "HIGIENE"


class TipoProduto(str, Enum):
    FISICO = "FISICO"
    DIGITAL = "DIGITAL"
    

class ProdutoBase(BaseModel):
    sku: str = Field(..., description = "Código único do produto [3 letras + 5 dígitos] (ELE00005)")
    nome: str = Field(..., description = "Nome do produto")
    categoria: CategoriaProduto = Field(..., description = "Categoria do produto")
    qtd_estoque: int = Field(..., ge = 0, description = "Quantidade de produto no estoque")
    preco: float = Field(..., gt = 0, description = "Preço do produto") 


class ProdutoFisicoCreate(ProdutoBase):
    tipo: Literal["FISICO"]
    peso: float = Field(..., gt = 0, description = "Peso do produto")


class ProdutoDigitalCreate(ProdutoBase):
    tipo: Literal["DIGITAL"]
    codigo_uso: str = Field(..., description = "Código de uso do produto")


ProdutoCreate = Annotated[
    Union[ProdutoFisicoCreate, ProdutoDigitalCreate], Field(discriminator="tipo")
    ]


class ProdutoFisicoResponse(ProdutoBase):
    tipo: Literal["FISICO"]
    peso: float
    status: str

class ProdutoDigitalResponse(ProdutoBase):
    tipo: Literal["DIGITAL"]
    codigo_uso: str
    status: str


ProdutoResponse = Annotated[Union[ProdutoDigitalResponse, ProdutoFisicoResponse], Field(discriminator = "tipo")]