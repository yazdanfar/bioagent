import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt

model = "llama3.2:1b"
prompt = "what is python" # prompt from user
system_prompt =  # system prompt for example to be fun or as lawyer , ....

# send the query to the model
response = client.generate(model=model, prompt= prompt)

# Print the response from the model

print("Response from the Ollama:")
print(response.response)