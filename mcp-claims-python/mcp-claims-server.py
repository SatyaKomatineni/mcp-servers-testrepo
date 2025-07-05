import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Run the Claims server with specified transport')
    parser.add_argument('--transport', 
                       choices=['streamable-http', 'stdio'],
                       default='stdio',
                       help='Transport type to use (default: stdio)')
    parser.add_argument('--host',
                       default='127.0.0.1',
                       help='Host for streamable-http transport (default: 127.0.0.1)')
    parser.add_argument('--port',
                       type=int,
                       default=9000,
                       help='Port for streamable-http transport (default: 9000)')

    args = parser.parse_args()
    
    if args.transport == 'streamable-http':
        mcp.run(transport=args.transport, host=args.host, port=args.port)
    elif args.transport == 'stdio':
        mcp.run(transport='stdio')
    else:
        raise ValueError(f"Invalid transport: {args.transport}")


if __name__ == "__main__":
    main()