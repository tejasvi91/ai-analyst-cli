import os
from openai import OpenAI
from dotenv import load_dotenv
from data_loader import load_csv, get_basic_summary
from evaluator import log_evaluation

load_dotenv()
client = OpenAI()


def summarize_data(file_path: str):
    #df = load_csv(file_path)
    try:
       df = load_csv(file_path)
    except Exception as e:
       print(f"Error loading file: {e}")
       return
    summary = get_basic_summary(df)

    prompt = f"""
You are a professional data analyst.

Analyze this dataset summary and provide:
1. Key observations
2. Any anomalies
3. Business insights

Dataset Summary:
{summary}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content

    print("\n=== AI SUMMARY ===\n")
    print(answer)

    log_evaluation(prompt, answer)


def ask_question(file_path: str, question: str):
    #df = load_csv(file_path)
    try:
       df = load_csv(file_path)
    except Exception as e:
       print(f"Error loading file: {e}")
       return
    summary = get_basic_summary(df)

    prompt = f"""
Dataset Summary:
{summary}

Answer this question clearly and concisely:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content

    print("\n=== AI ANSWER ===\n")
    print(answer)

    log_evaluation(prompt, answer)


def generate_insights(file_path: str):
    df = load_csv(file_path)
    summary = get_basic_summary(df)

    prompt = f"""
You are a business intelligence assistant.

From this dataset summary, generate 5 structured business insights.
Each insight must include reasoning.

Dataset:
{summary}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content

    print("\n=== AI INSIGHTS ===\n")
    print(answer)

    log_evaluation(prompt, answer)