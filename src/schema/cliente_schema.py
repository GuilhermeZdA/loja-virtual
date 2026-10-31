from pydantic import BaseModel, Field

class EnderecoSchema(BaseModel):
    cep: str = Field(..., description = "CEP do cliente, 8 números (63000001)")
    uf: str = Field(..., description = " Unidade Federativa do cliente (CE)")
    cidade: str = Field(..., description = "Cidade habitada pelo cliente")

class EnderecoResponse(BaseModel):
    cep: str
    uf: str
    cidade: str


class ClienteCreate(BaseModel): # Molde de entrada
    nome: str = Field(..., description = "Nome do cliente")
    email: str = Field(..., description = "Email do cliente (peaple@gmail.com)")
    cpf: str = Field(..., description = "Cadastro de Pessoa Física do Cliente")
    endereco: EnderecoSchema = Field(..., description = "CEP, Cidade e UF do cliente")


class ClienteResponse(BaseModel): # Molde de saída
    nome: str
    email: str
    cpf: str
    endereco: EnderecoSchema