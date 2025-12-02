from langchain.tools import tool

try:
    from langchain_community.tools import DuckDuckGoSearchRun
    search_engine = DuckDuckGoSearchRun()

    @tool("search", description="Search the web for medical information")
    def search_tool(query: str) -> str:
        return search_engine.run(query)

except Exception:
    @tool("search", description="Fallback search tool (no internet)")
    def search_tool(query: str) -> str:
        return f"[Search unavailable] Query: {query}"
