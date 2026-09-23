# SISTEMA DE LOJA VIRTUAL SIMPLIFICADA
Projeto da disciplina de POO 

# Resumo das classes
- Produto
- Cliente
- Carrinho
- Pedido
- Pagamento
- NotaFiscal
- Relatório

# Classes
- ## Produto
    ### Atributos
    - SKU
    - Nome
    - Categoria
    - Preço (>0)
    - Estoque (>=0)
    - Status

    ### Métodos
    - Ajuste de estoque
    - Validação

    - cadastrar_produto()
    - ler_produto()
    - atualizar_produto()
    - remover_produto()

- ## Cliente
    ### Atributos
    - ID
    - Nome
    - Categoria
    - Email
    - CPF
    - Endereço (CEP, Cidade, UF)

    ### Métodos
    - Validação

    - cadastrar_cliente()
    - ler_cliente()
    - atualizar_cliente()
    - remover_cliente()

- ## Carrinho
    ### Atributos
    - Subtotal (Preço do carrinho)
    - Produtos

    ### Métodos
    - adicionar_carrinho()
    - remover_carrinho()
    - alterar_qtd_itens()

- ## Pedido
    ### Atributos
    - Cliente
    - Produtos
    - Frete
    - Desconto
    - Total
    - Estado (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO)

    ### Métodos
    - cancelar_pedido() (somente se CRIADO ou PAGO)
    - calcular_frete()
    - gerar_nota()

- ## Pagamento
    ### Atributos
    - Data
    - Forma (PIX, CREDITO, DEBITO, BOLETO)
    - Valor

    ### Métodos
    - Validação (total pago ≥ total do pedido)
    - pedido_pago() (Mudar o estado do Pedido para Pago)

- ## NotaFiscal
    ### Atributos
    - Código de Rastreio (Se o pedido for Enviado)

    ### Métodos
    - pedido_entregue() (Se a data for alcançada, pedido é Entregue)

- ## Relatório
    ### Atributos
    