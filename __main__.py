from classes.cliente import Cliente
from classes.frete import Endereco
from classes.produto import Produto

def main():
    # e1 = Endereco("63260000", "CE", "Brejo")
    # c1 = Cliente("Guilherme", "gui@gmail.com", "11423355695", e1)
    # c2 = Cliente("augutusf", "shdf@jaosd.com", "52998224725", e1)

    # c1.adicionar_cliente()
    # c2.adicionar_cliente()
    p1 = Produto("ABC1234", "Uva", "ALIMENTO", 10, 2.50)
    p1.adicionar_produto() 



if __name__ == "__main__":
    main()