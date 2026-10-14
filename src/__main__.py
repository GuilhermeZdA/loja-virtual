from models import Cliente, Endereco
from repositories.pessoaJSON import PessoaJSON
from caminhos import CLIENTES

def main():
    e1 = Endereco("63260000", "CE", "Brejos")
    c1 = Cliente("gui", "guimail@gmail.com", "36972168309", e1)
    gerenciador = PessoaJSON(CLIENTES)

    gerenciador.adicionar_cliente(c1)
    gerenciador.exibir_cliente()
    gerenciador.remover_cliente(c1)
    gerenciador.exibir_cliente()


if __name__ == "__main__":
    main()