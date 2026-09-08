from langchain_community.document_loaders import WebBaseLoader
url = 'https://my.clevelandclinic.org/health/drugs/18819-carbamide-peroxide-ear-solution'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
