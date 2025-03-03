from  langchain_ollama import OllamaEmbeddings, ChatOllama
import ollama

class Models:
    def __init__(self):
        self.embeddings_ollama = OllamaEmbeddings(
            model="nomic-embed-text"
        )
        self.model_ollama = ChatOllama(
            model="llama3.1:latest",
            temperature=0,
        )

    def load_models(self):
        # Initialize embeddings and model using OLLAMA
        self.embeddings_ollama = OllamaEmbeddings(model='nomic-embed-text')
        self.model_ollama = lambda prompt: ollama.chat(prompt, model="llama3.1")

