import json
from src.caminhos import CLIENTES, PRODUTOS, PEDIDOS, CUPOM, NOTAFISCAL, SETTINGS
from src.models import Cliente, Cupom, Endereco, ProdutoDigital, ProdutoFisico
from src.repositories import CupomJSON, PessoaJSON, ProdutoJSON

FRETE = {
    "taxa_peso": {
        "taxa_kg": 4.0
    },

    "taxa_uf": {
        "CE": 2, "RN": 2, "PI": 2, "PB": 2, "PE": 2, "MA": 2,
        "AL": 3, "SE": 3, "BA": 3, "PA": 3, "AP": 3, "TO": 3,
        "AC": 4, "AM": 4, "RO": 4, "RR": 4, "MT": 4, "MS": 4, "GO": 4, "DF": 4,
        "MG": 4, "ES": 4, "RJ": 4, "SP": 4, "PR": 4, "SC": 4, "RS": 4,
    },
}

def limpar_banco():
    for arquivo in (CLIENTES, PRODUTOS, PEDIDOS, CUPOM, NOTAFISCAL):
        arquivo.write_text("{}", encoding="utf-8")

    if not SETTINGS.exists():
        SETTINGS.write_text(json.dumps(indent = 4), encoding="utf-8")


def seed_cliente():

    clientes = [Cliente("Weskley Weskio", "weskley@gmail.com", "12345678909", Endereco("63010000", "CE", "Juazeiro do Norte")),
                Cliente("Gael Will", "gaelwill@ufca.edu.br", "04151427767", Endereco("01000000", "SP", "São Paulo")),
                Cliente("Gabrielson Gomes", "gabrielson@gmail.com", "75609432413", Endereco("69970000", "AC", "Taracaucá"))]

    for cliente in clientes:
        PessoaJSON.adicionar_cliente(cliente)


def seed_produto():
    produtos = [ProdutoDigital("AVA001", "Avast", "ELETRONICO", 20, 100.0, "AVASTUSAR"),
                ProdutoDigital("GOW2018", "God of War", "ELETRONICO", 10, 149.9, "A4FEW2"),
                ProdutoFisico("MES001", "Mesa de madeira", "DECORACAO", 5, 250.0, 50),
                ProdutoFisico("ATM002", "Lata de Atum", "ALIMENTO", 10, 3.0, 0.3)]

    for produto in produtos:
        ProdutoJSON.adicionar_produto(produto)

def seed_cupom():
    cupons = [Cupom("CUPOM10", "$", 10, "20-10-2027", 3),
              Cupom("LOJA20", "%", 20, "31-12-2026", 5)]

    for cupom in cupons:
        CupomJSON.adicionar_cupom(cupom)

def main():
    limpar_banco()
    seed_cliente()
    seed_produto()
    seed_cupom()

if __name__ == "__main__":
    main()