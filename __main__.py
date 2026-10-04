from classes.produto import Produto, ProdutoDigital, ProdutoFisico

def main():
    p1 = ProdutoFisico("AAA123", "Banana", "Alimento", 5.0, 30)
    print(p1.__dict__)


if __name__ == "__main__":
    main()