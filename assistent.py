import json
import openai

# Load API key from secrets.json
with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

# Set the OpenAI API key
openai.api_key = api_key

def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    # Initialize the messages with a system message
    messages = [
        {"role": "system", "content": "You are a virtual assistant and your name is JARVIS."}
    ]
    
    while True:
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        
        new_message = get_response(messages=messages)
        print("JARVIS:", new_message)
        
        # Optionally, add the assistant's response to the messages to maintain context
        messages.append({"role": "assistant", "content": new_message})