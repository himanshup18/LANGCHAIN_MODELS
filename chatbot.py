from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file

model = ChatOpenAI()

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break      
    result = model.invoke(user_input)  # ask a question
    print("AI:", result.content)