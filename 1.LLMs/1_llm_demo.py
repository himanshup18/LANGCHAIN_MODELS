from langchain_openai import OpenAI # pip install langchain-openai
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv() # take environment variables from .env file

llm = OpenAI(model = "gpt-3.5-turbo-instruct") 

result = llm.invoke("What is the capital of India?") #ask a question

print(result)
