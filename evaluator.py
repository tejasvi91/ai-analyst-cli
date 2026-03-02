import json
from datetime import datetime


def log_evaluation(prompt: str, answer: str):
    log_entry = {
        "timestamp": str(datetime.now()),
        "prompt_length": len(prompt),
        "response_length": len(answer)
    }

    with open("evaluation_log.json", "a") as f:
        json.dump(log_entry, f)
        f.write("\n")