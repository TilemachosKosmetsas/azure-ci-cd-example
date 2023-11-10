from fastapi import FastAPI
import random

app = FastAPI()

# List of words to choose from
words = ["dog", "cat", "boy", "toy"]

@app.get("/")
def read_root():
    # Randomly select a word
    selected_word = random.choice(words)
    return {"word": selected_word}
