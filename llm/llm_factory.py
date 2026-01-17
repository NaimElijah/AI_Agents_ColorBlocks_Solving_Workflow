import os
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

# Choose your model here, can be Ollama or Google Gemini. Can also switch between different model sizes as needed.
# model = "gemini-2.5-flash"
# model = "gemini-2.5-flash-lite"
# global_llm = ChatGoogleGenerativeAI(model=model, temperature=0)
# model = "qwen3:0.6b"                                    # model name
model = "ibm/granite4:350m"                               # model name
global_llm = ChatOllama(model=model, temperature=0.0)   # can be Ollama or Google Gemini or ...

# SETUP API KEY if using Google Gemini
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key   # SETUP API KEY if using Google Gemini


def get_llm():
    return global_llm

def get_llm_with_tools(tools):
    return get_llm().bind_tools(tools)
