from classes.cliente import Cliente
from classes.frete import Endereco
from classes.produto import Produto
from classes.pedido import Cupom

def main():
    e1 = Endereco("63260000", "CE", "Brejos")
    c1 = Cliente("gui", "guimail@gmail.com", "36972168309", e1)
    c1.exibir_cliente()

if __name__ == "__main__":
    main()