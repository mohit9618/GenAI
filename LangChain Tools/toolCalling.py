from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
load_dotenv()

# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


# tool binding

llm = ChatGoogleGenerativeAI(model = 'gemini-3.7-flash')
llm_with_tools = llm.bind_tools([multiply])

# tool calling
query = HumanMessage('can you multiply 3 with 10.')
messages = [query]

result = llm_with_tools.invoke(messages)
messages.append(result)

# tool execution
tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)
