import requests
import json

# Set up the base URL for local Ollama API
url = "http://127.0.0.1:11434/api/chat"

# Define the payload (your input prompt)

payload = {
    "model": "llama3.2:1b", # model replace here
    "messages": [{"role": "user", "content": "What is Python?"}] 
}

# send the HTTP POST request with streaming enabled
response = requests.post(url, json=payload, stream=True)

# Check the response status

if response.status_code == 200:
    print("Streaming response from Ollama:")
    for line in response.iter_lines(decode_unicode=True):
        if line: # Ignore empty lines
            try:
                # parse each line as a JSON object
                json_data = json.loads(line)
                # Extract and print the assistant's message content
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()
else:
    print(f"Error: {response.status_code}")
    print(response.text)