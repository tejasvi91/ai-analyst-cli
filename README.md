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
