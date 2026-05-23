from dotenv import load_dotenv
load_dotenv()

#from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(
#     model="gpt-4.1-mini",
#     temperature=0
# )

# from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="tinyllama"      #"llama3"
# )
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="YOUR_GROQ_API_KEY"
)