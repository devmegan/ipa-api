# [IPA API](https://devmegan.github.io/ipa-api/)

Api that returns phonetic code words from the international phonetic alphabet. 

Written with [FastAPI](https://fastapi.tiangolo.com/).

Clone and use `uvicorn app:app --reload` to run live server. API docs exist at `/docs`

## GET `/letter/{letter}`

Takes a case-insensitive letter as a path parameter and returns a json response with the letter and corresponsing phonetic code word.

eg: 

```
request: 

GET /letter/A

response:

{
    "letter":"A",
    "word":"Alfa"
}

```

### Validation

`/letter/{letter}` endpoint has some validation:
- letter parameter must be an uppercase or lowercase character from the English alphabet (a-z, A-Z)
- letter parameter must have a maximum length of 1 character