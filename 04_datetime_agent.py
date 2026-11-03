
from smolagents import CodeAgent, LiteLLMModel

# 1. Connect Gemini model
model = LiteLLMModel(
    model_id="gemini/gemini-flash-lite-latest"
)

# 2. Create AI Agent
agent = CodeAgent(
    tools=[],
    model=model,
    max_steps=5,
    additional_authorized_imports=["datetime"]
)

# 3. Give a task to the Agent
result = agent.run(
    "Get today's date and calculate the date 7 days from today. "
    "Display both dates in YYYY-MM-DD format."
)

# 4. Display result
print("\nFinal Answer:")
print(result)
