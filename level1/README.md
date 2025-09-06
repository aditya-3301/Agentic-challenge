# Level 1
- API accessed: Google Gemini

## Procedure:

### To run locally:
1. Create a **folder** `.streamlit/` in the same level as the python file of level 1.
2. Inside it, create a file `secrets.toml`
3. Add your API key there exactly as this:
### api_key = "YOUR_KEY_HERE"
4. Make sure the current directory in terminal is level1
5. Type "streamlit run llm_call" in terminal to open streamlit app
6. In general, type "streamlit run _filename.py_" to run it .
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
