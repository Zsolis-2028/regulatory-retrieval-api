# regulatory‑retrieval‑api  
A lightweight retrieval API that ingests a regulation, cleans it, chunks it, and serves it through a simple question‑answering endpoint. Built to be fast, transparent, and easy to run — whether you’re testing locally or spinning it up in Docker.

---

## What this project does (in plain English)
This API takes a regulation PDF, turns it into clean text, breaks it into chunks, and lets you ask questions about it.  
It’s basically a tiny retrieval system you can run anywhere — no mystery, no magic, just clean Python and a simple workflow.

You can:

- extract text from a regulation  
- clean and normalize it  
- chunk it into structured JSON  
- load it into the API  
- ask questions and get relevant chunks back  
- run everything in Docker with one command  

---

## Tech Stack
- Python  
- Docker  
- JSONL  
- Local text processing  
- Standard libraries only  

---

## Project Structure
```
regulatory-mvp/
│
├── api.py                 # The API server
├── ask.py                 # Query script for local testing
├── chunk.py               # Chunking logic
├── clean.py               # Text cleaning
├── extract.py             # PDF → text extraction
├── download.py            # Optional downloader
├── chunks.jsonl           # Final chunked dataset
│
├── regulation.pdf         # Source document
├── regulation.txt         # Raw extracted text
├── regulation_clean.txt   # Cleaned text
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── screenshots/           # Proof of the system running
```

---

## How to run it locally
```
python extract.py
python clean.py
python chunk.py
python api.py
```

Then open:

```
http://localhost:8000/ask?question=Your+question+here
```

---

## How to run it in Docker
```
docker-compose up --build
```

---

## Screenshots
Screenshots live in the `screenshots/` folder and show:

- container running  
- API responding  
- health check  
- dashboard + logs  
- compose setup  

---

## Why I built this
I wanted a small, clean retrieval pipeline I could run anywhere — something that shows:

- I understand end‑to‑end data flow  
- I can containerize and deploy an API  
- I can build tools that are actually useful  
- I can document and structure a project like an engineer  

---

## Future improvements
- Add embeddings + vector search  
- Add FastAPI docs UI  
- Add metadata to chunks  
- Add a frontend  
- Deploy to a cloud container service  
