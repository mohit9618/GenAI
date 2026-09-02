from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name ='..')

text = "Delhi is the capital of india."

result = embedding.embed_query(text)

print(str(result))