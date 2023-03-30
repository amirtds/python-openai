import os

from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt, download_loader


load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()
documents = loader.load_data(urls=['https://testdriven.io/blog/django-custom-user-model/'])
index = GPTSimpleVectorIndex(documents)

index.save_to_disk('./indexed_articles/django_custom_user_model.json')