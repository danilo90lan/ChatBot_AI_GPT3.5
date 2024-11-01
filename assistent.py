import json
import openai
import time

# Load API key from secrets.json
with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

# Set the OpenAI API key
openai.api_key = api_key

def get_response(messages: list):
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1.0
            )
            return response['choices'][0]['message']['content']
        # except openai.error.RateLimitError:
        #     print("Rate limit exceeded. Retrying in 10 seconds...")
        #     time.sleep(10)  # Wait 10 seconds before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if any other error occurs

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a virtual assistant and your name is JARVIS."}
    ]
    
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        
        new_message = get_response(messages=messages)
        if new_message:
            print("JARVIS:", new_message)
            messages.append({"role": "assistant", "content": new_message})