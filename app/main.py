from fastapi import FastAPI

app = FastAPI(
    title="Demo Authentication API",
    description="A small API used to demonstrate SentinelAI incident analysis.",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "demo-auth-api",
    }