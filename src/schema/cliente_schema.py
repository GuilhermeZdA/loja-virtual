from pydantic import BaseModel, Field

class EnderecoSchema(BaseModel):
    cep: str = Field(..., description = "CEP do lugar onde o cliente habita")
    uf: str = Field(..., description = " Unidade Federatica onde o cliente habita")
    cidade: str = Field(..., description = "Cidade onde o cliente habita")


class ClienteCreate(BaseModel): # Molde de entrada
    nome: str = Field(..., description = "Nome do cliente")
    email: str = Field(..., description = "Email do cliente")
    cpf: str = Field(..., description = "Cadastro de Pessoa Física (CPF) do Cliente")
    endereco: EnderecoSchema = Field(..., description = "CEP, Cidade e UF do cliente")


class ClienteResponse(BaseModel): # Molde de saída
    nome: str
    email: str
    cpf: str
    endereco: EnderecoSchema