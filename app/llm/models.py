from langchain_groq import ChatGroq
import os


ROUTER_LLM = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


SQL_LLM = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


ANALYTICS_LLM = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key=os.getenv("GROQ_API_KEY")
)


SUMMARY_LLM = ChatGroq(
    model="mixtral-8x7b-32768",
    api_key=os.getenv("GROQ_API_KEY")
)