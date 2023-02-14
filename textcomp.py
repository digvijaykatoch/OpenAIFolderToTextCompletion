import openai
import os
import re

# Set up OpenAI API key and model
openai.api_key = "sk-blahblahlGLM" # Replace with you own api key. Get it from here: https://platform.openai.com/account/api-keys
model_engine = "davinci"

# Define function to train the model on the specified text data
def train_model(folder_path):
    # Get all text files in the specified folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # Combine all text files into a single string
    text = ""
    for file in text_files:
        with open(os.path.join(folder_path, file), 'r') as f:
            text += f.read()

    # Clean up the text by removing extra whitespace and special characters
    text = re.sub('\s+', ' ', text)
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)

    # Train the OpenAI model on the cleaned text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Return the model response
    return response.choices[0].text

# Define function to run the chatbot
def run_chatbot():
    # Start the chatbot loop
    while True:
        # Get user input
        question = input("Ask me a question: ")

        # Persist the question
        with open('question_log.txt', 'a') as f:
            f.write(question + '\n')

        # Generate a response from the OpenAI model
        response = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Print the response to the user
        print(response.choices[0].text)

# Train the OpenAI model on the specified text data
model_response = train_model('folder_path_with_text_files')

# Print the trained model response for testing
print(model_response)

# Run the chatbot
run_chatbot()
