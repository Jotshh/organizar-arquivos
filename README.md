# Organizador de Arquivos

Script em Python que organiza automaticamente os arquivos de uma pasta em subpastas, de acordo com o tipo de extensão (PDFs, Imagens, Documentos, Slides, Textos, etc.).

## Funcionalidades

- Varre uma pasta e move cada arquivo para uma subpasta baseada em sua extensão.
- Cria as subpastas de destino automaticamente, caso não existam.
- Registra logs de cada ação (arquivo movido, ignorado ou com erro).
- Trata erros comuns (arquivo em uso, permissão negada, nome duplicado) sem travar a execução.
- Caminho da pasta configurável por variável de ambiente (não fica fixo no código).

## 🗂️ Tipos de arquivo suportados

| Extensão | Pasta de destino |
|---|---|
| `.pdf` | PDFs |
| `.jpg`, `.jpeg`, `.png` | Imagens |
| `.pptx` | Slides |
| `.txt` | Textos |
| `.docx`, `.odt` | Documentos |

Tu pode adicionar outras pastas para outras extensões no array TIPOS

## Pré-requisitos

- Python 3.10+
- Biblioteca `python-dotenv`

Instale a dependência com:

```bash
pip install python-dotenv
```

## Configuração (arquivo `.env`)

O caminho da pasta que será organizada deverá ser definida o seu caminho por meio de um arquivo `.env` na raiz do projeto.

1. Crie um arquivo chamado `.env` na raiz do repositório.
2. Dentro dele, defina a variável `CAMINHO_PASTA` com o caminho da pasta que deseja organizar:

```env
CAMINHO_PASTA=C:/Users/seu_usuario/Downloads
```

3. Salve o arquivo. O script lê essa variável automaticamente através do `load_dotenv()`.

## Como usar

Com o `.env` configurado, basta executar:

```bash
python main.py
```

O script vai:
1. Ler o caminho definido em `CAMINHO_PASTA`.
2. Percorrer os arquivos dessa pasta.
3. Mover cada um para a subpasta correspondente ao seu tipo (criando a subpasta se necessário).
4. Exibir no terminal um log de cada movimentação.

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
