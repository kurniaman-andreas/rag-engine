
import os
import time
from dotenv import load_dotenv
from langdetect import detect
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Global variables
llm = None
embed = None
vectorstore = None
retriever = None
prompt = None
context_chain = None
chat_history = []

# Detect language
def detect_language(question):
    try:
        lang = detect(question)
        return "English" if lang == "en" else "Bahasa Indonesia"
    except:
        return "Bahasa Indonesia"

# Prompt templates
templateSystem = """
You are a reliable and respectful assistant designed to support Indonesian citizens (WNI) abroad by providing accurate and relevant information regarding protection and services.  
- Answer the user's questions only using context provided to you, but assume this your genuine knowledge about services and protection for WNI in Singapore.
- If you don't know the answer, just say "maaf, saya tidak tahu/sorry, I don’t know and suggest the user to contact the Indonesian Embassy in Singapore and provide its address and phone number Alamat KBRI Singapura: 7 Chatsworth Rd, Singapore 247671 and contact KBRI Singapura: +65 6737 7422"   
- The user's question is in {language}, you must answer in {language}, with an empathetic tone. 
- At the end of your answer, ask if the answer was helpful.  If yes, express your happiness to assist. If not, apologize sincerely and offer to help further.
- If asked about your identity or creator, do not mention any name.  
- If asked what you can do, say you assist in answering questions related to protection and services for WNI in Singapore.
- If there are important numbers, procedures, addresses, or documents mentioned in context, list them in full.
Context:
{context}
"""

templateContext = """
Given a chat history and the latest user question which might reference previous conversation, reformulate the question into a standalone question that can be understood without any prior context.
If the question is already clear on its own, return it as is.
Focus on questions about protection and services for Indonesian citizens abroad.
"""


def load_embedding_model():
    return OpenAIEmbeddings()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def contextualization_question(input: dict):
    if input.get("chat_history"):
        return context_chain.invoke(input)
    return input["question"]

def print_typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Initialization
def initialize_chatbot():
    global llm, embed, vectorstore, retriever, prompt, context_chain

    llm = OpenAI(api_key=openai_api_key, temperature=0)
    embed = load_embedding_model()

    # Load vectorstore_openai
    vectorstore = FAISS.load_local("vectorstore_openai", embed, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()

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

    global context_chain
    context_chain = prompt_context | llm | StrOutputParser()

# Chat function
def chatting(query: str, history: list = None):
    global chat_history, retriever, prompt, llm

    if history is None:
        history = chat_history

    if not query or query.lower() == "end":
        return "Percakapan diakhiri."

    if llm is None or prompt is None:
        initialize_chatbot()

    detected_lang = detect_language(query)
    full_prompt = prompt.partial(language=detected_lang)

    rag_chain_local = (
        RunnablePassthrough.assign(
            context=contextualization_question | retriever | format_docs
        )
        | full_prompt
        | llm
    )

    start_time = time.time()
    response = rag_chain_local.invoke({
        "question": query,
        "chat_history": history
    })
    print(f"Response time: {time.time() - start_time:.2f} seconds")

    history.extend([
        HumanMessage(content=query),
        AIMessage(content=response.content if hasattr(response, 'content') else str(response))
    ])

    return response.content if hasattr(response, 'content') else str(response)

# CLI interface
if __name__ == "__main__":
    initialize_chatbot()
    print_typing_effect("Hallo, selamat datang saya chatbot, ada yang bisa saya bantu? ✋")

    count = 0
    while True:
        if count <= 1:
            time.sleep(2)
        count += 1

        user_input = input("Anda: ").strip()
        if user_input.lower() == "end":
            break

        response = chatting(user_input)
        print_typing_effect(f"Bot: {response}")

    chat_history.clear()

