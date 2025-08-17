from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from repo root by default
def load_env(dotenv_path: str | None = None) -> None:
    if dotenv_path is None:
        dotenv_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path=dotenv_path)

def get(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)
