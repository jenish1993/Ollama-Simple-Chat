import os
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from tools.tools import get_weather

MODEL = os.environ.get("OLLAMA_MODEL", "ollama:llama3.2:1b")

def weather_forecast_agent(prompt:str) -> str:

    SYSTEM_PROMPT = """
        You are an weather forecast expert. You will always use provided tools to fulfill user query.
        Tools: get_weather: Get weather for a given city. and you will have to extract city name from user query.
        """
    
    llama_model = ChatOllama(
        model = MODEL,
        temperature=0.1, # set it very low because we don't want creative answers we want to call a tool and provide pricise answers.
        max_tokens=1000,
        timeout=30, # sets timeout so that if model fails to answer it times out.
    )

    agent = create_agent(
        model = MODEL,
        tools = [get_weather],
        system_prompt = SYSTEM_PROMPT
    )

    result = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content": prompt
                }
            ]
        }
    )

    return result["messages"][-1].content_blocks