from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()


from langchain_core.documents import Document

doc1 = Document(
        page_content="Artificial Intelligence is the field of building machines that can perform tasks that normally require human intelligence.",
        metadata={"topic": "AI"}
    )

doc2 =  Document(
        page_content="Machine Learning is a subset of Artificial Intelligence where computers learn patterns from data and use those patterns to make predictions.",
        metadata={"topic": "Machine Learning"}
    )

doc3 =  Document(
        page_content="Deep Learning uses neural networks with multiple layers to learn complex patterns from large amounts of data.",
        metadata={"topic": "Deep Learning"}
    )

doc4 = Document(
        page_content="Natural Language Processing enables computers to understand, process, and generate human language.",
        metadata={"topic": "NLP",}
    )

doc5 = Document(
        page_content="Generative AI models can create new content such as text, images, audio, and code based on patterns learned from training data.",
        metadata={"topic": "Generative AI",}
    )


vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2"),
    persist_directory='chroma_db',
    collection_name='sample'
)

# add docs
docs = [doc1, doc2, doc3, doc4, doc5]

vector_store.add_documents(docs)


# get

r1 = vector_store.get(include=['embeddings' , 'documents' , 'metadatas'])

# search
r2 = vector_store.similarity_search(
    query='What can a Generative model do?',
    k = 2
)


r3 = vector_store.similarity_search_with_score(
    query='What can a Generative model do?',
    k = 2
)


r4 = vector_store.similarity_search_with_score(
    query='neural networks',
    filter={"topic":"Deep Learning"}
)

# update document
updated_doc1 =  Document(
        page_content="Deep Learning uses neural networks with multiple layers to learn complex patterns from large amounts of data.",
        metadata={"topic": "ML DL"}
    )

vector_store.update_document(document_id='...' , document=updated_doc1)

# delete
vector_store.delete(ids=['...'])