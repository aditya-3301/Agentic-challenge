# Level 1
- API accessed: Google Gemini
- Make sure all the libraries imported are installed
- (Streamlit,google.generativeai,pypdf)

## Procedure:

### To run locally:
1. Create a **folder** `.streamlit/` in the same level as the python file of level 1.
2. Inside it, create a file `secrets.toml`
3. Add your API key there exactly as this:
   __api_key = "YOUR_KEY_HERE"__
4. Open VSCode Terminal
5. Make sure the current directory in terminal is level1
6. Type "streamlit run llm_call" in terminal to open streamlit app
7. In general, type "streamlit run _filename.py_" to run it .
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
