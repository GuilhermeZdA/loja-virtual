from classes.produto import Produto

def main():
    p1 = Produto("AAA-123")
    print(p1.sku)
    p1.sku = "AAA-124"
    print(p1.sku)

if __name__ == "__main__":
    main()