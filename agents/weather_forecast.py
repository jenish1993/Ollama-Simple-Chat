import os
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.messages import SystemMessage, HumanMessage
from tools.tools import get_weather
#from langgraph.checkpointer.memory import InMemoryServer

MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")

def weather_forecast_agent(prompt:HumanMessage) -> str:

    SYSTEM_PROMPT = """
        You are an weather forecast expert. You will always use provided tools to fulfill user query.
        Tools: get_weather: Get weather for a given city. and you will have to extract city name from user query.
        else you could respond "It's always sunny in @city.
        No more small talk please.
        """
    
    llama_model = ChatOllama(
        model = "llama3.2:1b",
        temperature=1, # set it very low because we don't want creative answers we want to call a tool and provide pricise answers.
        max_tokens=1000,
        timeout=30, # sets timeout so that if model fails to answer it times out.
        system_prompt=SystemMessage(
            content=[
                {
                    "type":"text",
                    "text": SYSTEM_PROMPT
                }
            ]
        ),
        #checkpointer = InMemoryServer()
    )

    tools= [get_weather]

    agent = create_agent(llama_model, tools, name="weather_assitant")

    result = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content": prompt + "\n" 
                    + "Include Air Quality Index at this city."
                }
            ]
        }
    )

    return result["messages"]