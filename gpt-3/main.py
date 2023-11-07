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

while True:
    question = input()
    if question == 'bye':
        break
    else:
        response = query_engine.query(question)
        print(response)

# response = query_engine.query("what is covered on exam 3")  # insert question here
# print(response)