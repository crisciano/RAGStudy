from langchain_community.vectorstores import Chroma
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import config

class RAGEngine:
    def __init__(self):
        # Reconecta ao banco vetorial existente
        self.embeddings = NVIDIAEmbeddings(
            model=config.EMBEDDING_MODEL, 
            nvidia_api_key=config.NVIDIA_API_KEY
        )
        self.vectorstore = Chroma(
            persist_directory=config.CHROMA_PATH, 
            embedding_function=self.embeddings
        )
        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4} # Returns the 4 most relevant chunks
        )
        
        # LLM NVIDIA
        self.llm = ChatNVIDIA(
            model=config.LLM_MODEL, 
            nvidia_api_key=config.NVIDIA_API_KEY,
            temperature=0.2 # Low temperature for precision in code/SQL
        )
        
        self.chain = self._create_chain()

    # Função auxiliar para extrair o texto dos chunks recuperados
    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def _create_chain(self):
        system_prompt = (
            "You are a technical assistant specializing in the system and its database.\n"
            "Use the provided context snippets to answer the question.\n"
            "If the question asks for a SQL query or example, extract or adapt one from the context.\n"
            "If you don't know the answer, clearly state that you could not find the information.\n\n"
            "Context:\n{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        
        # question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        # return create_retrieval_chain(self.retriever, question_answer_chain)

        # Modern LCEL pipeline (read left to right)
        # 1. Takes the input string, passes it through the retriever and extracts text (context)
        # 2. Keeps the input string intact
        # 3. Feeds into Prompt -> LLM -> Extracts final text only
        rag_chain = (
            {"context": self.retriever | self.format_docs, "input": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return rag_chain

    def ask(self, query: str) -> str:
        # response = self.chain.invoke({"input": query})
        # return response["answer"]
        # No LCEL, passamos a string diretamente para o invoke
        return self.chain.invoke(query)