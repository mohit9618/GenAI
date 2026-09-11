from langchain_core.tools import tool

# s1 create function

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

# s2 add type hinting

def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b


# s3 add tool decorator

@tool
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3 , "b":5})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema())