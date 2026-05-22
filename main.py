from agents.weather_forecast import weather_forecast_agent

def main():
    PROMPT = "what is weather in Ahmedabad?"
    result = weather_forecast_agent(prompt=PROMPT)
    
    print(result)

if "__Main__":
    main()