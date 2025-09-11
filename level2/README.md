# Level 2: Building Agent Behaviors

This level focuses on building a **mini-agent** using the **FastMCP** protocol. 
A simple MCP tool that responds to weather-related queries.

# Level 1
- API accessed: Google Gemini
- Make sure all the libraries imported are installed
- (Streamlit,google.generativeai,pypdf,fastmcp)
- pip install streamlit google-generativeai fastmcp requests


## Procedure:

## 🚀 Procedure

### To Run Locally:

1. Create a **folder** named `.streamlit/` in the same directory as the Level 2 Python files(i.e. in the level2 folder).

2. Inside it, create a file called `secrets.toml`.

3. Add your API keys in the following format:

   ```toml
   api_key = "YOUR_KEY_HERE"
   weather_api_key = "YOUR_KEY_HERE"

4. Open VSCode Terminal
5. Make sure the current directory in terminal is level2

### Open command prompt and run the server using: fastmcp run weather_mcp.py
### Open another command prompt with level2 directory run it using: python run weather-mcp.py

---
## Project Structure

```
├── level2/
│ ├── README.md
│ └── .streamlit/
│     └── secrets.toml

```
---
