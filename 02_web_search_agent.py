
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel
)

# Connect Google Gemini
model = LiteLLMModel(
    model_id="gemini/gemini-flash-lite-latest"
)

# Create Web Search Tool
search_tool = DuckDuckGoSearchTool(
    max_results=5
)

# Create Agent
agent = CodeAgent(
    tools=[search_tool],
    model=model,
    max_steps=5
)

# Run Agent
result = agent.run(
    "Search for the best AI Agent frameworks in 2026. "
    "Compare smolagents, LangGraph and CrewAI."
)

print("\nFinal Answer:")
print(result)
