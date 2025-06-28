# Example MCP Servers

This repo contains example developer MCP Servers.


## Initial Setup

The following sections contain setup instructions for Python and TypeScript examples.


## Python Servers

### Python Setup and Start Instructions

Note: Python projects have the same setup and start instructions:

Setup (one time):

```bash
cd <server directory>
uv venv
source .venv/bin/activate
```

To start:

```bash
make dev
```

### 1. Claims MCP Server

Test claims based on a pydantic model. Lookup by id.

Directory: [mcp-claims-python](./mcp-claims-python/)

See [Python Setup and Start Instructions](#python-setup-and-start-instructions)


### 2. System Configuration Management Database (CMDB) MCP Server

Test systems based on a pydantic model. Lookup by id.

Directory: [mcp-cmdb-python](./mcp-cmdb-python/)

See [Python Setup and Start Instructions](#python-setup-and-start-instructions)


### 3.  Prompts MCP Server

Test prompts based on a pydantic model. Search by keywords using role and descriptions.

Directory: [mcp-prompts-python](./mcp-prompts-python/)

See [Python Setup and Start Instructions](#python-setup-and-start-instructions)


### 4.  Provider MCP Server

Test providers based on a pydantic model. Lookup by id.

Directory: [mcp-provider-python](./mcp-provider-python/)

See [Python Setup and Start Instructions](#python-setup-and-start-instructions)


### 5.  Pharmacy MCP Server

Search a Chroma vector store loaded from a PDF with pharmacy drug information (see [pharmacydrugs.pdf](./mcp-vector-search/data/docs/pharmacydrugs.pdf)). Does a similarity search.

Directory: [mcp-vector-search](./mcp-vector-search/)

The vector store must be created before starting the MCP Server. The current implementation used an OpenAI embedding model and LangSmith for 
observability. You will need a LangSmith API key and an OpenAI API key.

To create the vector store, follow these steps:

1. `cd mcp-vector-search`
2. Copy `.env.example` to `.env`
3. In `.env`, fill in the keys for LANGSMITH_API_KEY and OPENAI_API_KEY:

  ```sh
  LANGSMITH_API_KEY=your-api-key-if-tracing
  OPENAI_API_KEY=your-api-key
  ```
4. Oepn the Jupyter notebook [load-store.ipynb](./mcp-vector-search/load-store.ipynb) and run all the cells.

5. See [Python Setup and Start Instructions](#python-setup-and-start-instructions) to start the MCP server.


## TypeScript Servers


### 1. Demo TypeScript MCP Server

This is the sample TypeScript MCP Server that has a tool to add two numbers. It is currently configured to run using the stdio transport.

Directory: [mcp-demo-typescript](./mcp-demo-typescript/)

Since this is configured to run with stdio transport, the typescript must be compiled:

1. `cd mcp-demo-typescript`
2. `npm install`
2. `npm run build`




