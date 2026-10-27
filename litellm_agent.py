from litellm import completion
from tools_manager import execute_tool
from ai_system_role import display_select_ai_roles
from process_embeddings import create_dataset_embeddings, cosine_similiarity, create_embeddings


from config import (
    BASE_URL as ai_base_url,
    API_KEY as ai_api_key,
    MODEL as ai_model,
    BRAVE_SEARCH_MCP_URL as brave_mcp_url,
)
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
# Creat the dataset emedding first
RAG_embeddings = create_dataset_embeddings()
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

    user_text_embedding = create_embeddings(user_text)
    similiarity = -1
    matching_file = ''
    print(type(RAG_embeddings))
    for file_name, vector in RAG_embeddings.items():
        similiarity_value = cosine_similiarity(user_text_embedding, vector)
        if similiarity_value > similiarity:
            matching_file = file_name
    print(f"Matching file from RAG Dataset is {matching_file}")
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
    