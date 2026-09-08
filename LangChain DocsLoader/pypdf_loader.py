from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnableParallel

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.7-flash')
prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

loader = PyPDFLoader('Devops.pdf')

docs = loader.load()

print(docs[0].page_content)
print(docs[1].metadata)