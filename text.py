import ollama

response = ollama.chat(
    model='gemma3:latest',
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response)