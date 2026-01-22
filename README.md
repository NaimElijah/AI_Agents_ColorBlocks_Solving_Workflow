# 🧠 AI Agents Color Blocks Problem Solving Workflow

> A modular **Agentic AI system** that solves *Color Blocks planning problems* by orchestrating multiple intelligent agents, heuristic search, and a graph-based workflow powered by local LLMs.

---

## 🚀 Project Overview

This project demonstrates a **real agentic AI architecture**, combining:

* **LLM-powered reasoning agents**
* **Classical heuristic search algorithms**
* **A manager–worker agent workflow**
* **Tool-calling vs self-reasoning agent strategies**
* **Graph-based execution using LangGraph**

The system is designed to solve **Color Blocks problems**, where each problem consists of:

* An **initial configuration** of colored blocks
* A **goal configuration**
* A requirement to find a valid sequence of actions that transforms the initial state into the goal state

---

## 🏗️ System Architecture

```
┌────────────────────┐
│   Manager Agent    │
│  (Decision Maker)  │
└─────────┬──────────┘
          │
          ▼
┌─────────────────────────────┐
│       Agent Graph           │
│   (LangGraph Workflow)      │
└─────────┬─────────┬─────────┘
          │         │
          ▼         ▼
┌────────────────┐  ┌────────────────────┐
│ Self-Solver     │  │ Tool-Solver Agent  │
│ Agent (LLM)     │  │ (Search + Heuristic)│
└────────────────┘  └────────────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Heuristic Search   │
                    │ (State Space)      │
                    └────────────────────┘
```

---

## 🤖 Agents Explained

### 🧠 Manager Agent

* Oversees the entire workflow
* Decides **how** a problem should be solved
* Routes execution between agents

### 🧩 Self-Solver Agent

* Attempts to solve the problem **purely through reasoning**
* Uses the LLM without external tools
* Useful for small or simple problem instances

### 🛠️ Tool-Solver Agent

* Uses **heuristic search algorithms**
* Delegates planning to symbolic solvers
* Ideal for complex or large state spaces

---

## 🔍 Heuristic Search Engine

The project includes a **fully implemented classical planning engine**:

* Explicit **state representation**
* Expandable **search nodes**
* Pluggable **heuristics**
* Clean separation between:

  * State
  * Actions
  * Cost
  * Evaluation

This makes the system:

* Easy to extend
* Easy to benchmark
* Easy to compare against LLM-only reasoning

---

## 🧠 Graph-Based Execution (LangGraph)

The agent workflow is defined as a **directed execution graph**, allowing:

* Deterministic control flow
* Clear agent transitions
* Debuggable reasoning paths
* Easy extension with new agents

This mirrors **production-grade agent pipelines**.

---

## 🗂️ Project Structure

```
AI_Agents_ColorBlocks_Solving_Workflow/
│
├── agents/
│   ├── agent_base.py
│   ├── manager_agent.py
│   ├── self_solver_agent.py
│   └── tool_solver_agent.py
│
├── graph/
│   └── agent_graph.py
│
├── heuristic_search/
│   ├── color_blocks_state.py
│   ├── heuristics.py
│   ├── search.py
│   ├── search_node.py
│   └── simple_test.py
│
├── llm/
│   └── llm_client.py
│
├── states/
│   └── state1.py (can add more if wanted for different implementations)
|
├── tools/
│   └── color_blocks_tool.py
|
├── config.py
└── main.py
```

---

## ⚙️ Prerequisites
### Can install a Local LLM with Ollama

This project can run locally with **Ollama**.

**Download Ollama:**  
https://ollama.com/

Once installed, you can pull any model you want to run.  
Below are a few recommended examples, but you are free to pick any size or model from the Ollama library.

```bash
ollama pull qwen3:0.6b
```

or

```bash
ollama pull ibm/granite4:350m
```

or

Choose any model you prefer, make sure the model supports tools.
Browse available models here:
https://ollama.com/library
You may use **any model** that supports tool calling.

---

### 🐍 Python Dependencies

```bash
pip install langgraph langchain-google-genai langchain-core mcp langchain-ollama
```

---

## ▶️ Running the Project

```bash
python main.py
```

The system will:

1. Load Color Blocks problems to both agents
2. Initialize the agent graph
3. each agent will decide on a solving strategy with a different approach(self solver and provided tool user)
4. Execute the solution workflow
5. Print reasoning and results
6. Manager agent will compare solutions of both agents

---

## 🧠 Key Concepts Demonstrated

* Agentic AI systems
* LLM tool usage
* Planning vs Reasoning
* Graph-based workflows
* Modular AI system design

---

## 🧩 Extending the System

You can easily:

* Add new agents
* Plug in new heuristics
* Replace the search algorithm
* Swap LLM models
* Add memory or reflection agents

This project is designed as a **foundation**, not a toy.

---

## 📜 License

This project was created for Portfolio and Educational Purposes.
