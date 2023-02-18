
import openai, os

openai.api_key = "[YOUR_API_KEY]"

def generate_response(prompt, max_tokens = 150):
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = max_tokens,
        n = 1,
        stop = None,
        temperature = 0.7)
    message = response.choices[0].text.strip()
    return message

print()
prompt = input("Enter prompt: ")
response = generate_response(prompt)

print(f'\nResponse: {response}\n')
