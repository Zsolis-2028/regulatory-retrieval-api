from flask import Flask, request, jsonify
import json
import logging
from fuzzywuzzy import fuzz

# ---------------------------------------
# Logging Setup (Production‑Style)
# ---------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------------------------------
# Load chunks
# ---------------------------------------
chunks = []
with open("chunks.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        chunks.append(json.loads(line))

def search_top_k(query, k=3):
    scored = []
    for chunk in chunks:
        text = chunk["text"]
        score = fuzz.partial_ratio(query.lower(), text.lower())
        scored.append((score, chunk))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:k]

def summarize(chunks):
    combined = " ".join(chunk["text"] for _, chunk in chunks)
    combined = combined.replace("\n", " ")
    sentences = combined.split(".")
    summary = ". ".join(sentences[:3]).strip()
    return summary + "."

app = Flask(__name__)

# ---------------------------------------
# Main API Endpoint
# ---------------------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    logger.info(f"Received question: {question}")

    results = search_top_k(question)
    summary = summarize(results)

    logger.info(f"Summary generated for question: {question}")

    response = {
        "question": question,
        "summary": summary,
        "results": [
            {"score": score, "text": chunk["text"]}
            for score, chunk in results
        ]
    }

    return jsonify(response)

# ---------------------------------------
# Health Check Endpoint
# ---------------------------------------
@app.route("/health", methods=["GET"])
def health():
    logger.info("Health check pinged")
    return {"status": "ok"}, 200

# ---------------------------------------
# Run App
# ---------------------------------------
if __name__ == "__main__":
    logger.info("Starting Regulatory API service...")
    app.run(host="0.0.0.0", port=5000)