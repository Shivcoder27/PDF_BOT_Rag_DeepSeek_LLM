# PDF_ChatModel_Rag_DeepSeek_LLM

![Model Architecture](https://github.com/Shivcoder27/PDF_BOT_Rag_DeepSeek_LLM/blob/main/model_SS.png)

## Overview

**PDF_BOT_Rag_DeepSeek_LLM** is an AI-powered PDF chatbot that utilizes Retrieval-Augmented Generation (RAG) with **DeepSeek LLM** to efficiently extract, process, and generate insights from PDF documents. This project enables intelligent document interaction, summarization, and Q&A functionalities for users.

## Features

- Upload and parse PDF documents
- Query PDFs using natural language
- Retrieve relevant information using RAG
- Generate responses using DeepSeek LLM
- Scalable and efficient processing

## Installation

### Prerequisites

```bash
# Ensure you have the following installed:
Python 3.8+
pip
Git
Virtual Environment (optional but recommended)
```

### Clone the Repository

```bash
git clone https://github.com/Shivcoder27/PDF_BOT_Rag_DeepSeek_LLM.git
cd PDF_BOT_Rag_DeepSeek_LLM
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Application

```bash
python app.py
```

### Example Query

```plaintext
User: What is the summary of this document?
Bot: The document discusses...
```

## Configuration

Modify `config.py` to adjust:

```python
API_KEY = "your-api-key"
MODEL_PARAMETERS = {
    "temperature": 0.7,
    "max_tokens": 200
}
DATABASE_URI = "sqlite:///data.db"
```

## Contributing

We welcome contributions! To contribute:

```bash
git fork https://github.com/Shivcoder27/PDF_BOT_Rag_DeepSeek_LLM.git
cd PDF_BOT_Rag_DeepSeek_LLM
git checkout -b feature-branch
git commit -m "Add new feature"
git push origin feature-branch
```

Then, open a Pull Request.

## License

```plaintext
This project is licensed under the MIT License. See LICENSE for details.
```

## Contact

For queries, open an issue or reach out to [Shivcoder27](https://github.com/Shivcoder27).

