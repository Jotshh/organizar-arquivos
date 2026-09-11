"""
Organizador de Arquivos por Tipo
---------------------------------
Percorre uma pasta e move cada arquivo para uma subpasta de acordo
com sua extensão (ex: .pdf -> PDFs, .jpg -> Imagens).
"""

import logging
import shutil
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
CAMINHO_DA_PASTA = os.getenv("CAMINHO_PASTA")

print(CAMINHO_DA_PASTA)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

PASTA_ALVO = Path(CAMINHO_DA_PASTA)

TIPOS = {
    ".pdf": "PDFs",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".pptx": "Slides",
    ".png": "Imagens",
    ".txt": "Textos",
    ".docx": "Documentos",
    ".odt": "Documentos",
}


def organizar_pasta(pasta_alvo: Path) -> None:

    if not pasta_alvo.exists():
        logging.error("Pasta não encontrada: %s", pasta_alvo)
        return
    for item in list(pasta_alvo.iterdir()):

        if item.is_dir():
            continue

        extensao = item.suffix.lower()

        if extensao not in TIPOS:
            continue

        pasta_destino = pasta_alvo / TIPOS[extensao]

        try:
            pasta_destino.mkdir(exist_ok=True)
            shutil.move(str(item), str(pasta_destino / item.name))
            logging.info("Movido: %s -> %s", item.name, pasta_destino.name)

        except PermissionError:
            logging.warning("Sem permissão para mover: %s (arquivo em uso?)", item.name)
        except FileExistsError:
            logging.warning("Já existe um arquivo com esse nome em %s: %s", pasta_destino, item.name)
        except OSError as erro:
            logging.error("Erro ao mover %s: %s", item.name, erro)


if __name__ == "__main__":
    organizar_pasta(PASTA_ALVO)
