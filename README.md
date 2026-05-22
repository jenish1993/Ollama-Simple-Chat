# Ollama Simple Chat - Weather Forecast AI

A LangGraph-based AI weather forecast application that uses local LLM models via Ollama and LangChain to intelligently extract city names from user queries and provide weather information.

## Project Overview

This project demonstrates how to build an intelligent agent using:
- **LangChain**: Framework for building applications with language models
- **Ollama**: Local LLM execution without cloud dependencies
- **LangGraph**: Computational graphs for agent workflows
- **Python**: Core programming language

The application features a weather forecast agent that understands natural language queries, extracts city information, and provides weather forecasts.

## Project Structure

```
Ollama-Simple-Chat/
├── main.py                 # Entry point for the application
├── agents/
│   └── weather_forecast.py # Weather forecast agent implementation
├── tools/
│   └── tools.py           # Tool definitions (get_weather)
├── Pipfile                # Pipenv dependency specification
└── README.md             # This file
```

## Features

- **Intelligent Weather Agent**: Understands natural language queries and extracts city names
- **Local LLM Support**: Uses Ollama for local model inference
- **Tool Integration**: Demonstrates tool use with LangChain agents
- **Customizable Models**: Supports different Ollama models via environment variables
- **Temperature Control**: Configurable model parameters for precise responses

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- pip or pipenv for package management

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jenish1993/Ollama-Simple-Chat.git
   cd Ollama-Simple-Chat
   ```

2. **Install Ollama**
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - Start the Ollama service: `ollama serve`

3. **Install Python Dependencies**

   **Option A: Using Pipenv (Recommended)**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

   **Option B: Using pip**
   ```bash
   pip install langchain langchain-ollama
   ```

4. **Pull a model with Ollama**
   ```bash
   ollama pull llama3.2:1b
   # or use another model like:
   # ollama pull mistral
   # ollama pull neural-chat
   ```

## Configuration

### Environment Variables

- `OLLAMA_MODEL`: Specify which Ollama model to use
  - Default: `ollama:llama3.2:1b`
  - Example: `export OLLAMA_MODEL=ollama:mistral:7b`

### Model Parameters

In `agents/weather_forecast.py`, you can customize:
- `temperature`: Controls creativity (0.1 = precise, 1.0 = creative)
- `max_tokens`: Maximum response length
- `timeout`: Response timeout in seconds

## Usage

### Run the Application

```bash
python main.py
```

### Example Queries

The agent can understand various natural language queries:
- "What is the weather in Ahmedabad?"
- "Tell me the weather for New York"
- "How's the weather in London?"

### Modify the Query

Edit `main.py` to change the query:
```python
PROMPT = "what is weather in Paris?"
result = weather_forecast_agent(prompt=PROMPT)
print(result)
```

### Use as a Library

```python
from agents.weather_forecast import weather_forecast_agent

result = weather_forecast_agent(prompt="What's the weather in Tokyo?")
print(result)
```

## Project Components

### Main Entry Point (`main.py`)
- Initializes the weather forecast agent
- Sends a user query about weather
- Prints the agent's response

### Weather Forecast Agent (`agents/weather_forecast.py`)
- Creates a LangChain agent with system prompt
- Configures Ollama model with specific parameters
- Invokes the agent with user messages
- Extracts and returns response content

### Tools (`tools/tools.py`)
- `get_weather(city: str)`: Returns weather information for a given city
- Currently returns mock data; can be extended with real weather APIs

## Troubleshooting

### Issue: Connection refused (Cannot connect to Ollama)
**Solution**: Ensure Ollama is running
```bash
ollama serve
```

### Issue: Model not found
**Solution**: Pull the model first
```bash
ollama pull llama3.2:1b
```

### Issue: Tool not being called
**Solution**: 
- Ensure the model has tool-calling capabilities
- Check system prompt clearly instructs the model to use tools
- Verify tool parameters match model expectations

### Issue: Slow responses
**Solution**:
- Use a smaller model: `ollama pull phi` (lightweight)
- Increase `timeout` value in the agent configuration
- Reduce `max_tokens` for faster generation

## Model Recommendations

- **Lightweight**: `phi`, `mistral:7b` (fast, lower memory)
- **Balanced**: `llama3.2:1b`, `neural-chat` (good speed/quality)
- **Powerful**: `llama2:7b`, `mistral:7b` (better quality, slower)

## Future Enhancements

- [ ] Integration with real weather APIs (OpenWeatherMap, etc.)
- [ ] Multi-turn conversation support
- [ ] Additional tools (location search, alerts)
- [ ] Web interface with Streamlit or FastAPI
- [ ] Docker containerization
- [ ] Response caching and optimization

## Dependencies

Key Python packages:
- `langchain`: LLM application framework
- `langchain-ollama`: Ollama integration for LangChain
- `ollama`: Ollama Python client

## License

This project is open source and available under the MIT License.

## Author

Created by [jenish1993](https://github.com/jenish1993)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

---

**Note**: This is a demonstration project for learning LangChain and Ollama. For production use, consider using established weather APIs and implementing proper error handling and caching strategies.
