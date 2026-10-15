import ollama

print("Bonjour, je suis ton assistant intelligent, comment je peux t'aider ?")
question = input()

rep_affiche = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": question}]
    )

print(rep_affiche["message"]["content"])