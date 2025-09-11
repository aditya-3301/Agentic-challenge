# FastMCP 2
from fastmcp import FastMCP
import requests
import streamlit as st

# Retrieve API key from Streamlit secrets
weather_api_key = st.secrets.get("weather_api_key")

# Create a FastMCP instance
mcp = FastMCP("weather_mcp")

@mcp.tool()
def get_weather(city):
    if not city:
        return "Please provide a valid city name."
    print(f"Getting weather in {city}\n\n")

    if not weather_api_key:
        return "Weather API key not found. Please check your configuration."

    # Build the request URL
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)

    # Handle non-200 responses
    if response.status_code != 200:
        data = response.json()
        return f"Could not get weather for '{city}': {data.get('message', 'Unknown error')}"

    data = response.json()

    # Check for required data fields
    if "main" not in data or "weather" not in data:
        return "Incomplete weather data received."

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"It's {description}, {temp}°C in {city}."

if __name__ == "__main__":
    mcp.run()
