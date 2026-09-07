from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model1 = ChatHuggingFace(llm = llm1)
model2 = ChatHuggingFace(llm = llm2)
model3 = GoogleGenerativeAI(model='gemini-3.7-flash')

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes->{notes} and quiz->{quiz}',
    input_variables=['notes' , 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model3 | parser

chain = parallel_chain | merge_chain

text = """
A black hole is a region of space where gravity is so strong that nothing, not even light, can escape from it. Black holes usually form when a very massive star reaches the end of its life and collapses under its own gravity. This collapse can compress a huge amount of matter into an extremely small region called a singularity, according to classical general relativity.

The boundary surrounding a black hole is called the event horizon. Once an object crosses this boundary, it cannot return to the outside universe. Black holes are not cosmic vacuum cleaners; objects can orbit them just as planets orbit stars if they are at a safe distance.

Scientists cannot directly see a black hole because it does not emit visible light. However, they can detect black holes by observing their effects on nearby stars, gas, and light. When matter falls toward a black hole, it can form a very hot accretion disk that emits powerful radiation.

Black holes can have different masses, ranging from stellar-mass black holes to supermassive black holes found at the centers of galaxies. Studying black holes helps scientists understand gravity, space, time, and the extreme conditions of our universe.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()