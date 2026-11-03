from smolagents import CodeAgent, LiteLLMModel, tool


@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggest a menu based on the occasion.

    Args:
        occasion: Type of party.
    """
    if occasion == "casual":
        return "Pizza, snacks and drinks."

    elif occasion == "formal":
        return "Three-course dinner with dessert."

    elif occasion == "superhero":
        return "Healthy food buffet."

    return "Custom menu for the party."


model = LiteLLMModel(
    model_id="gemini/gemini-flash-lite-latest"
)

agent = CodeAgent(
    tools=[suggest_menu],
    model=model,
    max_steps=5
)

# Publish to Hugging Face Hub
print("Publishing agent to Hugging Face Hub...")

#agent.push_to_hub(
#    "username/party-menu-agent",
#    private=True
#)

print("Agent created successfully!")
print("Ready to use locally.")

print("Agent publishing process completed!")