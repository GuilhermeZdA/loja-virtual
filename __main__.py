from classes.cliente import Cliente
from classes.frete import Endereco

def main():
    e1 = Endereco("63260000", "CE", "Brejo")
    c1 = Cliente("Guilherme", "gui@gmail.com", "11423355695", e1)

    c1.adicionar_cliente()



if __name__ == "__main__":
    main()