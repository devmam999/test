import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.auth import authenticate_user, create_token

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger("demo-auth-api")

app = FastAPI(
    title="Demo Authentication API",
    description="A small API used to demonstrate SentinelAI incident analysis.",
    version="1.0.0",
)


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "demo-auth-api",
    }


@app.post("/login")
def login(credentials: LoginRequest) -> dict[str, str]:
    user = authenticate_user(
        credentials.username,
        credentials.password,
    )

    if user is None:
        logger.warning(
            "login_failed username=%s reason=invalid_credentials",
            credentials.username,
        )
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    logger.info("login_success username=%s", user.username)

    return {
        "access_token": create_token(user.username),
        "token_type": "bearer",
    }