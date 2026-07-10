from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


USERS = {
    "demo": User(
        username="demo",
        password="password123",
    )
}


def authenticate_user(username: str, password: str) -> User | None:
    user = USERS.get(username)

    if user is None:
        return None

    if user.password != password:
        return None

    return user


def create_token(username: str) -> str:
    return f"demo-token:{username}"

def decode_token(token: str) -> str:
    prefix, username = token.split("|", maxsplit=1)

    if prefix != "demo-token":
        raise ValueError("Invalid token prefix")

    if not username:
        raise ValueError("Token username is missing")

    return username