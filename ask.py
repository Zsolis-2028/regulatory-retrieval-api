import json
import re

# Load chunks
chunks = []
with open("chunks.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        chunks.append(json.loads(line))

from fuzzywuzzy import fuzz

def search_top_k(query, k=3):
    scored = []

    for chunk in chunks:
        text = chunk["text"]
        score = fuzz.partial_ratio(query.lower(), text.lower())
        scored.append((score, chunk))

    # Sort by score, highest first
    scored.sort(reverse=True, key=lambda x: x[0])

    # Return top k chunks
    return scored[:k]

def summarize(chunks):
    combined = " ".join(chunk["text"] for _, chunk in chunks)
    combined = combined.replace("\n", " ")
    sentences = combined.split(".")
    summary = ". ".join(sentences[:3]).strip()
    return summary + "."

while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    results = search_top_k(question)

    print("\n--- Top Matches ---")
    for score, chunk in results:
        print(f"\nScore: {score}")
        print(chunk["text"])

    print("\n--- Summary ---")
    print(summarize(results))