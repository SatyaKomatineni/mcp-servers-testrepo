from fastmcp import FastMCP
from typing import Optional
from models import System
from test_data import test_systems
import argparse


mcp = FastMCP("System Configuration Management Database Server")

@mcp.tool()
def lookup_system_by_id(system_id: str) -> Optional[System]:
    """
    Look up a system by its ID.
    
    Args:
        system_id: The unique identifier of the system to look up
        
    Returns:
        The System object if found, None otherwise
    """
    for system in test_systems:
        if system.id == system_id:
            return system
    return None


def main():
    parser = argparse.ArgumentParser(description='Run the CMDB server with specified transport')
    parser.add_argument('--transport', 
                       choices=['streamable-http', 'stdio'],
                       default='stdio',
                       help='Transport type to use (default: stdio)')
    parser.add_argument('--host',
                       default='127.0.0.1',
                       help='Host for streamable-http transport (default: 127.0.0.1)')
    parser.add_argument('--port',
                       type=int,
                       default=9001,
                       help='Port for streamable-http transport (default: 9001)')

    args = parser.parse_args()
    
    if args.transport == 'streamable-http':
        mcp.run(transport=args.transport, host=args.host, port=args.port)
    elif args.transport == 'stdio':
        mcp.run(transport='stdio')
    else:
        raise ValueError(f"Invalid transport: {args.transport}")


if __name__ == "__main__":
    main()