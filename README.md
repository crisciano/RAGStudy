# RAG Documentation & SQL Assistant

A **Retrieval-Augmented Generation (RAG)** pipeline built on top of NVIDIA AI Endpoints and ChromaDB. It ingests PDF documents, stores them as vector embeddings, and answers natural language questions — including SQL query generation — grounded in the ingested content.

---

## Architecture

```
PDFs (data/)
    │
    ▼
[ingest.py]  →  PyPDFLoader + RecursiveCharacterTextSplitter
                    │
                    ▼
             NVIDIAEmbeddings (nvidia/llama-nemotron-embed-vl-1b-v2)
                    │
                    ▼
              ChromaDB  (chroma_db/)
                    │
                    ▼
[retriever.py]  →  Similarity Search (top-k chunks)
                    │
                    ▼
             ChatNVIDIA LLM  (meta/muse-glimmer-30b)
                    │
                    ▼
              [init.py]  →  Interactive CLI
```

---

## Project Structure

```
RAG/
├── config.py           # Centralized configuration (models, paths, API key)
├── ingest.py           # PDF ingestion pipeline with MD5-based change detection
├── retriever.py        # RAGEngine class — vector retrieval + LLM chain (LCEL)
├── init.py             # Interactive CLI entry point
├── checkModels.py      # Utility to list all available NVIDIA models
├── generatePDF.py      # Generates a sample SysOrder documentation PDF for testing
├── requirements.txt    # Python dependencies
├── Makefile            # Environment setup commands
├── envvars             # Exported environment variables (not committed)
├── processed_hashes.json  # Tracks MD5 hashes to avoid reprocessing unchanged files
├── data/               # Drop PDF documents here for ingestion
└── chroma_db/          # Persistent ChromaDB vector store
```

---

## Prerequisites

- **WSL** (Windows Subsystem for Linux) or a Linux/macOS environment
- **Python 3.10+**
- A valid **NVIDIA AI Endpoints API key** — obtain one at [build.nvidia.com](https://build.nvidia.com)

---

## Setup

```bash
# 1. Start WSL (Windows only)
wsl

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
make install

# 4. Configure your API key
#    Edit the Makefile and set NVIDIA_API_KEY, then run:
make dotenv

# 5. Load the environment variables
source .envvars

# 6. Verify the API key is set
echo $NVIDIA_API_KEY
```

> **SSL issues (corporate networks):** If you get certificate errors, export these before running any script:
> ```bash
> export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
> export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
> ```

---

## Usage

### 1. Generate a sample document (optional)

Creates `data/sysorder_docs.pdf` — a mock e-commerce system documentation used for testing.

```bash
python generatePDF.py
```

### 2. Ingest PDFs into the vector store

Drop any `.pdf` files into the `data/` folder, then run:

```bash
python ingest.py
```

The pipeline:
- Computes an MD5 hash for each PDF.
- Skips files that haven't changed since the last run.
- Splits new/modified documents into 800-token chunks (150-token overlap).
- Embeds and stores chunks in ChromaDB.

### 3. Start the interactive assistant

```bash
python init.py
```

Type any question about your ingested documents. Type `quit` or `exit` to stop.

### 4. Inspect available NVIDIA models

```bash
python checkModels.py
```

Prints all available embedding and chat models from the NVIDIA API.

---

## Configuration (`config.py`)

| Variable          | Default value                              | Description                        |
|-------------------|--------------------------------------------|------------------------------------|
| `NVIDIA_API_KEY`  | `$NVIDIA_API_KEY` env var                  | NVIDIA AI Endpoints API key        |
| `CHROMA_PATH`     | `./chroma_db`                              | ChromaDB persistence directory     |
| `DATA_PATH`       | `./data`                                   | Directory scanned for PDF files    |
| `EMBEDDING_MODEL` | `nvidia/llama-nemotron-embed-vl-1b-v2`     | Embedding model used for indexing  |
| `LLM_MODEL`       | `meta/muse-glimmer-30b`                    | Chat model used for generation     |

---

## How It Works

1. **Ingestion** (`ingest.py`): Reads all PDFs from `data/`, splits them into overlapping text chunks using `RecursiveCharacterTextSplitter`, generates vector embeddings via the NVIDIA API, and persists them in ChromaDB. MD5 hashing ensures only new or modified files are reprocessed.

2. **Retrieval** (`retriever.py`): On each query, `RAGEngine` performs a similarity search against the vector store to retrieve the top-4 most relevant chunks. These chunks are injected as context into the LLM prompt.

3. **Generation** (`retriever.py`): A LangChain LCEL chain combines the retrieved context with the user's question and sends it to the NVIDIA-hosted LLM. The system prompt instructs the model to answer based strictly on the provided context and to generate SQL queries when requested.

---

## Suggested Improvements

### Retrieval quality
- **Hybrid search**: Combine vector similarity with BM25 keyword search (e.g., using `langchain_community.retrievers.BM25Retriever`) to improve recall on exact term matches.
- **Re-ranking**: Add a cross-encoder re-ranker after the initial retrieval step to improve the ranking of the top-k chunks before feeding them to the LLM.
- **Contextual chunking**: Experiment with `SemanticChunker` (LangChain) instead of `RecursiveCharacterTextSplitter` to produce semantically coherent chunks.
- **Metadata filtering**: Store page number, document name, and section heading as chunk metadata and expose them as filters in queries.

### Ingestion
- **Multi-format support**: Extend ingestion to handle `.docx`, `.txt`, `.csv`, and web pages (e.g., using `UnstructuredFileLoader`).
- **Incremental deletions**: Track removed files in `processed_hashes.json` and delete their corresponding vectors from ChromaDB.
- **Async ingestion**: Process multiple PDFs concurrently using `asyncio` or `concurrent.futures` to speed up large batches.

### Interface
- **Web UI**: Wrap `RAGEngine` in a FastAPI backend and add a simple frontend (Streamlit or Gradio) for a browser-based chat interface.
- **Streaming responses**: Use `.stream()` instead of `.invoke()` in `RAGEngine.ask()` to stream tokens to the terminal or UI in real time.
- **Chat history**: Add conversation memory (e.g., `ConversationBufferWindowMemory`) so the LLM can reference previous turns.
- **Source citations**: Return the source document name and page number alongside each answer.

### Security & ops
- **Secret management**: Move the API key out of the Makefile entirely and load it exclusively from a `.env` file (ignored by `.gitignore`) using `python-dotenv`.
- **Input validation**: Sanitize and truncate user queries before sending them to the LLM to prevent prompt injection.
- **Logging**: Replace `print` statements with Python's `logging` module for structured, level-based output.
- **Tests**: Add unit tests for `calculate_md5`, `run_ingestion`, and `RAGEngine.ask` using `pytest` and mocked NVIDIA API responses.

### Models
- **Swap the LLM**: Try `meta/llama-3.1-405b-instruct` or `mistralai/mistral-large-3-675b-instruct-2512` for higher quality answers.
- **Swap the embedding model**: `nvidia/nv-embedqa-e5-v5` or `baai/bge-m3` may yield better retrieval accuracy depending on your document domain.
