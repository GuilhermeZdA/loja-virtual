import json
from src.caminhos import PEDIDOS, NOTAFISCAL

class RelatorioJSON:


    @staticmethod
    def gerar_relatorio_pedido() -> list:
        with open(PEDIDOS, 'r', encoding = "utf-8") as arquivo:
            pedidos_salvos = json.load(arquivo)

        if not pedidos_salvos:
            return {"message": "Nenhum pedido salvo"}
        
        total_pedido = len(pedidos_salvos)
        cont = {}

        for pedido in pedidos_salvos.values():
            estado = pedido["estado"]

            if estado in cont:
                cont[estado] += 1
            else:
                cont[estado] = 1
            
        resultado = []

        for estado, qtd in cont.items():
            percentual = (qtd / total_pedido) * 100 

            item = {
                "estado": estado,
                "quantidade": qtd,
                "percentual": f"{percentual:.2f}%"
            }

            resultado.append(item)

        return resultado

    @staticmethod
    def gerar_faturamento() -> dict:
        with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
            notas_salvas = json.load(arquivo)

        if not notas_salvas:
            return {"message": "Nenhuma nota fiscal salva"}

        quantidade_vendas = 0
        faturamento = 0.0

        for nota in notas_salvas.values():
            if nota["estado"] == "EMITIDO":
                faturamento += nota["valor_pago"]
                quantidade_vendas += 1

        if quantidade_vendas > 0:
            ticket_medio = faturamento / quantidade_vendas
        else:
            ticket_medio = 0

        resultado = {
            "faturamento": faturamento,
            "quantidade_vendas": quantidade_vendas,
            "ticket_medio": ticket_medio
        }

        return resultado

    @staticmethod
    def gerar_ranking_produtos() -> list:
        with open(NOTAFISCAL, 'r', encoding = "utf-8") as arquivo:
            notas_salvas = json.load(arquivo)

        if not notas_salvas:
            return {"message": "nenhuma nota fiscal salva"}

        cont = {}

        for notas in notas_salvas.values():
            for produto in notas["produtos"]:
                sku = produto["sku"]
                if sku in cont:
                    cont[sku]["quantidade_vendido"] += produto["qtd"]
                else:

                    item = {
                        sku : {
                        "nome": produto["nome"],
                        "sku" : sku,
                        "quantidade_vendido": produto["qtd"]
                        }
                    }

                    cont.update(item)

        resultado = []

        while cont:
            sku_maior = ""
            maior = -1

            for key, dados in cont.items():
                if dados["quantidade_vendido"] > maior:
                    maior = dados["quantidade_vendido"]
                    sku_maior = key

            dados_maior = cont[sku_maior]

            resultado.append(dados_maior)

            del cont[sku_maior]

        return resultado
            

                    
