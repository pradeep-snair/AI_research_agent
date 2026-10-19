from litellm import completion
import os
from dotenv import load_dotenv  
import os, sys

load_dotenv()
# Setting the LLM parameters 
ai_base_url=os.getenv("BASE_URL")
ai_api_key=os.getenv("API_KEY")
ai_model=os.getenv("MODEL") or "qwen3.5"
if not ai_model:
    raise ValueError("Set the MODEL environment variable to a model name.")

chat_context = [
    {
    "role": "system",
     "content": "You are a helpful assistant. \
                Remember relevant details from this conversation. \
                Explain concepts clearly with real life examples."                 
     }
]
banner = f"{'=' * 40} \nAI Assitant\n{'=' * 40} \n"
print(banner)

exit_list = ["q", "quit", "exit", "bye"]

while True:
    user_text = input("Hi!, how can I help: ").strip()
    if user_text.lower() in exit_list:
        break
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
        messages= chat_context 
            
    )
    ai_response = response.choices[0].message.content
    print(f"\nAssistant: {ai_response}")

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
    