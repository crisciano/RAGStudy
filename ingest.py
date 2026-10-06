import os
import json
import hashlib
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_community.vectorstores import Chroma
import config

# Local file to track the state of processed files
HASH_FILE = "processed_hashes.json"

def calculate_md5(file_path):
    """Generates an MD5 hash by reading the file in chunks to save memory."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def run_ingestion():
    stored_hashes = load_hashes()
    new_hashes = stored_hashes.copy()
    docs_to_process = []
    
    # 1. Identify new or modified files
    for filename in os.listdir(config.DATA_PATH):
        if filename.endswith(".pdf"):
            file_path = os.path.join(config.DATA_PATH, filename)
            current_hash = calculate_md5(file_path)
            
            # If it's a new file or its content has changed
            if file_path not in stored_hashes or stored_hashes[file_path] != current_hash:
                print(f"[PROCESSING] New/Modified: {filename}")
                # Using individual PyPDFLoader instead of DirectoryLoader
                loader = PyPDFLoader(file_path)
                docs_to_process.extend(loader.load())
                new_hashes[file_path] = current_hash
            else:
                print(f"[SKIPPED] No changes: {filename}")

    if not docs_to_process:
        print("\nNo new files to process. Exiting pipeline.")
        return

    # 2. Chunk only the files that need processing
    print(f"\nSplitting {len(docs_to_process)} pages/documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(docs_to_process)
    print(f"Created {len(chunks)} new text chunks.")

    # 3. Initialize Embedding model
    embeddings = NVIDIAEmbeddings(
        model="nvidia/llama-nemotron-embed-vl-1b-v2", 
        nvidia_api_key=config.NVIDIA_API_KEY
    )

    # 4. Add to ChromaDB (it automatically appends to the existing directory)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=config.CHROMA_PATH
    )
    
    # 5. Save the new hash state only if everything succeeded
    save_hashes(new_hashes)
    print("Vector store updated successfully!")

if __name__ == "__main__":
    run_ingestion()