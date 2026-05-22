from agents.weather_forecast import weather_forecast_agent

def main():
    #PROMPT = HumanMessage('weather in ahmedabad')
    result = weather_forecast_agent(prompt="Weather in ahmedabad")
    
    print(result)

if "__Main__":
    main()