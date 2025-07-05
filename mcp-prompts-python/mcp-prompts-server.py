from fastmcp import FastMCP
from models.prompt import Prompt
from typing import List
from test_data.test_prompts import test_prompts

mcp = FastMCP("Prompts Server")

@mcp.tool()
def search_prompts(search_string: str) -> List[Prompt]:
    """
    Search for prompts that contain any of the words in the search string.
    The search is case-insensitive and matches against name, role, and description fields.
    
    Args:
        search_string (str): The search string to match against prompts
        
    Returns:
        List[Prompt]: A list of matching prompts
    """
    # Split search string into words and convert to lowercase
    search_words = search_string.lower().split()
    
    # Filter prompts that match any of the search words
    matching_prompts = []
    for prompt in test_prompts:
        # Check if any search word matches any of the fields
        if any(
            word in prompt.name.lower() or
            word in prompt.role.lower() or
            word in prompt.description.lower()
            for word in search_words
        ):
            matching_prompts.append(prompt)
    
    return matching_prompts

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    # mcp.run()
    
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9003)