from retriever import RAGEngine

if __name__ == "__main__":
    # Carrega a base persistida e inicializa o modelo
    rag = RAGEngine()

    print("\n" + "="*50)
    print("--- RAG Documentation & SQL System Ready ---")
    print("="*50)
    while True:
        q = input("\nQuestion: ")
        if q.lower() in ['quit', 'exit']: break
        print(f"\n{rag.ask(q)}\n" + "-"*50)
        # user_input = input("\nPergunta (ou 'sair'): ")
        # if user_input.lower() == 'sair':
        #     break
            
        # resposta = rag.ask(user_input)
        # print(f"\nResposta:\n{resposta}")


# import os
# from config import (
#     NVIDIA_API_KEY,
#     CHROMA_PATH,
#     DATA_PATH,
#     EMBEDDING_MODEL,
#     LLM_MODEL
# )

# from openai import OpenAI

# print("================================")
# print("Running NVIDIA LLM API test")
# print("================================")

# if not NVIDIA_API_KEY:
#     raise ValueError("NVIDIA_API_KEY environment variable is not set.")
# if not os.path.exists(CHROMA_PATH):
#     os.makedirs(CHROMA_PATH)
# if not os.path.exists(DATA_PATH):
#     os.makedirs(DATA_PATH)
# if not EMBEDDING_MODEL:
#     raise ValueError("EMBEDDING_MODEL environment variable is not set.")
# if not LLM_MODEL:
#     raise ValueError("LLM_MODEL environment variable is not set.")


# client = OpenAI(
#   base_url = "https://integrate.api.nvidia.com/v1",
#   api_key = NVIDIA_API_KEY
# )

# if not client:
#     raise ValueError("Failed to create OpenAI client.")

# # response = client.embeddings.create(
# #     input=["What is the civil caseload in South Dakota courts?"],
# #     model="nvidia/llama-nemotron-embed-vl-1b-v2",
# #     encoding_format="float",
# #     extra_body={"modality": ["text"], "input_type": "query", "truncate": "NONE"}
# # )

# # print(response.data[0].embedding)

# # =================== deepseek-v4-pro-0813 =================== #
# # completion = client.chat.completions.create(
# #   model="deepseek-ai/deepseek-v4-pro-0813",
# #   messages=[{"role":"user","content":"Write a limerick about the wonders of GPU computing."}],
# #   temperature=1,
# #   top_p=0.95,
# #   max_tokens=16384,
# #   seed=42,
# #   extra_body={"chat_template_kwargs":{"thinking":False}},
# #   stream=False
# # )

# # print(completion.choices[0].message.content)

# try:
#     # =================== llama-3.1-8b-instruct =================== #
#     completion = client.chat.completions.create(
#       model="meta/llama-3.1-8b-instruct",
#       messages=[{"role":"user","content":"How much is 35 times 2?"}],
#       temperature=0.2,
#       top_p=0.7,
#       max_tokens=1024,
#       stream=False
#     )

#     # Handle both content and tool calls for non-streaming
#     if completion.choices[0].message.content is not None:
#       print(completion.choices[0].message.content)
# except Exception as e:
#     print(f"An error occurred: {e}")




# # ngc registry model download-version nvidia/nemo/llama-3_1-8b-instruct-nemo:2.0