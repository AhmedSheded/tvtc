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

