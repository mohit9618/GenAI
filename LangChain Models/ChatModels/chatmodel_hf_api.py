from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="amd-quark/llama-tiny-fp8-quark-quant-method",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)
result = model.invoke("Who is the capital of India.")
print(result.content)