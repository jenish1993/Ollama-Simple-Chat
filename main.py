from agents.weather_forecast import weather_forecast_agent
from agents.gemini_weather_forecast import gemini_weather_forecast

def main():
    PROMPT = "what is weather in ahmedabad?"
    #result = weather_forecast_agent(prompt="Weather in ahmedabad")
    
    #calling Gemini.
    result = gemini_weather_forecast(prompt=PROMPT)
    
    print(result)

if "__Main__":
    main()