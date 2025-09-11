# Level 2: Building Agent Behaviors

This level focuses on building a **mini-agent** using the **FastMCP** protocol. 
A simple MCP tool that responds to weather-related queries.

# Level 1
- API accessed: Google Gemini
- Make sure all the libraries imported are installed
- (Streamlit,google.generativeai,pypdf,fastmcp)
- pip install streamlit google-generativeai fastmcp requests


## Procedure:

### To run locally:
1. Create a **folder** `.streamlit/` in the same level as the python file of level 2.
2. Inside it, create a file `secrets.toml`
3. Add your API key there exactly as this:
```__api_key = "YOUR_KEY_HERE"__```
```__weather_api_key = "YOUR_KEY_HERE"__```
4. Open VSCode Terminal
5. Make sure the current directory in terminal is level2
6.Open command prompt and run the server using: fastmcp run weather_mcp.py
7.Open another command prompt with level2 directory run it using: python run weather-mcp.py

---
## Project Structure

```
Agentic-challenge/
├── level1/
│ ├── README.md
│ ├── llm_call.py
│ ├── pdf_reader.py
│ └── .streamlit/
│     └── secrets.toml
├── level2/
│ ├── README.md
│ └── .streamlit/
│     └── secrets.toml
└── README.md
```
---
