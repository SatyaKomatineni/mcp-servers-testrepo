# Development Notes

# Available MCP tools:

Here are the available tools with their descriptions:

1. **lookup_claim**: Looks up a medical claim by its ID.

Parameters: claim_id (string) - The unique identifier of the claim.

2. **lookup_provider**: Looks up a healthcare provider by their National Provider Identifier (NPI).

Parameters: npi (string) - The National Provider Identifier (NPI) of the provider.

3. **search_prompts**: Searches for prompts that contain any of the words in the search string.

Parameters: search_string (string) - The search string to match against prompts.

4. **vector_search**: Searches the vector database for relevant documents and returns aggregated results.

Parameters: search_query (string) - The search query string, separator (string) - String to use between aggregated results (default: "\n\n").

5. **lookup_system_by_id**: Looks up a system by its ID.

Parameters: system_id (string) - The unique identifier of the system to look up.

6. **getMCPServerTools**: Gets the list of available MCP server tools.

7. **add_numbers**: Adds two numbers together.

Parameters: a (number) - The first number to add, b (number) - The second number to add.

8. **weather**: Gets the weather in a location (fahrenheit). Note: this returns demo dummy data.

Parameters: location (string) - The location to get the weather for. 

9. **convertFahrenheitToCelsius**: Converts a temperature in fahrenheit to celsius.

Parameters: temperature (number) - The temperature in fahrenheit to convert.

10. **tell-me-a-joke-about**: Tells a joke about a subject. Note: this returns demo dummy data.

Parameters: subject (string) - The subject of the joke.

11. **query**: Queries the database with a SQL query.

Parameters: sql (string) - The SQL query to execute.


# Model and Test Data

Model: meta-llama/llama-4-scout-17b-16e-instruct
Test system: jenkins-01
Test claim: C005
Test drug: Ivermectin
Test provider: 3456789012


# Running the Servers

UI: test-assistant-ui-mcp: npm run dev

uv run mcp-provider-server.py
uv run mcp-claims-server.py
uv run mcp-prompts-server.py
uv run mcp-cmdb-server.py

mcp-vector-search: uv run mcp-pharmacy-server.py

mcp-demo-typescript:  
- npm run dev-streamable
- Also - npm run build to create server.js for stdio

