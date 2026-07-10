# Demo Authentication API

A small FastAPI authentication service used to demonstrate SentinelAI.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload