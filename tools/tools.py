
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    return f"Weather in {city}: Sunny, 72°F"

@tool
def get_air_quality_index(city: str) -> str:
    """Get polution or air quality index information for a city."""
    return f"Current {city} Air Quality Index (AQI) is 70 Moderate level"