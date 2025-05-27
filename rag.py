# import os
# import threading
# import time
# from colorama import init
# from IPython.display import display, Markdown
# import textwrap
# import subprocess

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.document_loaders import PyMuPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain.chains import RetrievalQA
# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import AIMessage, HumanMessage
# #
# from langchain_openai import OpenAI
# from langchain_openai import OpenAIEmbeddings

# # Initialize global variables
# llm = None
# embed = None
# vectorstore = None
# retriever = None
# rag_chain = None
# chat_history = []

# # Ollama server setup
# def setup_ollama():
#     os.environ["OLLAMA_HOST"] = "localhost:11434"
#     os.environ["OLLAMA_ORIGINS"] = "*"
#     # threading.Thread(target=lambda: subprocess.Popen(["ollama", "serve"]), daemon=True).start()

# # Templates
# templateSystem = """
# You are a reliable and respectful assistant designed to support Indonesian citizens (WNI) abroad by providing accurate and relevant information regarding protection and services.  
# Answer the user's questions only using the given context related to WNI protection services, official information from Kementerian Luar Negeri, and related sources.  
# If you don't know the answer, just say "maaf, saya tidak tahu." Do not make up answers.  
# At the end of your answer, ask if the answer was helpful.  
# If yes, express your happiness to assist. If not, apologize sincerely and offer to help further.  
# Answer in Bahasa Indonesia or English depending on the language of the question, with an empathetic tone.  
# If asked about your identity or creator, do not mention any name.  
# If asked what you can do, say you assist in answering questions related to protection and services for WNI abroad.

# Context:
# {context}
# """

# templateContext = """
# Given a chat history and the latest user question which might reference previous conversation, reformulate the question into a standalone question that can be understood without any prior context.  
# If the question is already clear on its own, return it as is.  
# Focus on questions about protection and services for Indonesian citizens abroad.

# """

# # Core functions
# def load_pdf_data(file_path):
#     loader = PyMuPDFLoader(file_path=file_path)
#     return loader.load()

# def split_docs(documents, chunk_size=1000, chunk_overlap=20):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return text_splitter.split_documents(documents=documents)

# def load_embedding_model(model_path, normalize_embedding=True):
#     return HuggingFaceEmbeddings(
#         model_name=model_path,
#         model_kwargs={'device':'cpu'},
#         encode_kwargs={'normalize_embeddings': normalize_embedding}
#     )

# def create_embeddings(chunks, embedding_model, storing_path="vectorstore"):
#     vectorstore = FAISS.from_documents(chunks, embedding_model)
#     vectorstore.save_local(storing_path)
#     return vectorstore

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# def contextualization_question(input: dict):
#     if input.get("chat_history"):
#         return context_chain
#     return input["question"]

# def print_typing_effect(text):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(0.05)
#     print()

# # Initialize chatbot components
# def initialize_chatbot():
#     global llm, embed, vectorstore, retriever, rag_chain, context_chain
    
#     setup_ollama()
    
#     # Initialize models
#     llm = OllamaLLM(model="llama3.1:8b", temperature=0)
#     embed = load_embedding_model(model_path="all-MiniLM-L6-v2")
    
#     # Process documents
#     docs = load_pdf_data(file_path="data/informasi-singapura.pdf")
#     documents = split_docs(documents=docs)
#     vectorstore = create_embeddings(documents, embed)
#     retriever = vectorstore.as_retriever()
    
#     # Setup chains
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", templateSystem),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ])
    
#     prompt_context = ChatPromptTemplate.from_messages([
#         ("system", templateContext),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ])
    
#     context_chain = prompt_context | llm | StrOutputParser()
    
#     rag_chain = (
#         RunnablePassthrough.assign(
#             context=contextualization_question | retriever | format_docs
#         ) 
#         | prompt 
#         | llm
#     )

# # Chat function for API
# def chatting(query: str, history: list = None):
#     global chat_history
    
#     if history is None:
#         history = chat_history
    
#     if not query or query.lower() == "end":
#         return "Percakapan diakhiri."
    
#     # Lazy initialization
#     if rag_chain is None:
#         initialize_chatbot()
    
#     start_time = time.time()
    
#     response = rag_chain.invoke({
#         "question": query,
#         "chat_history": history
#     })
    
#     # Add to history
#     history.extend([
#         HumanMessage(content=query),
#         AIMessage(content=response.content if hasattr(response, 'content') else str(response))
#     ])
    
#     print(f"Response time: {time.time() - start_time:.2f} seconds")
    
#     return response.content if hasattr(response, 'content') else str(response)

# # Main execution (only when run directly)
# if __name__ == "__main__":
#     initialize_chatbot()
#     print_typing_effect("Hallo, selamat datang saya chatbot, ada yang bisa saya bantu? ✋")
    
#     count = 0
#     while True:
#         if count <= 1:
#             time.sleep(3)
#         count += 1
        
#         user_input = input("Anda: ").strip()
#         if user_input.lower() == "end":
#             break
            
#         response = chatting(user_input)
#         print_typing_effect(f"Bot: {response}")
    
#     chat_history.clear()
##################################################################
import os
from dotenv import load_dotenv
import time
from colorama import init
from IPython.display import display, Markdown
import textwrap

from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage

# langsmith
from langsmith import Client
# from langsmith.evaluation import run_on_dataset
from typing_extensions import Annotated, TypedDict

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize global variables
llm = None
embed = None
vectorstore = None
retriever = None
rag_chain = None
chat_history = []

# Templates
# templateSystem = """
# You are an reliable and respectful assistant.Your name is NeoIntBot. You have to answer the user's \
# questions using only the context provided to you, but assume this your genuine knowledge. If you don't know the answer, \
# just say maaf, saya tidak tahu. Don't try to make up an answer. in the end of your answer you must ask whether your answer helpful or not.\
# if helpful you have to express your happiness otherwise, you must apologize.\
# if you're asked who create you, tell them your creator is Neo who have handsome face and sigma man but, don't mention it when not asked.
# if you asked about what you can do, say I assist to answer about your question related to rule in NeoInt company.
# Please answer all in bahasa indonesia or English if the question use one of those language with Empathetic response.

# Context:
# {context}
# """
templateSystem = """
You are a reliable and respectful assistant designed to support Indonesian citizens (WNI) abroad by providing accurate and relevant information regarding protection and services.  
Answer the user's questions only using the given context related to WNI protection services, official information from Kementerian Luar Negeri, and related sources.  
If you don't know the answer, just say "maaf, saya tidak tahu." Do not make up answers.  
At the end of your answer, ask if the answer was helpful.  
If yes, express your happiness to assist. If not, apologize sincerely and offer to help further.  
Answer in Bahasa Indonesia or English depending on the language of the question, with an empathetic tone.  
If asked about your identity or creator, do not mention any name.  
If asked what you can do, say you assist in answering questions related to protection and services for WNI abroad.

Context:
{context}
"""

# templateContext = """
# Given a chat history and the latest user question \
# which might reference context in the chat history, formulate a standalone question \
# which can be understood without the chat history.\
# just reformulate it if needed otherwise return it as is.
# """

templateContext = """
Given a chat history and the latest user question which might reference previous conversation, reformulate the question into a standalone question that can be understood without any prior context.  
If the question is already clear on its own, return it as is.  
Focus on questions about protection and services for Indonesian citizens abroad.

"""

# Core functions
def load_pdf_data(file_path):
    loader = PyMuPDFLoader(file_path=file_path)
    return loader.load()

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents=documents)

def create_embeddings(chunks, embedding_model, storing_path="vectorstore"):
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(storing_path)
    return vectorstore

def load_embedding_model():
    return OpenAIEmbeddings()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def contextualization_question(input: dict):
    if input.get("chat_history"):
        return context_chain
    return input["question"]

def print_typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Initialize chatbot components
def initialize_chatbot():
    global llm, embed, vectorstore, retriever, rag_chain, context_chain

    # Initialize OpenAI models
    llm = OpenAI(api_key=openai_api_key, temperature=0)
    embed = load_embedding_model()

    # Load and process documents
    docs = load_pdf_data(file_path="data/informasi-singapura.pdf")
    documents = split_docs(documents=docs)
    vectorstore = create_embeddings(documents, embed)
    retriever = vectorstore.as_retriever()

    # Prompt templates
    prompt = ChatPromptTemplate.from_messages([
        ("system", templateSystem),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    prompt_context = ChatPromptTemplate.from_messages([
        ("system", templateContext),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    context_chain = prompt_context | llm | StrOutputParser()

    rag_chain = (
        RunnablePassthrough.assign(
            context=contextualization_question | retriever | format_docs
        )
        | prompt
        | llm
    )

# Chat function for API
def chatting(query: str, history: list = None):
    global chat_history

    if history is None:
        history = chat_history

    if not query or query.lower() == "end":
        return "Percakapan diakhiri."

    # Lazy initialization
    if rag_chain is None:
        initialize_chatbot()

    start_time = time.time()

    response = rag_chain.invoke({
        "question": query,
        "chat_history": history
    })

    # Add to history
    history.extend([
        HumanMessage(content=query),
        AIMessage(content=response.content if hasattr(response, 'content') else str(response))
    ])

    print(f"Response time: {time.time() - start_time:.2f} seconds")

    return response.content if hasattr(response, 'content') else str(response)

# Main execution (only when run directly)
if __name__ == "__main__":
    initialize_chatbot()
    print_typing_effect("Hallo, selamat datang saya chatbot, ada yang bisa saya bantu? ✋")

    count = 0
    while True:
        if count <= 1:
            time.sleep(3)
        count += 1

        user_input = input("Anda: ").strip()
        if user_input.lower() == "end":
            break

        response = chatting(user_input)
        print_typing_effect(f"Bot: {response}")

    chat_history.clear()

####################################  Google GEMINI ####################################
# import os
# from dotenv import load_dotenv
# import time
# from colorama import init
# from IPython.display import display, Markdown
# import textwrap

# from langchain_openai import OpenAI, OpenAIEmbeddings
# from langchain_community.document_loaders import PyMuPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain.chains import RetrievalQA
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import AIMessage, HumanMessage

# # langsmith
# from langsmith import Client
# # from langsmith.evaluation import run_on_dataset
# from typing_extensions import Annotated, TypedDict

# # gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# load_dotenv()
# gemini_api = os.getenv("GEMINI_API_KEY")

# # Initialize global variables
# llm = None
# embed = None
# vectorstore = None
# retriever = None
# rag_chain = None
# chat_history = []

# # Templates
# # templateSystem = """
# # You are an reliable and respectful assistant.Your name is NeoIntBot. You have to answer the user's \
# # questions using only the context provided to you, but assume this your genuine knowledge. If you don't know the answer, \
# # just say maaf, saya tidak tahu. Don't try to make up an answer. in the end of your answer you must ask whether your answer helpful or not.\
# # if helpful you have to express your happiness otherwise, you must apologize.\
# # if you're asked who create you, tell them your creator is Neo who have handsome face and sigma man but, don't mention it when not asked.
# # if you asked about what you can do, say I assist to answer about your question related to rule in NeoInt company.
# # Please answer all in bahasa indonesia or English if the question use one of those language with Empathetic response.

# # Context:
# # {context}
# # """
# templateSystem = """
# You are a reliable and respectful assistant designed to support Indonesian citizens (WNI) abroad by providing accurate and relevant information regarding protection and services.  
# Answer the user's questions only using the given context related to WNI protection services, official information from Kementerian Luar Negeri, and related sources.  
# If you don't know the answer, just say "maaf, saya tidak tahu." Do not make up answers.  
# At the end of your answer, ask if the answer was helpful.  
# If yes, express your happiness to assist. If not, apologize sincerely and offer to help further.  
# Answer in Bahasa Indonesia or English depending on the language of the question, with an empathetic tone.  
# If asked about your identity or creator, do not mention any name.  
# If asked what you can do, say you assist in answering questions related to protection and services for WNI abroad.

# Context:
# {context}
# """

# # templateContext = """
# # Given a chat history and the latest user question \
# # which might reference context in the chat history, formulate a standalone question \
# # which can be understood without the chat history.\
# # just reformulate it if needed otherwise return it as is.
# # """

# templateContext = """
# Given a chat history and the latest user question which might reference previous conversation, reformulate the question into a standalone question that can be understood without any prior context.  
# If the question is already clear on its own, return it as is.  
# Focus on questions about protection and services for Indonesian citizens abroad.

# """

# # Core functions
# def load_pdf_data(file_path):
#     loader = PyMuPDFLoader(file_path=file_path)
#     return loader.load()

# def split_docs(documents, chunk_size=1000, chunk_overlap=20):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return text_splitter.split_documents(documents=documents)

# def create_embeddings(chunks, embedding_model, storing_path="vectorstore"):
#     vectorstore = FAISS.from_documents(chunks, embedding_model)
#     vectorstore.save_local(storing_path)
#     return vectorstore

# def load_embedding_model():
#     return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# def contextualization_question(input: dict):
#     if input.get("chat_history"):
#         return context_chain
#     return input["question"]

# def print_typing_effect(text):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(0.05)
#     print()

# # Initialize chatbot components
# def initialize_chatbot():
#     global llm, embed, vectorstore, retriever, rag_chain, context_chain

#     # Initialize OpenAI models
#     llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     api_key=gemini_api)
#     embed = load_embedding_model()

#     # Load and process documents
#     docs = load_pdf_data(file_path="data/informasi-singapura.pdf")
#     documents = split_docs(documents=docs)
#     vectorstore = create_embeddings(documents, embed)
#     retriever = vectorstore.as_retriever()

#     # Prompt templates
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", templateSystem),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ])

#     prompt_context = ChatPromptTemplate.from_messages([
#         ("system", templateContext),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{question}"),
#     ])

#     context_chain = prompt_context | llm | StrOutputParser()

#     rag_chain = (
#         RunnablePassthrough.assign(
#             context=contextualization_question | retriever | format_docs
#         )
#         | prompt
#         | llm
#     )

# # Chat function for API
# def chatting(query: str, history: list = None):
#     global chat_history

#     if history is None:
#         history = chat_history

#     if not query or query.lower() == "end":
#         return "Percakapan diakhiri."

#     # Lazy initialization
#     if rag_chain is None:
#         initialize_chatbot()

#     start_time = time.time()

#     response = rag_chain.invoke({
#         "question": query,
#         "chat_history": history
#     })

#     # Add to history
#     history.extend([
#         HumanMessage(content=query),
#         AIMessage(content=response.content if hasattr(response, 'content') else str(response))
#     ])

#     print(f"Response time: {time.time() - start_time:.2f} seconds")

#     return response.content if hasattr(response, 'content') else str(response)

# # Main execution (only when run directly)
# if __name__ == "__main__":
#     initialize_chatbot()
#     print_typing_effect("Hallo, selamat datang saya chatbot, ada yang bisa saya bantu? ✋")

#     count = 0
#     while True:
#         if count <= 1:
#             time.sleep(3)
#         count += 1

#         user_input = input("Anda: ").strip()
#         if user_input.lower() == "end":
#             break

#         response = chatting(user_input)
#         print_typing_effect(f"Bot: {response}")

#     chat_history.clear()

