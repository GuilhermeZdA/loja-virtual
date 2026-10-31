from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.models import Pedido, Endereco, ItemPedido, Cupom, Frete
from src.repositories import PedidoJSON, PessoaJSON, CupomJSON, ProdutoJSON, NotaFiscalJSON
from src.schema import PedidoCreate, PedidoResponse

from src.api.carrinho_route import carrinhos_ativos

router = APIRouter(prefix = "/pedido", tags = ["Pedido"])


@router.get("/pedido/{id_}", status_code = 200, response_model = PedidoResponse)
def exibir_pedido(id_: str):
    try:
        pedido_atual = PedidoJSON.buscar_pedido(id_)
        return pedido_atual

    except KeyError:
        raise HTTPException(status_code = 404, detail = "Erro! Produto não encontrado")


@router.post("/", status_code = 201, response_model = PedidoResponse)
def iniciar_pedido(dados: PedidoCreate):

    if dados.cpf not in carrinhos_ativos:
        raise HTTPException(status_code = 404, detail = f"Erro! Não existe carrinho cadastrado com o CPF {dados.cpf}")

    carrinho_cliente = carrinhos_ativos[dados.cpf]

    if not carrinho_cliente.itens:
        raise HTTPException(status_code = 400, detail = "Erro! O carrinho está vazio")


    # Cria instâncias ItemPedido para garantir a imutabilidade do pedido
    itens_static = []
    for item_carrinho in carrinho_cliente.itens:
        item_pedido = ItemPedido(
            item = item_carrinho.item,
            qtd = item_carrinho.qtd
        )
        itens_static.append(item_pedido)


    endereco_dados = PessoaJSON.buscar_dados("endereco", dados.cpf)

    endereco_obj = Endereco(
        cep = endereco_dados["cep"],
        uf = endereco_dados["uf"],
        cidade = endereco_dados["cidade"]
    )


    cupom_obj = None

    if dados.cod_cupom is not None:

        cupom_dados = CupomJSON.buscar_cupom(dados.cod_cupom)

        if cupom_dados is None:
            raise HTTPException(status_code = 404, detail = f"Erro! não existe cupom com o código {dados.cod_cupom}")

        if cupom_dados["status"] == "INATIVO":
            raise HTTPException(status_code = 400, detail = "Erro! O cupom está inatico")

        cupom_obj = Cupom(
            codigo = cupom_dados["codigo"],
            tipo = cupom_dados["tipo"],
            valor = cupom_dados["valor"],
            validade = cupom_dados["validade"],
            qtd_usos = cupom_dados["qtd_usos"]
        )


    frete_obj = Frete(
        uf = endereco_dados["uf"],
        peso_total = carrinho_cliente.peso_total
    )


    novo_pedido = Pedido(
        id_ = PedidoJSON.gerar_id(),
        cpf = dados.cpf,
        endereco = endereco_obj,
        itens = itens_static,
        frete = frete_obj,
        cupom = cupom_obj
    )

    PedidoJSON.adicionar_pedidos(novo_pedido)

    ProdutoJSON.retirar_estoque(novo_pedido.itens)

    if dados.cod_cupom is not None:
        CupomJSON.descontar_usos(dados.cod_cupom)

    del carrinhos_ativos[dados.cpf]

    return novo_pedido.gerar_dict()


@router.patch("/pedido/{id_}/cancelar")
def cancelar_pedido(id_: str):
    try:

        pedido_atual = PedidoJSON.buscar_pedido(id_)

        if pedido_atual["estado"] == "CANCELADO":
            raise HTTPException(status_code = 400, detail = "Erro! O pedido já está cancelado")

        if pedido_atual["estado"] == "PAGO" or pedido_atual["estado"] == "CRIADO":

            PedidoJSON.atualizar_estado(id_, "CANCELADO")

            ProdutoJSON.devolver_estoque(pedido_atual["itens"])

            NotaFiscalJSON.cancelar_nota_fiscal(id_) 

            return {"message" : "O pedido foi cancelado com sucesso!"}

        else:
            raise HTTPException(status_code = 400, detail = f"Não é possível cancelar um pedido que já foi {pedido_atual['estado']}")
    
    except KeyError:
        raise HTTPException(status_code = 404, detail = f"Erro! Não existe pedido de ID {id_}")


@router.patch("/pedido/{id_}/enviar")
def enviar_pedido(id_: str):
    try:

        pedido_atual = PedidoJSON.buscar_pedido(id_)

        if pedido_atual["estado"] == "ENVIADO":
            return {"message": "O pedido já foi ENVIADO"}

        if pedido_atual["estado"] == "PAGO":

            codigo_rastreio = PedidoJSON.gerar_cod_rastreio()
            
            PedidoJSON.atualizar_estado(id_, "ENVIADO")
            PedidoJSON.atualizar_cod_rastreio(id_, codigo_rastreio)

            return {"message": "O pedido foi ENVIADO com sucesso"}

        else:
            raise HTTPException(status_code = 400, detail = f"Não é possivel enviar um pedido que foi {pedido_atual['estado']}")
        
    except KeyError:
        raise HTTPException(status_code = 404, detail = f"Erro! Não existe pedido de ID {id_}")


@router.patch("/pedido/{id_}/entregar")
def entregar_pedido(id_: str):
    try:

        pedido_atual = PedidoJSON.buscar_pedido(id_)

        if pedido_atual["estado"] == "ENTREGUE":
            return {"message": "O pedido já foi ENTREGUE"}

        if pedido_atual["estado"] == "ENVIADO":

            data_pag = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            PedidoJSON.atualizar_estado(id_, "ENTREGUE")
            
            PedidoJSON.atualizar_data_entrega(id_, data_pag)

            return {"message": "O pedido foi entregue com sucesso"}

        else:
            raise HTTPException(status_code = 400, detail = f"Não é possivel enviar um pedido que foi {pedido_atual['estado']}")

    except KeyError:
        raise HTTPException(status_code = 404, detail = "Erro! Não existe pedido de ID {id_}")