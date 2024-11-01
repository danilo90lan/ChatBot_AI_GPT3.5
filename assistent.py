import json
import openai

with open("secret.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

openai.api_key = api_key

def get_response(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1.0
    )
    return response

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a virtual assistent and your name is JARVIS"}
    ]
    user_input = input("\nYou ")
    messages.append({"role": "user", "content": user_input})