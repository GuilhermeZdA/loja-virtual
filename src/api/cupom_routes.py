from fastapi import APIRouter, HTTPException
from src.models import Cupom
from src.repositories import CupomJSON
from src.schema.cupom_schema import CupomCreate, CupomResponse, CupomUpdate

router = APIRouter(prefix = "/cupom", tags = ["Cupom"])


@router.post("/", status_code = 201, response_model = CupomResponse)
def criar_cupom(dados: CupomCreate):

    if CupomJSON.cupom_existe(dados.codigo):
        raise HTTPException(status_code = 400, detail = "Erro! Já existe um cupom com esse código")
        
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

    if not cupons_salvos:
        raise HTTPException(status_code = 404, detail = "Erro! Não existe cupons cadastrados")
    
    return cupons_salvos


@router.patch("/cupom/{cod_cupom}/{atributo}", status_code = 200)
def atualizar_atributo(cod_cupom: str, atributo: str, dados: CupomUpdate):
    atributos_permitidos = ["validade", "valor"]

    atributo = atributo.strip().lower()

    if atributo not in atributos_permitidos:
        raise HTTPException(status_code = 400, detail = f"Erro! É possivel modificar apenas os atributos {atributos_permitidos}")

    if not CupomJSON.cupom_existe(cod_cupom):
        raise HTTPException(status_code = 400, detail = f"Erro! Não existe cupom cadastrado com o código {cod_cupom}")

    cupons_salvos = CupomJSON.buscar_cupom()

    if not cupons_salvos:
        raise HTTPException(status_code = 400, detail = "Erro! Não há cupons cadastrados")

    cupom_atual = cupons_salvos[cod_cupom]

    if cupom_atual["status"] == "INATIVO":
        raise HTTPException(status_code = 400, detail = "Erro! Não é possível alterar um cupom inativo")

    cupom_atual[atributo] = dados.novo_valor
    cupom_atual.pop("status", None) # O status nasce na instância só depois de inicializada

    try:
        validador = Cupom(**cupom_atual)
    except Exception as erro:
        raise HTTPException(status_code = 400, detail = str(erro))

    CupomJSON.atualizar_dados(cod_cupom, atributo, dados.novo_valor)

    return {"message": f"{atributo} atualizado com sucesso!"}


@router.delete("/{codigo}", status_code = 200)
def remover_cupom(codigo: str):

    sucesso = CupomJSON.remover_cupom(codigo)

    if not sucesso:
        raise HTTPException(status_code = 401, detail = "Cupom não encontrado")

    return {"message": f"cupom de {codigo} removido com sucesso!"}