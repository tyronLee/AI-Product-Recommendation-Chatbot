from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_chroma import Chroma
from models import Models
import gradio as gr

models = Models()
embeddings = models.embeddings_ollama
llm = models.model_ollama

vector_store = Chroma(
    collection_name="langchain",
    embedding_function=embeddings,
    persist_directory="./db/chromadb",
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI sales assistant. Only recommend products that are in the database. If there is no product related to the question, do not answer the question and provide an apology instead. "),
        ("human", "Use the user question {input} to answer the question. Use only the {context} to answer the question.")
    ]
)

retriever = vector_store.as_retriever(kwargs={"k": 10})
combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

def main():
    while True:
        query = input("Enter your question or q to exit: ")
        if query.lower() in ["q", "exit"]:
            break

        result = retrieval_chain.invoke({"input": query})
        print("AI Assistant: ", result["answer"], "\n\n")

def invoke(input):
    result = retrieval_chain.invoke({"input": input})
    return result["answer"]


interface = gr.Interface(fn=invoke, inputs="text", outputs="text")
interface.launch()