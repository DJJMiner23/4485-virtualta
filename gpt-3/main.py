# Need to install these if it doesn't work for you
# pip install llama_index
# pip install openai

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = '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'

reader = SimpleDirectoryReader("./data")
documents = reader.load_data()
index = GPTVectorStoreIndex(documents)

query_engine = index.as_query_engine()
response = query_engine.query("what should I study for exam 1?")  # insert question here
print(response)
