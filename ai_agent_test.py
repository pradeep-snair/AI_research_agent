from openai import OpenAI
from dotenv import load_dotenv  
import os, sys

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
    ) 
tools=[
        {
            "type": "mcp",
            "server_label": "web_search",
            "server_url": "https://ai-hub-lite.msc.rokulabs.net/mcp",
            "require_approval": "never",
        }
    ],
extra_headers={
        "x-mcp-servers": "web_search"
    }

ai_model=os.getenv("MODEL") or "qwen3.5"
if not ai_model:
    raise ValueError("Set the MODEL environment variable to a model name.")

exit_list = ["q", "quit", "exit", "bye"]
while True:
    user_input = input("Hi!, how can I help: ")
    if user_input.lower() in exit_list:
        sys.exit() 
    response = client.chat.completions.create(
        model=ai_model,
        messages=[ 
            {
                "role" : "user",
                "content" : user_input  
            }
        ]
    )
    print(response.choices[0].message.content)