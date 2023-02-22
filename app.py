import json

from fastapi import FastAPI, Path

tags_metadata = [
    {
        "name": "ipa",
        "description": "endpoints handling international phonetic alphabet",
    },
]

app = FastAPI(
    title="IPA API",
    version="0.0.1",
    description="Api that returns phonetic code words from the international phonetic alphabet",
    contact={
        "email": "devmegan@protonmail.com",
    },
    docs_url="/",
    openapi_tags=tags_metadata,
)

@app.get("/letter/{letter}", tags=["letter"])
def read_item(letter: str = Path(max_length=1, regex="^[a-zA-Z]$")):
    letter = letter.upper()

    file = open('ipa.json')
    
    ipa_data = json.load(file)
    word = ipa_data[letter]

    file.close()
    
    return {"letter": letter, "word": word}