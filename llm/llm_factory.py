import os
import config
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

# class LLMFactory:       #  can be used for modularity if needed
#     def __init__(self, model_name: str, temperature: float = 0.0):
#         self.model_name = model_name
#         self.temperature = temperature

#     def create_llm(self):
#         if "gemini" in self.model_name:
#             return ChatGoogleGenerativeAI(model=self.model_name, temperature=self.temperature)
#         else:
#             return ChatOllama(model=self.model_name, temperature=self.temperature)
        

# class LLMWrapper:       #  can be used for modularity if needed
#     def __init__(self, llm):
#         self.llm = llm

#     def bind_tools(self, tools):
#         # Here you would implement the logic to bind tools to the LLM
#         # This is a placeholder implementation
#         self.tools = tools
#         return self
    
#     def __getattr__(self, name):
#         return getattr(self.llm, name)



# Choose your model here, can be Ollama or Google Gemini. Can also switch between different model sizes as needed.
# model = "gemini-2.5-flash"
# model = "gemini-2.5-flash-lite"
# global_llm = ChatGoogleGenerativeAI(model=model, temperature=0)
# SETUP API KEY if using Google Gemini
# os.environ["GOOGLE_API_KEY"] = config.llm_api_key

global_llm = ChatOllama(model=config.llm_model, temperature=config.llm_temperature)   # can be Ollama or Google Gemini or ...

def get_llm():
    return global_llm

def get_llm_with_tools(tools):
    return get_llm().bind_tools(tools)
