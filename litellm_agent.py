from litellm import completion
from dotenv import load_dotenv  
import os
from tools_manager import execute_tool
from ai_system_role import display_select_ai_roles

load_dotenv()
# Setting the LLM parameters 
ai_base_url=os.getenv("BASE_URL")
ai_api_key=os.getenv("API_KEY")
ai_model=os.getenv("MODEL") or "qwen3.5"
brave_mcp_url = os.getenv("BRAVE_SEARCH_MCP_URL")
if not ai_model:
    raise ValueError("Set the MODEL environment variable to a model name.")
#MCP tools section
search_tools=[
        {
            "type": "mcp",
            "server_label": "brave_search",
            "server_url": brave_mcp_url,
            "require_approval": "never",
            "allowed_tools": ["brave_web_search"],
        }
    ]
# Give user the option to select system prompt.
system_prompt = display_select_ai_roles()

chat_context = [
    {
    "role": "system",
    "content": system_prompt             
     }
]
banner = f"{'=' * 40} \nAI Assitant\n{'=' * 40} \n"
print(banner)

exit_list = ["q", "quit", "exit", "bye"]

while True:
    user_text = input("Hi!, how can I help: ").strip()
    if user_text.lower() in exit_list:
        break
    tool_result = execute_tool(user_text)
    if tool_result:
        print(f"User Tool: {tool_result}")
        continue
    chat_context.append(
        {
        "role": "user",
        "content": user_text,
        }
    ) 
    response = completion(
        model=ai_model,
        api_key=ai_api_key,
        api_base=ai_base_url,
        messages= chat_context,
        extra_body={"tools": search_tools,
                    "tool_choice": "auto",},
            
    )
    ai_response = response.choices[0].message.content
    print(f"Assistant: {ai_response}")

    chat_context.append(
        {
        "role": "assistant",
        "content": ai_response
        }
    )
    # Code snippet to print full conversation history.
    # print(f"{'=' * 20}Conversation History{'=' * 20}")
    # for chat in chat_context:
    #     print(f"Role: {chat['role'].title()}\nContent: {chat['content']}")
    # print(f"{'=' * 60}")
    