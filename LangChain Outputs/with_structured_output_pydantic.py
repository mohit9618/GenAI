from langchain_google_genai import GoogleGenerativeAI
from typing import TypedDict , Annotated , Optional ,Literal
from pydantic import BaseModel , Field
from dotenv import load_dotenv
load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.7-flash')

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="write down all the key themes discussed in the review in a list.")
    summary: str = Field(description="A breif summary of the review.")
    sentiment: Literal["pos" , "neg"] = Field(description="Return sentiment of the review either positive or negative.")
    pros: Optional[list[str]] = Field(default=None , description="Write down all the pros inside a list.")
    cons: Optional[list[str]] = Field(default=None , description="Write down all the cons inside a list.")
    name: Optional[str] = Field(default=None , description="Write the name of the reviewer.")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("prompt")