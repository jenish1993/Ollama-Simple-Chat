import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.tools import get_weather, get_air_quality_index, search

def gemini_weather_forecast(prompt:str):
    GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        api_key = GOOGLE_API_KEY
    )

    agent = create_agent(
        model = llm,
        tools = [search, get_weather, get_air_quality_index],
        name="Gemini Weather forecast"
    )

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

    return result["messages"][-1].content