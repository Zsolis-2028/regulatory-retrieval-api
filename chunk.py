import json

input_path = "regulation_clean.txt"
output_path = "chunks.jsonl"

CHUNK_SIZE = 800  # characters per chunk

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

chunks = []
start = 0

while start < len(text):
    end = start + CHUNK_SIZE
    chunk = text[start:end].strip()
    chunks.append(chunk)
    start = end

with open(output_path, "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        record = {
            "id": f"chunk_{i}",
            "text": chunk
        }
        f.write(json.dumps(record) + "\n")

print(f"Created {len(chunks)} chunks in chunks.jsonl")