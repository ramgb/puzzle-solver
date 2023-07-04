import json

data = json.load(open('dicts/wordsapi_list.json'))

for key in data.keys():
    if len(key.split(" ")) == 1 and key.isalpha():
        print(key)