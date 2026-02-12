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
