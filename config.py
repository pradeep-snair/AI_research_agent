"""Shared project settings loaded from the root .env file."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
# Existing environment variables take precedence over .env values.
load_dotenv(PROJECT_ROOT / ".env")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


BASE_URL = require_env("BASE_URL")
API_KEY = require_env("API_KEY")
EMBEDDING_MODEL = require_env("EMBEDDING_MODEL")
DATA_FOLDER_PATH = Path(require_env("DATA_FOLDER_PATH"))
if not DATA_FOLDER_PATH.is_absolute():
    DATA_FOLDER_PATH = PROJECT_ROOT / DATA_FOLDER_PATH

MODEL = os.getenv("MODEL") or "qwen3.5"
BRAVE_SEARCH_MCP_URL = os.getenv("BRAVE_SEARCH_MCP_URL")
