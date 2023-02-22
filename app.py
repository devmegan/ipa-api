import json

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"instructions": "use the /letter/{letter} endpoint to fetch the corresponding phonetic code word"}


@app.get("/letter/{letter}")
def read_item(letter: str):
    letter = letter.upper()

    file = open('ipa.json')
    
    ipa_data = json.load(file)
    word = ipa_data[letter]

    file.close()
    
    return {"letter": letter, "word": word}