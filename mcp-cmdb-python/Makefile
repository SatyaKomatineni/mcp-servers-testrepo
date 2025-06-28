dev:
	uv venv .venv
	. .venv/bin/activate && uv run mcp-cmdb-server.py

dev-stdio:
	uv venv .venv
	. .venv/bin/activate && uv run mcp-cmdb-server.py --transport stdio

dev-streamable-http:
	uv venv .venv
	. .venv/bin/activate && uv run mcp-cmdb-server.py --transport streamable-http --host 127.0.0.1 --port 9003

# . .venv/bin/activate && uv run mcp-cmdb-server.py --transport streamable-http --host 127.0.0.1 --port 9005
# . .venv/bin/activate && uv run mcp-cmdb-server.py --transport stdio
