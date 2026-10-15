import ollama

reponse = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": "ta question ici"}
    ]
)

print(reponse)