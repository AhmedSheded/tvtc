from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from django.conf import settings
import os

api_key = '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'
os.environ['OPENAI_API_KEY'] = api_key


def chatgpt(request):
    documents = SimpleDirectoryReader(settings.DATA_DIR).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(request)
    data = response.response
    return data

