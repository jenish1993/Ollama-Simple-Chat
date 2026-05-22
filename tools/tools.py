
from langchain.tools import tool

#tool to get weather details
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"