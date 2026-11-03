from smolagents import CodeAgent, LiteLLMModel, tool

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggest a menu based on the occasion.

    Args:
        occasion: Type of party.
                  Allowed values: casual, formal, superhero.
    """

    if occasion == "casual":
        return "Pizza, snacks and drinks."

    elif occasion == "formal":
        return "Three-course dinner with dessert."

    elif occasion == "superhero":
        return "Healthy food buffet."

    else:
        return "Custom menu for the party."


model = LiteLLMModel(
    model_id="gemini/gemini-flash-lite-latest"
)

agent = CodeAgent(
    tools=[suggest_menu],
    model=model,
    max_steps=5
)

result = agent.run("Prepare a formal menu for the party.")

print(result)