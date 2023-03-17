This project demonstrates how to build a simple Q&A system using Python, Django, and OpenAI's GPT. The system can answer questions based on the context provided from a specific article. The user interface is built using HTML and Tailwind.

## Getting Started
1. Clone the repository:

```bash
    git clone https://github.com/amirtds/python-openai
```

1. Install the required packages:
    
```bash
    pip install -r requirements.txt
```

1. Create a `.env` file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key
```

1. Run migration and start the server:

```bash
    cd llm_api
    python manage.py migrate
    python manage.py runserver
```

1. Run the frontend:

```bash
    cd frontend
    python -m http.server 8080
```