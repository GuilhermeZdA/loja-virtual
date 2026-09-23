# SISTEMA DE LOJA VIRTUAL SIMPLIFICADA
Projeto da disciplina de POO 

# Resumo das classes
- Cliente
- Produto
- ProdutoFisico
- ProdutoDigital
- ItemPedido
- Carrinho
- Pedido
- Pagamento
- NotaFiscal
- Relatório

# Classes
- ## Cliente
    ### Atributos
    - ID
    - Nome
    - Categoria
    - Email
    - CPF
    - Endereço (CEP, Cidade, UF)

    ### Métodos
    - cadastrar_cliente()
    - exibir_cliente()
    - atualizar_cliente()
    - remover_cliente()

- ## Produto
    ### Atributos
    - SKU
    - Nome
    - Categoria
    - Preço (>0)
    - Estoque (>=0)
    - Status

    ### Métodos
    - cadastrar_produto()
    - exibir_produto()
    - atualizar_produto()
    - remover_produto()

- ## ProdutoDigital
    ProdutoDigital -> Produto

- ## ProdutoFisico
    ProdutoFisico -> Produto
    ### Atributos
    - Peso

- ## ItemPedido
    ### Atributos
    - Item
    - Quantidade

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
    - pedido_pago() (Mudar o estado do Pedido para Pago)

- ## NotaFiscal
    ### Atributos
    - Código de Rastreio (Se o pedido for Enviado)

    ### Métodos
    - pedido_entregue() (Se a data for alcançada, pedido é Entregue)

- ## Relatório
    ### Atributos
    - Faturamento
    - Produtos mais vendidos
    - Vendas por categoria

    ### Métodos
    -exibir_relatório()
    