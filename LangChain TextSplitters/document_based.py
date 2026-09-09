from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

docs = """
class Student:
  
    school_name = "Data Institute of Technology"

    def __init__(self, name: str, roll_no: int):
        self.name = name          # Instance variable
        self.roll_no = roll_no    # Instance variable

    def display_info(self):
        print(f"Student: {self.name} | Roll No: {self.roll_no} | School: {self.school_name}")

# --- Driver Code ---
# Instantiating an object
student1 = Student("Ravi", 101)
student1.display_info()

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=200,
    chunk_overlap=0,
)

result = splitter.split_text(docs)

print(result) 