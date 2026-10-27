## LLM Model selection 
-   Initially used Ollama, the local model in machine but this was slow, 
hence switched to LiteLLM 
-   Created an API key in LiteLLM. Initially Web search was not working hence recreated the key with Brave search MCP tool and added tool section in code. 
-   In the AI tool added section for user to select a role which in turn changes the system prompt. 
-   Few local tools like dice roll, pwd generator aded. User input crudely passed to return tool output. A tools manager created to execute tools
-   Created embeddings using model 'nomic-embed-text' from ollama &  'text-embedding-3-large' from litellm. The cosine similarity was different in both instances for the sample input. 
-   Create embedding for documents in all the dataset.


## To do 
-   Need to add universal .env files to be used across modules.