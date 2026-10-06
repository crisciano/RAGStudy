import os

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
CHROMA_PATH = "./chroma_db"
DATA_PATH = "./data"

# NVIDIA Models
EMBEDDING_MODEL = "nvidia/llama-nemotron-embed-vl-1b-v2"  # or any other available in the API
# EMBEDDING_MODEL = "nvidia/nv-embed-qa-4"  # alternative embedding model
LLM_MODEL = "meta/muse-glimmer-30b"

SEPARATORS = ["\n\n", "\n", " ", ""]  # Separators for text chunking