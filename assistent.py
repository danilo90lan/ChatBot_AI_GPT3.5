import json  # Import the json module for reading JSON files
import openai  # Import the OpenAI Python library for API interactions
import time  # Import the time module for adding delays in execution

# Load the API key from a secrets.json file
with open("secrets.json") as f:
    secrets = json.load(f)  # Read the JSON data from the file
    api_key = secrets["api_key"]  # Extract the API key from the loaded JSON data

# Set the OpenAI API key for authentication
openai.api_key = api_key

def get_response(messages: list):
    """
    Function to get a response from the OpenAI API based on the provided messages.
    
    Args:
        messages (list): A list of message dictionaries representing the conversation.
    
    Returns:
        str: The content of the assistant's response.
    """
    while True:  # Infinite loop to handle retries on rate limit errors
        try:
            # Call the OpenAI ChatCompletion API with the provided messages
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Specify the model to use
                messages=messages,  # Pass the conversation history
                temperature=1.0  # Set the randomness of the response
            )
            # Return the content of the first message in the response choices
            return response['choices'][0]['message']['content']
        # Uncomment the following lines to handle rate limit errors
        # except openai.error.RateLimitError:
        #     print("Rate limit exceeded. Retrying in 10 seconds...")  # Inform the user of the rate limit
        #     time.sleep(10)  # Wait 10 seconds before retrying
        except Exception as e:  # Catch all other exceptions
            print(f"An error occurred: {e}")  # Print the error message
            break  # Exit the loop if any other error occurs

if __name__ == "__main__":
    # Initialize the conversation with a system message
    messages = [
        {"role": "system", "content": "You are a virtual assistant and your name is JARVIS."}
    ]
    try:
        user_input = ""  # Initialize user_input to start the loop
        while user_input.lower() != "exit":  # Loop until the user types "exit"
            user_input = input("\nYou: ")  # Prompt the user for input
            messages.append({"role": "user", "content": user_input})  # Add the user input to the conversation
            
            # Get the assistant's response based on the conversation
            new_message = get_response(messages=messages)
            if new_message:  # Check if a new message was received
                print("\nJARVIS:", new_message)  # Print the assistant's response
                messages.append({"role": "assistant", "content": new_message})  # Add the assistant's response to the conversation
    except KeyboardInterrupt:  # Handle user interrupt (Ctrl+C)
        print("\nSee yaaa!!")  # Print a goodbye message