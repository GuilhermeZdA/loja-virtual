from pathlib import Path

CAMINHO_RAIZ = Path(__file__).resolve().parent

CAMINHO_DB = CAMINHO_RAIZ / "db"
CLIENTES = CAMINHO_DB / "clientes.json"