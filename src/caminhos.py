from pathlib import Path

CAMINHO_RAIZ = Path(__file__).resolve().parent

CAMINHO_DB = CAMINHO_RAIZ / "db"
CLIENTES = CAMINHO_DB / "clientes.json"
PRODUTOS = CAMINHO_DB / "produtos.json"
PEDIDOS = CAMINHO_DB / "pedidos.json"
CUPOM = CAMINHO_DB / "cupom.json"
NOTAFISCAL = CAMINHO_DB / "notafiscal.json"
SETTINGS = CAMINHO_DB /  "settings.json"