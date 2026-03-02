# 🚀 AI Analyst CLI

A production-style CLI tool that helps analysts explore CSV datasets using AI.

Built to experiment with AI-assisted workflows, structured context building, and evaluation logging.

---

## 🔍 Problem

Analysts often spend time manually exploring datasets before generating insights.  
This tool streamlines that workflow using an AI-assisted CLI pipeline.

---

## ⚙️ Features

- 📊 Dataset summarization
- ❓ Natural language Q&A over CSV data
- 💡 Structured business insight generation
- 📝 Evaluation logging for observability
- 🐳 Docker-ready setup
- 🧱 Modular backend architecture

---

## 🏗 Architecture

User CLI Command  
→ Load CSV (Pandas)  
→ Generate Structured Summary  
→ Build Prompt Context  
→ LLM Call (OpenAI)  
→ Log Evaluation Metadata  
→ Print Result  

---

## 🖥 Example Usage

```bash
python main.py summarize sample.csv
python main.py ask sample.csv "Why did revenue drop in March?"
python main.py insights sample.csv
---

## 🧠 Engineering Focus

This project explores:

Context engineering for LLM workflows
Prompt structuring for analytical reasoning
Lightweight observability (evaluation logging)
Modular Python backend design
CLI-based internal AI tooling patterns


## 📁 **Project Structure**
ai-analyst-cli/
│
├── main.py
├── agent.py
├── data_loader.py
├── evaluator.py
├── sample.csv
├── .gitignore
└── README.md

##🚀 **Future Improvements**

Langfuse integration for advanced tracing
Multi-agent workflow orchestration
API layer with FastAPI
Cloud deployment
Structured output validation
