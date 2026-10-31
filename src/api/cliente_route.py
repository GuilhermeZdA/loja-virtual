from fastapi import APIRouter, HTTPException
from src.schema import ClienteCreate, ClienteResponse, ClienteUpdate
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


@router.get("/", status_code = 200, response_model = list[ClienteResponse])
def listar_clientes():

    clientes_salvos = PessoaJSON.exibir_cliente()

    return clientes_salvos


@router.patch("/cliente/{cpf}/{atributo}", status_code = 200)
def atualizar_atributo(cpf: str, atributo: str, dados: ClienteUpdate):
    atributos_permitidos = ["nome", "email"]

    atributo = atributo.strip().lower()
    dados.novo_valor = dados.novo_valor.strip()
    cpf = cpf.strip()

    if atributo not in atributos_permitidos:
        raise HTTPException(status_code = 400, detail = f"Erro! É possivel modificar apenas os atributos {atributos_permitidos}")

    if not PessoaJSON.cliente_existe(cpf):
        raise HTTPException(status_code = 400, detail = f"Erro! Não existe cliente cadastrado com o CPF {cpf}")


    clientes_ativos = PessoaJSON.buscar_cliente()

    if not clientes_ativos:
        raise HTTPException(status_code = 400, detail = "Erro! Não há clientes cadastrados")

    cliente_atual = clientes_ativos[cpf]

    if not cliente_atual:
        raise HTTPException(status_code = 400, detail = f"Erro! Não existe cliente com CPF {cpf}")

    try:
        endereco_obj = Endereco(**cliente_atual["endereco"])

    except (ValueError, TypeError) as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

    cliente_atual[atributo] = dados.novo_valor
    cliente_atual["endereco"] = endereco_obj

    try:
        validador = Cliente(cpf = cpf, **cliente_atual)

    except (ValueError, TypeError) as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

    PessoaJSON.atualizar_dados(cpf, atributo, dados.novo_valor)

    return {"message": f"{atributo} atualizado com sucesso!"}


@router.delete("/{cpf}", status_code = 200)
def remover_cliente(cpf: str):

    sucesso = PessoaJSON.remover_cliente(cpf)

    if not sucesso:
        raise HTTPException(status_code = 401, detail = "Cliente não encontrado")

    return {"message": f"cliente de {cpf} removido com sucesso!"}