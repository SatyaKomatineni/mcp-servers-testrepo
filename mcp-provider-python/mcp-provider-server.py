from fastmcp import FastMCP
from sample_providers import sample_providers
from models import HealthcareProvider

mcp = FastMCP("MCP Server for Healthcare Provider")

@mcp.tool()
def lookup_provider(npi: str) -> dict:
    """
    Look up a healthcare provider by their National Provider Identifier (NPI).
    
    Args:
        npi: The National Provider Identifier (NPI) of the provider
        
    Returns:
        dict: Provider information if found, None if not found
    """
    for provider in sample_providers:
        if provider.npi == npi:
            return provider.model_dump()
    return None

mcp.run(transport="streamable-http", host="127.0.0.1", port=9004)