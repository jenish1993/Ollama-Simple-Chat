import os
from langchain.agents import create_agent
from langchain.tools import tool

#tool to get weather details
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


MODEL = os.environ.get("OLLAMA_MODEL", "ollama:llama3.2:1b")

SYSTEM_PROMPT = """
You are an weather forecast expert. You will always use provided tools to fulfill user query.
Tools: get_weather: Get weather for a given city. and you will have to extract city name from user query.
"""

agent = create_agent(
    model = MODEL,
    tools=[get_weather],
    system_prompt="""you are an weather forecast expert. you will always use provided tools to fulfill user query."""
)

result = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content": "What is weather in Ahmedabad?"
            }
        ]
    }
)

print(result["messages"][-1].content_blocks)