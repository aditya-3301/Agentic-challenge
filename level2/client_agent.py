import asyncio
from fastmcp import Client
import google.generativeai as genai
import streamlit as st  # Just for getting the API key

# Get API key from Streamlit secrets
api_key = st.secrets.get("api_key")
if not api_key:
    print("API key not found. Add it to .streamlit/secrets.toml")
    exit(1)

# Configure Gemini
genai.configure(api_key=api_key.strip())

# User input
user_input = input("Get weather reports from any city, just type the name: (Type 'exit' to quit)\n")

if user_input.lower() == "exit":
    exit(0)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Ask Gemini to extract city name
response = model.generate_content(
    f'From the prompt: "{user_input}", extract the city name ONLY. '
    'If no city is given, respond with: "Please provide a city name."'
)

user_city = response.text.strip()

if "provide a city name" in user_city.lower():
    print(response.text)
    exit(0)

# Async function to call the tool
async def main():
    client = Client("weather_mcp.py")
    async with client:
        result = await client.call_tool("get_weather", {"city": user_city})
        print("Calling weather request with city:", user_city,"\n\n")
        if result.content:
            print(result.content[0].text)
        else:
            print("No content in result.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
