# Level 1

Working with LLMs and reading PDFs using Python.
- API accessed: Google Gemini


## Tasks 

### 1. Call an LLM API
Makes a basic prompt-response call using Gemini.

### 2. Read a PDF
Use `pypdf` to load and extract text from a PDF file.

```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
print(reader.pages[0].extract_text())

