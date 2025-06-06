# MCP-Python-fast-agent

This directory provides a minimal example of hosting a simple MCP server using `fast-agent`.

The server exposes three tools:

- **AddBlock** – store a block of text
- **DeleteBlock** – remove a previously stored block
- **GetBlocks** – return all stored blocks

The example uses the `FastMCP` server from the `mcp` package. Clients can connect
via STDIO or SSE to call these tools.
