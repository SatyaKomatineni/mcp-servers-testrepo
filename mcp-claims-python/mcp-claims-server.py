from fastmcp import FastMCP
from tests.test_claims import test_claims
from typing import Optional
from models.claim import MedicalClaim

mcp = FastMCP("Medical Claims Server")

# @mcp.tool()
# def greet(name: str) -> str:
#     return f"Hello, {name}!"

@mcp.tool()
def lookup_claim(claim_id: str) -> Optional[dict]:
    """
    Look up a medical claim by its ID.
    
    Args:
        claim_id: The unique identifier of the claim (e.g., "C001")
        
    Returns:
        A dictionary containing the claim details if found, None if not found
    """
    for claim in test_claims:
        if claim.claim_id == claim_id:
            # Convert the Pydantic model to a dictionary
            return claim.model_dump()
    return None

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    # mcp.run()
    
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)