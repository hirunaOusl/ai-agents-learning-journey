from smolagents import CodeAgent, LiteLLMModel

# Connect to Google Gemini
model = LiteLLMModel(
    model_id="gemini/gemini-flash-lite-latest"
)

# Create a Code Agent
agent = CodeAgent(
    tools=[],
    model=model,
    max_steps=5
)

# Give a task to the agent
result = agent.run(
    "Calculate the sum of all even numbers from 1 to 100."
)

print("\nFinal Answer:")
print(result)