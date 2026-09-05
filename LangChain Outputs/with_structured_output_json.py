from langchain_google_genai import GoogleGenerativeAI
from typing import TypedDict , Annotated , Optional ,Literal
from pydantic import BaseModel , Field
from dotenv import load_dotenv
load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.7-flash')

# Schema
json_schema = {
    "title":'Review',
    "type":"object",
    "properties": {
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":"Write down all the key themes discussed in the review in a list."
        },
        "summary":{
            "type":"string",
            "description":"A breif summary of the review."
        },
        "sentiment":{
            "type":"string",
            "enum":["pos" , "neg"],
            "description":"Return sentiment of the review either negative or positive."
        },
        "pros": {
            "type":["array" , "null"],
            "items": {
                "type":"string"
            },
            "description":"Write down all the pros inside a list."
        },
        "cons": {
                    "type":["array" , "null"],
                    "items": {
                        "type":"string"
                    },
                    "description":"Write down all the cons inside a list."
                },
    },
    "required": ["Key_themes" , "summary" , "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("prompt")
print(result)