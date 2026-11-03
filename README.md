# SISTEMA DE LOJA VIRTUAL SIMPLIFICADA

## Descrição
O projeto Sistema de Loja Virtual Simplificada possibilita que um cliente cadastre-se ao informar alguns dados pessoais para fornecer a capacidade de adicionar produtos da loja dentro de um carrinho virtual, depois efetuar um pedido de pagamento, o qual pode receber descontos por cupons ou acréscimos devido ao frete. Por fim, o cliente recebe uma nota fiscal, enquanto o dono da loja tem acesso a um relatório das vendas.

## Objetivo
Criar um sistema que facilite o comércio físico e virtual ao automatizar, organizar e otimizar várias etapas de uma transação comercial, como a criação de relatórios de venda, a realização do pedido de compra e o pagamento e a alocação de produtos no carrinho. Assim, o sistema facilita a compra pelos clientes e a organização do comércio pelo comerciante.

## Indice

[🔗](#como-acessar-o-projeto) Como acessar o projeto?

[🔗](#como-utilizar-a-api) Como utilizar a API?

[🔗](#fluxo-operacional) Fluxo operacional

[🔗](#decisões-de-implementação) Decisões de implementação


# Como acessar o projeto?

## 1. Clonar o repositório

Execute no terminal o comando:

```bash
git clone https://github.com/GuilhermeZdA/loja-virtual.git
```

para salvar uma cópia do projeto na sua máquina. Em seguida, entre no repositório pela sua IDE (VSCODE).


## 2. Instalar dependências

Python 3.12 ou superior.

FastAPI: Utilizada para criar a API do sistema e configurar suas rotas.
Uvicorn: Utilizada para executar um servidor web onde a API vai funcionar.
Pydantic: Utilizada para facilitar a validação dos dados na API.

Execute no terminal os comandos:

```bash
pip install fastapi
```
```bash
pip install uvicorn
```
```bash
pip install pydantic
```

## 3. Carregar o banco de dados

Passo opcional, preenche o banco de dados (Clientes, Produtos e Cupons) com alguns dados ficticios para testar o funcionamento do projeto.

```bash
python seed.py
```


## 4. Iniciar o servidor

Há duas formas para inicializar o servidor do Uvicorn:

### 1. Comando do Uvicorn no terminal

```bash
uvicorn src.api.main:app --reload
```
<br>

### 2. Executando o arquivo run.py

- Windows
```bash
python run.py
```
- Linux ou macOS
```bash
python3 run.py
```
<br>

**OBS**: Caso precise encerrar o servidor, execute o comando Ctrl + C no terminal ou apague o terminal. A página do SWAGGER não funcionará até que o servidor seja inicializado novamente e a página seja atualizada.

## 5. Acessando a página da API

Com o servidor do Uvicorn inicializado, acesse esse link:

**http://127.0.0.1:8000/docs**

para acessar a documentação interativa da API (Swagger)

## 6. Visão da API

Numa análise superficial, a página da API apresenta título, versão, descrição da API, os recursos (Produto, Cliente, etc) e no final 'Schemas'.

![Página inicial do Swagger](img/inicio-pagina.png)

# Como utilizar a API?

1. Escolha um recurso da API e uma de suas ações.

No exemplo será selecionado o Get do Cupom.

![Recurso Cupom da API](img/cupom-recurso.png)

2. Selecione a opção "Try it out"

![Recurso Cupom da API](img/cupom-get-try.png)

🟨: Parameters são as dados inseridos pelo usuário, nesse exemplo o usuário não precisa inserir informações.

🟥: Responses são as respostas da API em caso de sucesso ou de falha. Em caso de erro, uma mensagem especificando o que ocorreu é exibida. 

🟦: Try it Out habilita a execução da função, edição de parametros e do Request Body.

3. Selecione a opção "Execute"

![Recurso Cupom sendo executado](img/cupom-get-execute.png)

4. Veja os resultados no "Response body"

![Resultados do get Cupom](img/cupom-get-execute-sucesso.png)

🟦: Code 200 representando um sucesso

## Dicas e casos especificos

No geral, esses 4 passos são suficientes para executar o método Get dos recursos, mas para executar o Post, Delete e Patch há algumas pequenas diferenças.

### Parametros
---
Alguns métodos exigem que parametros sejam inseridos. Uma caixa de entrada (input) será exibida quando parametros forem exigidos.

![Input Delete Cupom](img/cupom-delete.png)


### Request Body
---
Para analisar a API, o Request Body aceita dados para simular seu funcionamento

![Request Body Cupom Post](img/cupom-post.png)

Nesse exemplo, o POST do recurso Cupom recebe diversos dados. Um deles é o código do cupom, representado abaixo:
```python
{"codigo" : "string"}
```

O nome escrito na esquerda ("codigo") nunca deve ser alterado. Já o nome na direita ("string") deve ser alterado no formato válido de cada atributo.
```python
{"codigo" : "CUPOM20"}
```

### Schema
---
Em baixo do Resquest Body, há dois nomes: Edit Value e Schema. Selecione Schema para acessar a descrição de cada atributo. As descrições são curtas e podem conter:
- Explicação sobre o que é atributo.
- Especificação de critérios de validação.
- Exemplos.
- Um enum contendo os valores aceitos.

![Schema do Cupom Post](img/cupom-schema.png)


# Fluxo operacional

## 1. Cadastro de entidades

O primeiro passo do sistema é o cadastro de clientes, produtos e cupons. Essas são as entidades básicas do sistema e são necessárias para realizar as próximas ações.

![Recursos Cliente, Produto e Cupom](img/produto-cliente.png)

## 2. Criação do Carrinho de Compras

O cliente cadastrado no sistema pode informar seu CPF, a quantidade e o SKU do produto que ela deseja adicionar ao carrinho. Após criar um carrinho, você pode exibi-lo fornecendo o CPF cadastrado nele, exclui-lo por inteiro ou retirar apenas produtos específicos.

**OBS**: O carrinho diferentemente das outros dados, não é armazenado em uma banco de dados, com o intuito de simular um Local Storage. Então caso o servidor reinicie ou ocorra algum erro, os dados dos carrinhos serão **APAGADOS**. Transforme-os em pedidos para evitar que isso aconteça.

![Carrinho POST](img/carrinho.png)

## 3. Criação do Pedido

O Pedido é uma dos recursos mais importantes e complexos da API. Inicialmente ele utiliza os dados do carrinho, cliente, cupom para calcular preço total, descontos do cupom, acréscismo do frete, data de criação do pedido e armazenas outras informações.

O pedido pode seguir esses fluxos:

```mermaid
graph LR
CRIADO ---> PAGO ---> ENVIADO ---> ENTREGUE

CRIADO ---> PAGO ---> CANCELADO

CRIADO ---> CANCELADO
```

Para criar o pedido é necessário informar o CPF que foi informado no carrinho e o código do cupom no POST.

![Iniciar Pedido](img/pedido-iniciar.png)

**OBS**: Caso o código do cupom não seja informado, digite **null** onde o código seria informado.

```python
{
"cpf": 12345678909,
"cod_cupom": null
}
```

## 4. Efetuar o pagamento

Após a criação do pedido, o próximo passo é o cliente efetuar o pagamento. O valor do pagamento deve ser **igual** ao valor total do pedido, além disso uma nota fiscal será gerada, armazenando alguns dados do pagamento. A nota fiscal também segue um fluxo que depende do cancelamento do pedido.

```mermaid
graph LR
EMITIDO ---> CANCELADO
```

## 5. Envio, Entrega e Cancelamento do Pedido

O pedido pode ser cancelado, enviado ou entregue. Para realizar essas mudanças, é necessário informar o ID do pedido gerado ao inicia-lo.

* CANCELADO: Bloqueia mudanças no pedido, cancela a nota fiscal e devolve os produtos para o estoque.
* ENVIADO: O produto vai ser enviado, gera um código de rastreio.
* ENTREGUE: O produto foi entregue no destino, gera uma data de entrega.

A mudança desses estados devem seguir o caminho do [fluxograma](#3-criação-do-pedido).

## 6. Relatórios

O recurso Relatórios oferece 3 tipos diferentes de análise de dados da loja:

* Relatório dos pedidos: Informa a quantidade/porcentagem de pedidos em cada um de seus estados.
* Faturamento e Ticket médio: Informa o faturamento total da loja, a quantidade de vendas finalizadas e o valor médio de cada venda. 
* Ranking dos produtos: Informa quais foram os produtos mais vendidos da loja.

# Decisões de implementação

## 1. O Uso de API em vez de CLI

A especificação libera criar uma interface por CLI ou por API, inicialmente planejava fazer a CLI, mas escolhi fazer a API para entender e aprender a usar APIs, visto que é uma competência muito útil de se adquirir. Utilizei o framework FastAPI devido ao nome, que me fez pensar que seria rápido e fácil, mas foi o que mais ocupou tempo no projeto e causou dor de cabeça, uma vez que eu não tinha experiência com APIs e o projeto já estava bem encaminhado. Por isso, tive que modificar muito o código, mas essas alterações trouxeram diversos beneficios, como:

* A visualização do projeto e a realização de testes ficaram muito fáceis, por causa do /docs do Swagger.
* A compreensão da lógica do vendas da lolja ficou melhor.
* O tratamento de erro facilitou encontrar não quebra o sistema e facilita a identificação de bugs

## 2. A persistência utilizando JSON

Escolhi fazer a persistência com JSON porque eu sabia como funcionava, mas não sabia implementar bem, então eu optei por ele. Além disso, eu não tenho experiência com SQLite ou outros SGBDs, mas como eu estou na disciplina de Bancos de Dados, eu escolhi por aprender por ela.

## 3. O uso de /repository

Em uma das aulas de POO, o orientador comentou sobre o uso desse padrão, o qual separa a lógica do negócio da infraestrutura do banco de dados, assim todas as funções relacionadas à persistência foram armazenadas nos arquivos no /repository. Essa mudança foi muito benéfica no projeto, pois ela ocorreu junto com a adesão da API e a organização da estrutura dos diretórios, o que deixou o projeto muito mais organizado e fácil de localizar. Uma das consequências foi a facilidade de realizar mudanças no código.

## 4. O uso de /schema

O uso de schemas facilitou muito a validação de dados, umas vez que o Basemodel do Pydantic cria uma classe que serve de molde das informações que entram na API e das informações que a API envia. Assim, o sistema acabou adquirindo uma dupla validação: schema e o property das classes.

## 5. O carrinho armazenado na memória

Escolhi não fazer a persistência para o carrinho de compras, pois eu quis simular a ideia de que o carrinho fica pré-pronto para cada cliente, como um local storage ou cookies. Então cuidado ao desligar o servidor do uvicorn.

## 6. Estrutura dos diretórios

Utilizei o padrão com /src, porque deixa bem organizado os diretórios, era o que eu conhecia e todo mundo usa e entende. Os demais diretórios foram nomeados com base no que eles armazenam (/schema) e de forma que eles ficassem com uma imagem especial na IDE.

![Diretórios na IDE](img/diretorios.png)

# Estrutura dos diretórios

```
loja-virtual/
├── README.md                    
├── LICENSE
├── .gitignore            
├── run.py     
├── seed.py    
│
├── img/    
│
└── src/
    ├── caminhos.py
    │
    ├── api/ 
    │   ├── main.py            
    │   ├── produto_route.py  
    │   ├── cliente_route.py    
    │   ├── cupom_routes.py    
    │   ├── carrinho_route.py   
    │   ├── pedido_route.py   
    │   ├── pagamento_routes.py  
    │   └── relatorio_route.py 
    │
    ├── models/                 
    │   ├── produto.py     
    │   ├── cliente.py     
    │   ├── frete.py          
    │   ├── carrinho.py        
    │   ├── pedido.py    
    │   └── pagamento.py   
    │
    ├── schema/ 
    │   ├── produto_schema.py
    │   ├── cliente_schema.py
    │   ├── cupom_schema.py
    │   ├── carrinho_schema.py
    │   ├── pedido_schema.py
    │   ├── pagamento_schema.py
    │   ├── notafiscal_schema.py
    │   └── relatorio_schema.py
    │
    ├── repositories/           
    │   ├── produtoJSON.py     
    │   ├── pessoaJSON.py      
    │   ├── cupomJSON.py       
    │   ├── pedidoJSON.py     
    │   ├── notafiscalJSON.py 
    │   ├── freteJSON.py      
    │   └── relatorioJSON.py  
    │
    └── db/
        ├── produtos.json
        ├── clientes.json
        ├── cupom.json
        ├── pedidos.json
        ├── notafiscal.json
        └── settings.json   
```

# Lista das classes 
1. Cliente
2. Produto
3. ProdutoDigital
4. ProdutoFisico
5. ItemCarrinho
6. Carrinho
7. Pedido
8. ItemPedido
9. Cupom
10. Pagamento
11. NotaFiscal
12. Endereco
13. Frete

# Diagrama de classes

```mermaid
classDiagram
    direction LR

    class Cliente {
        +str nome
        +str email
        +str cpf
        +Endereco endereco
        +validar_cpf()
    }
    
    class Endereco {
        +str cep
        +str uf
        +str cidade
    }

    class Produto {
        +str sku
        +str nome
        +str categoria
        +int qtd_estoque
        +float preco
        +str status
        +analisar_status()
        +gerar_dict()
    }

    class ProdutoFisico {
        +float peso
    }

    class ProdutoDigital {
        +str codigo_uso
    }

    class ItemCarrinho {
        +int qtd
        +float subtotal_preco
        +float subtotal_peso
    }

    class Carrinho {
        +str cpf
        +float preco_total
        +float peso_total
        +adicionar_item()
        +remover_item()
        +&lowbar;&lowbar;len&lowbar;&lowbar;()
    }

    class Frete {
        +str uf
        +float peso_total
        +calcular_frete()
    }

    class Cupom {
        +str codigo
        +str tipo
        +float valor
        +str validade
        +int qtd_usos
        +analisar_status()
    }

        class ItemPedido {
        +int qtd
        +float preco_unit
        +float subtotal_preco
    }

    class Pedido {
        +str id_
        +str estado
        +float desconto
        +float total
        +calcular_desconto()
        +calcular_total()
        +&lowbar;&lowbar;str&lowbar;&lowbar;()
    }

    class Pagamento {
        +str forma_pag
        +float valor_pago
    }

    class NotaFiscal {
        +int codigo_nota
        +str estado
    }

    Produto <|-- ProdutoFisico
    Produto <|-- ProdutoDigital
    Cliente *-- Endereco
    Carrinho "1" *-- "*" ItemCarrinho
    ItemCarrinho --> Produto
    Pedido "1" *-- "*" ItemPedido
    ItemPedido --> Produto
    Pedido *-- Frete
    Pedido o-- Endereco
    Pedido o-- "0..1" Cupom
    Pedido ..> Carrinho : criado a partir de
    Pagamento ..> Pedido : paga
    Pagamento ..> NotaFiscal : gera
```









### **Para uma visão mais detalhada, o [link](https://miro.com/app/board/uXjVHjQXB5Y=/?share_link_id=994540664978) de acesso do diagrama pelo Miro.**

![Diagrama UML](img/diagrama.jpg)

# Classes detalhadas

- ## Cliente
    ### Atributos
    - id
    - nome
    - categoria
    - email
    - cpf
    - endereço (CEP, Cidade, UF)

    ### Métodos
    - cadastrar_cliente()
    - exibir_cliente()
    - atualizar_cliente()
    - remover_cliente()

- ## Produto
    ### Atributos
    - sku
    - nome
    - categoria
    - preço_unidade (>0)
    - qtd_stoque (>=0)
    - status

    ### Métodos
    - cadastrar_produto()
    - exibir_produto()
    - atualizar_produto()
    - remover_produto()

- ## ProdutoDigital
    ProdutoDigital -> Produto
    ### Atributos
    - codigo_uso

- ## ProdutoFisico
    ProdutoFisico -> Produto
    ### Atributos
    - peso

- ## ItemCarrinho
    ### Atributos
    - item
    - qtd

- ## Carrinho
    ### Atributos
    - cliente
    - itens
    - preco_total
    - peso_total

    ### Métodos
    - adicionar_carrinho()
    - remover_carrinho()
    - alterar_qtd_itens()

- ## Pedido
    ### Atributos
    - carrinho
    - frete
    - desconto
    - total
    - estado (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO)

    ### Métodos
    - cancelar_pedido() (somente se CRIADO ou PAGO)
    - buscar_frete()
    - usar_cupom()
    - calcular_total()

- ## ItemPedido
    ### Atributos
    - item
    - qtd
    - preco_unidade

- ## Cupom
    ### Atributos
    - codigo
    - tipo (Valor/Percentual)
    - valor
    - validade
    - categoria
    - qtd_usos

- ## Pagamento
    ### Atributos
    - data
    - forma (PIX, CREDITO, DEBITO, BOLETO)
    - valor

    ### Métodos
    - efetuar_pagamento() (Mudar o estado do Pedido para Pago)
    - gerar_nota()

- ## NotaFiscal
    ### Atributos
    - valor_pago
    - produtos
    - data
    
    ### Métodos
    - exibir_nota()

- ## Endereco
    ### Atributos
    - cep
    - cidade
    - uf

- ## Frete
    ### Atributos
    - endereco
    - peso_total
    - valor

    ### Métodos
    - calcular_frete()