from fastapi import APIRouter, HTTPException
from src.models import Cupom
from src.repositories import CupomJSON
from src.schema.cupom_schema import CupomCreate, CupomResponse

router = APIRouter(prefix = "/cupom", tags = ["Cupom"])


@router.post("/", status_code = 201, response_model = CupomResponse)
def criar_cupom(dados: CupomCreate):
    try:
        novo_cupom = Cupom(
            codigo = dados.codigo,
            tipo = dados.tipo,
            valor = dados.valor,
            validade = dados.validade,
            qtd_usos = dados.qtd_usos
        )

        CupomJSON.adicionar_cupom(novo_cupom)

        return novo_cupom.gerar_dict()

    except ValueError as erro:
       raise HTTPException(status_code = 400, detail = str(erro))


@router.get("/", status_code = 200, response_model = list[CupomResponse])
def listar_cupons():

    cupons_salvos = CupomJSON.exibir_cupom()

    return cupons_salvos


@router.delete("/{codigo}", status_code = 200)
def remover_cupom(codigo: str):

    sucesso = CupomJSON.remover_cupom(codigo)

    if not sucesso:
        raise HTTPException(status_code = 401, detail = "Cupom não encontrado")

    return {"message": f"cupom de {codigo} removido com sucesso!"}