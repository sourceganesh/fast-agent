from mcp.server.fastmcp import FastMCP

# In-memory list of text blocks
blocks: list[str] = []

# Create the MCP server
app = FastMCP(name="BlockAgentServer")


@app.tool(name="AddBlock", description="Add a block of text")
def add_block(text: str) -> str:
    """Add a new block to the list."""
    blocks.append(text)
    return f"Added block: {text}"


@app.tool(name="DeleteBlock", description="Remove a previously added block")
def delete_block(text: str) -> str:
    """Delete a block if it exists."""
    try:
        blocks.remove(text)
        return f"Deleted block: {text}"
    except ValueError:
        return f"Block not found: {text}"


@app.tool(name="GetBlocks", description="Return all stored blocks")
def get_blocks() -> list[str]:
    """Return the current list of blocks."""
    return blocks


if __name__ == "__main__":
    # Default to stdio transport for simplicity. Use --transport=sse to serve via SSE.
    app.run(transport="stdio")
