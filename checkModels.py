from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA

# Isso vai imprimir uma lista com os nomes exatos dos modelos que você pode usar
print("="*50)
print("Available Embedding Models:")
print("="*50)
for model in NVIDIAEmbeddings.get_available_models():
    print(model.id)

print("="*50)
print("Available Chat Models:")
print("="*50)
for model in ChatNVIDIA.get_available_models():
    # print(model.id)
    if model.model_type in ["chat", "completion"]:
        print(model.id)


# ==============================================================
# Modelos de Embeddings disponíveis:
# ==============================================================
# snowflake/arctic-embed-l
# baai/bge-m3
# nvidia/llama-nemotron-embed-1b-v2
# nvidia/llama-3.2-nv-embedqa-1b-v2
# nvidia/nv-embedqa-e5-v5
# nvidia/nv-embedqa-mistral-7b-v2
# nvidia/nv-embedcode-7b-v1
# nvidia/llama-3.2-nv-embedqa-1b-v1
# NV-Embed-QA
# nvidia/llama-3.2-nemoretriever-300m-embed-v2
# nvidia/nv-embed-v1
# nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1
#  ==============================================================
# Modelos de Chat disponíveis:
#  ==============================================================
# mistralai/mistral-medium-3-instruct
# moonshotai/kimi-k2-instruct-0905
# stepfun-ai/step-3.5-flash
# nvidia/nemotron-3-ultra-550b-a55b
# zyphra/zamba2-7b-instruct
# utter-project/eurollm-9b-instruct
# bytedance/seed-oss-36b-instruct
# mistralai/mixtral-8x7b-instruct-v0.1
# google/gemma-3-1b-it
# mistralai/magistral-small-2506
# deepseek-ai/deepseek-v3.2
# ibm/granite-guardian-3.0-8b
# mistralai/mistral-medium-3.5-128b
# mistralai/ministral-3-14b-instruct-2512
# nvidia/nemoretriever-parse
# nvidia/nemotron-3-super-120b-a12b
# google/gemma-2-27b-it
# nvidia/llama-3.1-nemotron-nano-8b-v1
# google/paligemma
# meta/llama-3.2-11b-vision-instruct
# mistralai/mistral-small-3.1-24b-instruct-2503
# qwen/qwen3-next-80b-a3b-thinking
# nvidia/llama3-chatqa-1.5-8b
# nv-mistralai/mistral-nemo-12b-instruct
# google/gemma-3n-e4b-it
# nvidia/nemotron-nano-12b-v2-vl
# igenius/italia_10b_instruct_16k
# yentinglin/llama-3-taiwan-70b-instruct
# abacusai/dracarys-llama-3.1-70b-instruct
# openai/gpt-oss-120b
# mistralai/codestral-22b-instruct-v0.1
# qwen/qwen2.5-coder-7b-instruct
# minimaxai/minimax-m2.5
# meta/llama-3.2-90b-vision-instruct
# moonshotai/kimi-k2-instruct
# moonshotai/kimi-k2.5
# microsoft/phi-4-multimodal-instruct
# deepseek-ai/deepseek-v4-flash
# mistralai/mamba-codestral-7b-v0.1
# mistralai/mistral-large-3-675b-instruct-2512
# mistralai/mixtral-8x22b-instruct-v0.1
# speakleash/bielik-11b-v2.3-instruct
# qwen/qwen3-235b-a22b
# thudm/chatglm3-6b
# gotocompany/gemma-2-9b-cpt-sahabatai-instruct
# nvidia/llama-3.1-nemotron-nano-4b-v1.1
# google/shieldgemma-9b
# google/gemma-3-12b-it
# microsoft/phi-3-vision-128k-instruct
# meta/llama-3.2-3b-instruct
# rakuten/rakutenai-7b-instruct
# meta/llama-3.1-405b-instruct
# meta/llama3-8b-instruct
# mistralai/mistral-7b-instruct-v0.2
# meta/llama-3.2-1b-instruct
# meta/llama-guard-4-12b
# tokyotech-llm/llama-3-swallow-70b-instruct-v0.1
# minimaxai/minimax-m3
# meta/llama-4-scout-17b-16e-instruct
# deepseek-ai/deepseek-r1-distill-qwen-32b
# qwen/qwen3.5-122b-a10b
# qwen/qwen3.5-397b-a17b
# google/gemma-2-2b-it
# deepseek-ai/deepseek-r1-distill-qwen-14b
# mistralai/ministral-14b-instruct-2512
# mistralai/mistral-small-4-119b-2603
# deepseek-ai/deepseek-r1-0528
# meta/llama-3.1-70b-instruct
# igenius/colosseum_355b_instruct_16k
# deepseek-ai/deepseek-r1-distill-qwen-7b
# deepseek-ai/deepseek-v3.1-terminus
# google/gemma-4-31b-it
# upstage/solar-10.7b-instruct
# deepseek-ai/deepseek-r1
# rakuten/rakutenai-7b-chat
# microsoft/phi-3-medium-128k-instruct
# institute-of-science-tokyo/llama-3.1-swallow-70b-instruct-v0.1
# moonshotai/kimi-k2-thinking
# meta/llama-4-maverick-17b-128e-instruct
# nvidia/llama-3.1-nemoguard-8b-content-safety
# minimaxai/minimax-m2
# google/gemma-7b
# mistralai/mistral-nemotron
# mediatek/breeze-7b-instruct
# google/gemma-3-27b-it
# mistralai/mistral-7b-instruct-v0.3
# aisingapore/sea-lion-7b-instruct
# baichuan-inc/baichuan2-13b-chat
# tiiuae/falcon3-7b-instruct
# nvidia/llama-3.3-nemotron-super-49b-v1.5
# nvidia/nvidia-nemotron-nano-9b-v2
# microsoft/phi-3-small-8k-instruct
# google/codegemma-7b
# qwen/qwen3-next-80b-a3b-instruct
# meta/llama-3.3-70b-instruct
# microsoft/phi-4-mini-flash-reasoning
# minimaxai/minimax-m2.7
# mistralai/mathstral-7b-v0.1
# z-ai/glm5
# google/gemma-3n-e2b-it
# nvidia/llama-3.1-nemoguard-8b-topic-control
# microsoft/phi-3-small-128k-instruct
# mistralai/mistral-small-24b-instruct
# microsoft/phi-3-mini-4k-instruct
# marin/marin-8b-instruct
# institute-of-science-tokyo/llama-3.1-swallow-8b-instruct-v0.1
# openai/gpt-oss-20b
# qwen/qwen2-7b-instruct
# ibm/granite-3.3-8b-instruct
# deepseek-ai/deepseek-v4-pro
# mistralai/mixtral-8x22b-v0.1
# meta/llama-3.1-8b-instruct
# z-ai/glm-5.1
# nvidia/nvclip
# nvidia/nemotron-4-mini-hindi-4b-instruct
# qwen/qwen2.5-coder-32b-instruct
# nvidia/usdcode-llama-3.1-70b-instruct
# google/gemma-3-4b-it
# nvidia/llama-3.1-nemotron-70b-reward
# nvidia/llama-3.1-nemotron-ultra-253b-v1
# stepfun-ai/step-3.7-flash
# meta/llama3-70b-instruct
# deepseek-ai/deepseek-r1-distill-llama-8b
# microsoft/phi-3.5-mini-instruct
# google/gemma-2-9b-it
# microsoft/phi-3-medium-4k-instruct
# nvidia/llama-3.3-nemotron-super-49b-v1
# nvidia/riva-translate-4b-instruct
# nvidia/ising-calibration-1-35b-a3b
# 01-ai/yi-large
# nvidia/llama-3.1-nemotron-nano-vl-8b-v1
# microsoft/phi-3-mini-128k-instruct
# nvidia/nemotron-3-nano-30b-a3b
# microsoft/phi-4-mini-instruct
# qwen/qwen2.5-7b-instruct
# z-ai/glm4.7
# nvidia/nemotron-mini-4b-instruct
# moonshotai/kimi-k2.6
# microsoft/phi-3.5-vision-instruct
# deepseek-ai/deepseek-v3.1
# qwen/qwq-32b