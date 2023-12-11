import requests

api_key = '8c74dfe6-26a5-4ced-b5c7-b504e1a754cc'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
