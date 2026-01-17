## Prerequisites
### Install a Local LLM with Ollama

To run this project locally, we will install and use **Ollama**, a lightweight runtime for local large language models.

**Download Ollama:**  
https://ollama.com/

Once installed, you can pull any model you want to run.  
Below are a few recommended examples, but you are free to pick any size or model from the Ollama library.

ollama pull qwen3:0.6b

or

ollama pull ibm/granite4:350m

or

Choose any model you prefer, make sure the model supports tools.
Browse available models here:
https://ollama.com/library

### Python requirements
```bash
!pip install langgraph langchain-google-genai langchain-core mcp langchain-ollama
```

