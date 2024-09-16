import openai
import os

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the messages for the chat-based model
messages = [
    {"role": "system", "content": "You are a helpful web developer."},
    {"role": "user", "content": "Create a cool and stylish HTML page with a very modern inline css with a header, footer, and a main section with some bloglike content. The page should have a modern design with a clean, minimalistic layout. Please also change it a bit each time you generate it"}
]

# Use the ChatCompletion API to get a response
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # Or "gpt-4"
    messages=messages,
    max_tokens=300
)

# Access the generated HTML content
generated_html = response.choices[0].message.content

# Save the generated HTML to the mounted volume (host)
output_path = '/app/data/generated_website.html'  # This path should be mounted to your host machine
with open(output_path, 'w') as f:
    f.write(generated_html)

print(f"Website HTML generated and saved to {output_path}!")
