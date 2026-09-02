from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='..', temperature=0.5)

result = model.invoke("Prompt")
print(result)
