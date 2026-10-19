from fastapi import APIRouter, HTTPException
from typing import List
from src.schema.cliente_schema import ClienteCreate, ClienteResponse
from src.models import Cliente, Endereco
from src.repositories import PessoaJSON

router = APIRouter(prefix = "/Cliente", tags = ["Cliente"])

@router.post("/", status_code = 201, response_model = ClienteResponse)
def criar_clientes(dados: ClienteCreate):

    try:
        obj_endereco = Endereco (
            cep = dados.endereco.cep,
            uf = dados.endereco.uf,
            cidade = dados.endereco.cidade
        )

        novo_cliente = Cliente (
            nome = dados.nome,
            email = dados.email,
            cpf = dados.cpf,
            endereco = obj_endereco
        )

        PessoaJSON.adicionar_cliente(novo_cliente)

        return novo_cliente

    except ValueError as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

@router.get("/", status_code = 200, response_model = List[ClienteResponse])
def listar_clientes():

    clientes_salvos = PessoaJSON.exibir_cliente()

    return clientes_salvos

@router.delete("/{cpf}", status_code = 200)
def remover_cliente(cpf: str):

    sucesso = PessoaJSON.remover_cliente(cpf)

    if not sucesso:
        raise HTTPException(status_code = 401, detail = "Cliente não encontrado")

    return {"mensagem": f"Produto {cpf} removido com sucesso!"}