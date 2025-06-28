import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"
import sqlite3 from "sqlite3";
import { promisify } from "util";
import { z } from "zod";

const app = express();
app.use(express.json());

// Helper to create DB connection
const getDb = () => {
  const db = new sqlite3.Database("database.db");
  return {
    all: promisify<string, any[]>(db.all.bind(db)),
    close: promisify(db.close.bind(db))
  };
};

// Create a single server instance
const server = new McpServer({
  name: "example-server",
  version: "1.0.0"
});

// Set up server resources, tools, and prompts

// server.resource(
//   "echo",
//   new ResourceTemplate("echo://{message}", { list: undefined }),
//   async (uri, { message }) => ({
//     contents: [{
//       uri: uri.href,
//       text: `Resource echo: ${message}`
//     }]
//   })
// );

// server.tool(
//   "echo",
//   "Echoes the message {message}",
//   { message: z.string() },
//   async ({ message }) => ({
//     content: [{ type: "text", text: `Tool echo: ${message}` }]
//   })
// );

server.tool(
  "tell-me-a-joke-about",
  "Tells a joke about a subject",
  { 
    subject: z.string().describe("The subject of the joke"), 
  },
  async ({ subject }) => {
    console.log("tell-me-a-joke-about:", subject);
    return {    
      content: [{ type: "text", text: `Ha ha. A joke about: ${subject}` }]
    }
  });

// server.prompt(
//   "echo",
//   { message: z.string() },
//   ({ message }) => ({
//     messages: [{
//       role: "user",
//       content: {
//         type: "text",
//         text: `Please process this message: ${message}`
//       }
//     }]
//   })
// );

server.resource(
  "schema",
  "schema://main",
  async (uri) => {
    const db = getDb();
    try {
      const tables = await db.all(
        "SELECT sql FROM sqlite_master WHERE type='table'"
      );
      return {
        contents: [{
          uri: uri.href,
          text: tables.map((t: {sql: string}) => t.sql).join("\n")
        }]
      };
    } finally {
      await db.close();
    }
  }
);

// server.tool(
//   "add",
//   "Add two numbers together",
//   { a: z.number(), b: z.number() },
//   async ({ a, b }) => {
//     console.log("add:", a, b);
//     return {
//       content: [{ type: "text", text: String(a + b) }]
//     }
//   });

server.tool(
  "query",
  "Queries the database with {sql}",
  { sql: z.string().describe("The SQL query to execute") },
  async ({ sql }) => {
    const db = getDb();
    try {
      const results = await db.all(sql);
      // console.log("results:", results);
      return {
        content: [{
          type: "text",
          text: JSON.stringify(results, null, 2)
        }]
      };
    } catch (err: unknown) {
      const error = err as Error;
      return {
        content: [{
          type: "text",
          text: `Error: ${error.message}`
        }],
        isError: true
      };
    } finally {
      await db.close();
    }
  }
);

// Map to store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Handle POST requests for client-to-server communication
app.post('/mcp', async (req: express.Request, res: express.Response) => {
  try {
    // Check for existing session ID
    const sessionId = req.headers['mcp-session-id'] as string | undefined;
    let transport: StreamableHTTPServerTransport;

    if (sessionId && transports[sessionId]) {
      // Reuse existing transport
      transport = transports[sessionId];
    } else if (!sessionId && isInitializeRequest(req.body)) {
      // New initialization request
      transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: () => randomUUID(),
        onsessioninitialized: (sessionId) => {
          // Store the transport by session ID
          transports[sessionId] = transport;
        }
      });

      // Clean up transport when closed
      transport.onclose = () => {
        if (transport.sessionId) {
          delete transports[transport.sessionId];
        }
      };

      // Connect to the MCP server
      await server.connect(transport);
    } else {
      // Invalid request
      res.status(400).json({
        jsonrpc: '2.0',
        error: {
          code: -32000,
          message: 'Bad Request: No valid session ID provided',
        },
        id: null,
      });
      return;
    }

    // Handle the request
    await transport.handleRequest(req, res, req.body);
  } catch (error) {
    console.error('Error handling MCP request:', error);
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: '2.0',
        error: {
          code: -32603,
          message: 'Internal server error',
        },
        id: null,
      });
    }
  }
});

// Reusable handler for GET and DELETE requests
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Handle GET requests for server-to-client notifications via SSE
app.get('/mcp', handleSessionRequest);

// Handle DELETE requests for session termination
app.delete('/mcp', handleSessionRequest);

app.listen(4000);
console.log("Server is running on port 4000");