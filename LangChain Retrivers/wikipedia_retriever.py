import wikipedia

wikipedia.set_user_agent(
    "GenAILearning/1.0 (your-email@example.com)"
)


from langchain_community.retrievers import WikipediaRetriever

# Initalize retriever
retriever = WikipediaRetriever(top_k_results=2 , lang="en")

# Define Your Query
query = "India Pakistan relations"

docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")