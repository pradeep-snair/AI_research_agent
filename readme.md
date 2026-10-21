# AI Research Agent

A Python terminal assistant built with LiteLLM, featuring session-based chat history,
local utility tools, and a Brave Search MCP configuration for compatible backends.

## Features

- Chat with a language model using a configurable endpoint.
- Get the local time, roll a six-sided die, or generate a 12-character password.
- Retain chat context until the application exits.
- Request web search through a compatible Brave Search MCP server and model backend.

## Folder structure

```text
AI_research_agent/
├── .gitignore              # Excludes .env
├── ai_system_role.py       # Empty placeholder
├── litellm_agent.py        # Chat loop and model/MCP configuration
├── tools.py                # Time, dice, and password utilities
├── tools_manager.py        # Keyword-based local tool routing
├── test_tools_manager.py   # Manual tool smoke test
└── readme.md
```

Local-only files: `.env` (credentials), `.venv/` (environment), and `__pycache__/`.

## Setup

Requires Python 3, pip, and access to a compatible model backend.

```sh
git clone https://github.com/pradeep-snair/AI_research_agent.git
cd AI_research_agent
python3 -m venv .venv
source .venv/bin/activate
python -m pip install litellm python-dotenv
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

Create `.env` in the project root and replace these placeholders:

```dotenv
API_KEY=your-model-api-key
MODEL=provider/model-name
BASE_URL=https://your-model-endpoint.example/v1
BRAVE_SEARCH_MCP_URL=https://your-mcp-server.example/mcp
```

Use the model identifier required by your backend and LiteLLM configuration.
`MODEL` defaults to `qwen3.5` if unset. Web search requires a reachable MCP server
and a backend that accepts the supplied MCP tool format.

## Usage

```sh
python litellm_agent.py
```

Try `What is the time?`, `Roll dice`, `Generate a password`, or a general question.
Enter `q`, `quit`, `exit`, or `bye` to stop.

Local tools use keyword matching and run without a model request. Other prompts
are sent to the configured model with the current chat history.

## Testing

```sh
python test_tools_manager.py
```

Prints a timestamp, password, and dice result. This is a manual smoke test without
assertions; it does not validate model or MCP connectivity.

## Limitations

- Chat history is not saved; local tool interactions are excluded from it.
- Keyword matching can trigger tools for unintended prompts.
- Model/network errors are not handled, and MCP configuration is always sent.
- Search uses `require_approval="never"`; the app has no custom tool execution loop.
- Generated passwords are displayed in the terminal.

## Before publishing

Keep credentials out of Git. `.env` is already ignored; also add `.venv/`,
`__pycache__/`, and `*.py[cod]` to `.gitignore`. Review staged files and Git history
for secrets before making the repository public.

No license is included yet. Add a `LICENSE` file to specify reuse terms.
