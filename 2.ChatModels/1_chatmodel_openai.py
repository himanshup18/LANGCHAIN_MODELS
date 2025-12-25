from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file

model = ChatOpenAI(model="gpt-4", temperature=0.7)

result = model.invoke("What is the capital of India?")  # ask a question

print(result.content)