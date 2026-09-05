from langchain_google_genai import GoogleGenerativeAI
from typing import TypedDict , Annotated , Optional ,Literal
from dotenv import load_dotenv
load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.7-flash')

class Review(TypedDict):
    key_themes: Annotated[list[str], "write down all the key themes discussed in the review in a list."]
    summary:Annotated[str, "A breif summary of the review."]
    sentiment:Annotated[Literal["pos" , "neg"],"Return sentiment of the review either positive or negative."]
    pros:Annotated[Optional[list[str]], "Write down all the pros inside a list."]
    cons:Annotated[Optional[list[str]], "Write down all the cons inside a list."]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("prompt")